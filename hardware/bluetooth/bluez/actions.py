#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
  
    #shelltools.system("sed -i -e '/SystemdService/d' obexd/src/org.bluez.obex.service.in")
    pisitools.dosed("obexd/src/org.bluez.obex.service.in", "SystemdService", deleteLine=True)
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --libexecdir=/usr/libexec/ \
                         --enable-sixaxis \
                         --enable-experimental \
                         --disable-android \
                         --enable-cups \
                         --enable-datafiles \
                         --enable-optimization \
                         --enable-pie \
                         --enable-threads \
                         --enable-library \
                         --enable-tools \
                         --enable-manpages \
                         --enable-monitor \
                         --enable-udev \
                         --enable-test \
                         --enable-testing \
                         --enable-mesh \
                         --disable-systemd")
                         
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s install-pkglibexecPROGRAMS install-dbussessionbusDATA install-dbussystembusDATA install-dbusDATA install-man8" % get.installDIR())
 
    
    # Install conf files
    for i in ["profiles/input", "profiles/network" ,"src"]:
        pisitools.insinto("/etc/bluetooth", "%s/*.conf" % (i))
        
    
    # Simple test tools
    for i in ["bluezutils.py",
                "dbusdef.py",
                "example-advertisement",
                "example-gatt-client",
                "example-gatt-server",
                "ftp-client",
                "list-devices",
                "map-client",
                "monitor-bluetooth",
                "opp-client",
                "pbap-client",
                "sap_client.py",
                "simple-agent",
                "simple-endpoint",
                "simple-player",
                "test-adapter",
                "test-device",
                "test-discovery",
                "test-gatt-profile",
                "test-health",
                "test-health-sink",
                "test-hfp",
                "test-manager",
                "test-nap",
                "test-network",
                "test-profile",
                "test-sap-server"]:
        pisitools.dobin("test/%s" % i)
   # for i in 
      #  pisitools.dodoc("doc/%s" % i)
    # Install documents
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
