#!/system/bin/sh
# Magisk Action Button Handler for Galaxy 5G Modem & Band Master
# Author: hoc
MODDIR=${0%/*}

echo "=========================================="
echo "  📡 Galaxy 5G Modem & Band Master"
echo "  Samsung Galaxy M32 5G (MT6853)"
echo "  Author: hoc"
echo "=========================================="
echo ""

# Ensure httpd is running and responsive on port 8092
if ! /data/adb/magisk/busybox wget -q -O - http://localhost:8092/ >/dev/null 2>&1; then
    echo "[*] Starting / reviving Modem Master daemon on port 8092..."
    pkill -9 -f "8092" 2>/dev/null
    sleep 1
    /data/adb/magisk/busybox httpd -p 0.0.0.0:8092 -h "$MODDIR/web" -c "$MODDIR/web/httpd.conf"
else
    echo "[✓] Modem Master daemon active on port 8092."
fi

echo "[*] Opening Modem Master Web UI in browser: http://localhost:8092 ..."

# Launch the default web browser to http://localhost:8092
am start -a android.intent.action.VIEW -d "http://localhost:8092" >/dev/null 2>&1

echo ""
echo "[✓] Browser launched successfully!"
echo "    URL: http://localhost:8092"
echo "=========================================="
exit 0
