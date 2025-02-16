#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    pisitools.dosed("configure", "DISABLE_DEPRECATED", deleteLine=True)

    autotools.configure("--disable-static \
                         --disable-gtk-doc \
                         --enable-deprecated \
                         --with-systemdsystemunitdir=no \
                         --enable-introspection")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README")
