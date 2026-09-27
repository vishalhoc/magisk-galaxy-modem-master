#!/system/bin/sh
# Galaxy 5G Modem & Band Master Background Service
MODDIR=${0%/*}

while [ "$(getprop sys.boot_completed)" != "1" ]; do
    sleep 3
done

chmod 755 "$MODDIR/system/bin/modem_master" 2>/dev/null
chmod 755 "$MODDIR/web/cgi-bin/api.cgi" 2>/dev/null
chmod 755 "$MODDIR/action.sh" 2>/dev/null

cp "$MODDIR/system/bin/modem_master" /data/adb/modem_master 2>/dev/null
chmod 755 /data/adb/modem_master 2>/dev/null

# Kill any existing or stale instance on port 8092
pkill -9 -f "8092" 2>/dev/null
sleep 1

# Start Web Server on port 8092
BUSYBOX="/data/adb/magisk/busybox"
if [ -x "$BUSYBOX" ]; then
    "$BUSYBOX" httpd -p 0.0.0.0:8092 -h "$MODDIR/web" -c "$MODDIR/web/httpd.conf"
fi

exit 0
