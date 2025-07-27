# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import datetime

import uno, unohelper
from com.sun.star.task import XJobExecutor
from com.sun.star.document import XEventListener


class HelloWorld(unohelper.Base, XJobExecutor, XEventListener):
    """
    Write a Python comment here
    """
    def trigger(self, args):
        frame = self.desktop.ActiveFrame
        window = frame.ContainerWindow
        window.Toolkit.createMessageBox(
            window,
            uno.Enum('com.sun.star.awt.MessageBoxType', 'WARNINGBOX'),
            uno.getConstantByName("com.sun.star.awt.MessageBoxButtons.BUTTONS_OK"),
            "HelloWorld",
            "Hello World! After you click OK, I will write Hello world in cell A1").execute()
        context = self.context
        contextdir = " ".join(dir(context))
        window.Toolkit.createMessageBox(
            window,
            uno.Enum('com.sun.star.awt.MessageBoxType', 'WARNINGBOX'),
            uno.getConstantByName("com.sun.star.awt.MessageBoxButtons.BUTTONS_OK"),
            "HelloWorld",
            "Got context successfully. Its type is {}. Here is everything it can do: {}".format(type(context), contextdir)).execute()
        window.Toolkit.createMessageBox(
            window,
            uno.Enum('com.sun.star.awt.MessageBoxType', 'WARNINGBOX'),
            uno.getConstantByName("com.sun.star.awt.MessageBoxButtons.BUTTONS_OK"),
            "HelloWorld",
            "Here are my globals: {}".format(str(globals()))).execute()
        window.Toolkit.createMessageBox(
            window,
            uno.Enum('com.sun.star.awt.MessageBoxType', 'WARNINGBOX'),
            uno.getConstantByName("com.sun.star.awt.MessageBoxButtons.BUTTONS_OK"),
            "HelloWorld",
            "Here are my locals: {}".format(str(locals()))).execute()
        document = self.document
        documentdir = " ".join(dir(document))
        window.Toolkit.createMessageBox(
            window,
            uno.Enum('com.sun.star.awt.MessageBoxType', 'WARNINGBOX'),
            uno.getConstantByName("com.sun.star.awt.MessageBoxButtons.BUTTONS_OK"),
            "HelloWorld",
            "Got document successfully. Its type is {}. Here is everything it can do: {}".format(type(document), documentdir)).execute()
        desktop = self.desktop
        desktopdir = " ".join(dir(desktop))
        window.Toolkit.createMessageBox(
            window,
            uno.Enum('com.sun.star.awt.MessageBoxType', 'WARNINGBOX'),
            uno.getConstantByName("com.sun.star.awt.MessageBoxButtons.BUTTONS_OK"),
            "HelloWorld",
            "Got desktop successfully. Its type is {}. Here is everything it can do: {}".format(type(desktop), desktopdir)).execute()
        controller = desktop.Controller
        controllerdir = " ".join(dir(controller))
        window.Toolkit.createMessageBox(
            window,
            uno.Enum('com.sun.star.awt.MessageBoxType', 'WARNINGBOX'),
            uno.getConstantByName("com.sun.star.awt.MessageBoxButtons.BUTTONS_OK"),
            "HelloWorld",
            "Got controller successfully. Its type is {}. Here is everything it can do: {}".format(type(controller), controllerdir)).execute()
        sheet = document.getSheets()[0]
        window.Toolkit.createMessageBox(
            window,
            uno.Enum('com.sun.star.awt.MessageBoxType', 'WARNINGBOX'),
            uno.getConstantByName("com.sun.star.awt.MessageBoxButtons.BUTTONS_OK"),
            "HelloWorld",
            "Got first sheet successfully").execute()
        sheet.getCellByPosition(0,0).setString("Hello world")
        window.Toolkit.createMessageBox(
            window,
            uno.Enum('com.sun.star.awt.MessageBoxType', 'WARNINGBOX'),
            uno.getConstantByName("com.sun.star.awt.MessageBoxButtons.BUTTONS_OK"),
            "HelloWorld",
            "Set cell successfully").execute()
        return
    # boilerplate code below this point
    def __init__(self, context):
        self.context = context
        # see https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1Desktop.html
        self.document = self.createUnoService("com.sun.star.frame.Document")
        self.desktop = self.createUnoService("com.sun.star.frame.Desktop")
        # see https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1DispatchHelper.html
        self.dispatchhelper = self.createUnoService("com.sun.star.frame.DispatchHelper")
        frame = self.desktop.ActiveFrame
        window = frame.ContainerWindow
        window.Toolkit.createMessageBox(
            window,
            uno.Enum('com.sun.star.awt.MessageBoxType', 'WARNINGBOX'),
            uno.getConstantByName("com.sun.star.awt.MessageBoxButtons.BUTTONS_OK"),
            "HelloWorld",
            "Finished initializing").execute()
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
    HelloWorld,
    "org.libreoffice.HelloWorld",
    ("com.sun.star.task.JobExecutor",))
