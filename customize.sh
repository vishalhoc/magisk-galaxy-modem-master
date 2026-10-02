#!/system/bin/sh
# Galaxy 5G Modem & Band Master v2.0 Installer
# Author: hoc

ui_print "****************************************"
ui_print "  📡 Galaxy 5G Modem & Band Master v2.0"
ui_print "  by hoc"
ui_print "  Samsung Galaxy M32 5G (MT6853)"
ui_print "****************************************"

ui_print "- Setting executable permissions..."
set_perm_recursive $MODPATH 0 0 0755 0644
set_perm $MODPATH/action.sh 0 0 0755
set_perm $MODPATH/service.sh 0 0 0755
set_perm $MODPATH/system/bin/modem_master 0 0 0755
set_perm $MODPATH/web/cgi-bin/api.cgi 0 0 0755

ui_print "- Registering modem_master binary..."
cp -f "$MODPATH/system/bin/modem_master" /data/adb/modem_master 2>/dev/null
chmod 755 /data/adb/modem_master 2>/dev/null

ui_print "- Web UI daemon configured on port 8092"
ui_print "  Open: http://localhost:8092 in browser"
ui_print "  Or tap Action button in Magisk app"
ui_print "****************************************"
ui_print "  Installation complete! Reboot recommended."
ui_print "****************************************"
