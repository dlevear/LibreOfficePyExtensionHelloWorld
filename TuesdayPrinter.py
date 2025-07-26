# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import datetime

import uno, unohelper
from com.sun.star.task import XJobExecutor
from com.sun.star.document import XEventListener


class TuesdayPrinter(unohelper.Base, XJobExecutor, XEventListener):
    """A service only printing on Tuesdays

    Its important that this service implements this interface:
        - https://api.libreoffice.org/docs/common/ref/com/sun/star/task/XJobExecutor.html
    has a trigger function. Because of that, it can be used in menus and toolbars, by using:

        service:org.libreoffice.TuesdayPrinter

    as a URL.
    """
    def trigger(self, args):
        if args == "printontuesday":
            frame = self.desktop.ActiveFrame
            window = frame.ContainerWindow
            window.Toolkit.createMessageBox(
                window,
                uno.Enum('com.sun.star.awt.MessageBoxType', 'WARNINGBOX'),
                uno.getConstantByName("com.sun.star.awt.MessageBoxButtons.BUTTONS_OK"),
                "HelloWorld",
                "Hello World!").execute()
    # boilerplate code below this point
    def __init__(self, context):
        self.context = context
        # see https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1Desktop.html
        self.desktop = self.createUnoService("com.sun.star.frame.Desktop")
        self.document = self.createUnoService("com.sun.star.frame.Document")
        # see https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1DispatchHelper.html
        self.dispatchhelper = self.createUnoService("com.sun.star.frame.DispatchHelper")
    def createUnoService(self, name):
        """little helper function to create services in our context"""
        # see https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1lang_1_1ServiceManager.html
        # see https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XMultiComponentFactory.html#a77f975d2f28df6d1e136819f78a57353
        return self.context.ServiceManager.createInstanceWithContext(name, self.context)
    def disposing(self, args):
        pass
    def notifyEvent(self, args):
        pass

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    TuesdayPrinter,
    "org.libreoffice.TuesdayPrinter",
    ("com.sun.star.task.JobExecutor",))
