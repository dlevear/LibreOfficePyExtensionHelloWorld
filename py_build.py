#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from zipfile import ZipFile
import os, os.path, sys
scriptdir = os.path.dirname(os.path.abspath(sys.argv[0]))
extensionname = os.path.join('build', 'HelloWorld.oxt')
with ZipFile(extensionname, 'w') as myzip:
    os.chdir(scriptdir)
    for root, dirs, files in os.walk('.'):
        if '.git' in root:
            continue
        if 'build' in root:
            continue
        for name in files:
            if not name == extensionname:
                myzip.write(os.path.join(root, name))
