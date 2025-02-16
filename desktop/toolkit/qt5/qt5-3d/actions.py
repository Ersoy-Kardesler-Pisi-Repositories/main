#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools



def setup():
    shelltools.system("mkdir .git")
    pisitools.dosed(".qmake.conf", "5.15.3", "5.15.2")
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()


    pisitools.dodoc("LICENSE.GPL*")
