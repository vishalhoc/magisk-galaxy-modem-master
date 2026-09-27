#!/system/bin/sh
# Busybox HTTPD CGI handler for Galaxy 5G Modem & Band Master

printf "Content-Type: application/json\r\nAccess-Control-Allow-Origin: *\r\nCache-Control: no-cache\r\n\r\n"

QUERY="${QUERY_STRING}"
if [ "$REQUEST_METHOD" = "POST" ] && [ -n "$CONTENT_LENGTH" ] && [ "$CONTENT_LENGTH" -gt 0 ] 2>/dev/null; then
    read -n "$CONTENT_LENGTH" POST_DATA
    if [ -n "$POST_DATA" ]; then
        QUERY="$POST_DATA"
    fi
fi

ACTION=$(echo "$QUERY" | tr '&' '\n' | grep '^action=' | head -n 1 | cut -d '=' -f 2)
VAL=$(echo "$QUERY" | tr '&' '\n' | grep '^val=' | head -n 1 | cut -d '=' -f 2)

[ -z "$ACTION" ] && ACTION="status"

MM="/system/bin/modem_master"
if [ ! -x "$MM" ]; then
    MM="/data/adb/modules/galaxy-modem-master/system/bin/modem_master"
fi
if [ ! -x "$MM" ]; then
    MM="/data/adb/modem_master"
fi

case "$ACTION" in
    status)
        sh "$MM" status
        ;;
    set_network_mode)
        sh "$MM" set_network_mode "$VAL"
        ;;
    set_volte)
        sh "$MM" set_volte "$VAL"
        ;;
    set_vowifi)
        sh "$MM" set_vowifi "$VAL"
        ;;
    launch_servicemode)
        sh "$MM" launch_servicemode "$VAL"
        ;;
    revert)
        sh "$MM" revert
        ;;
    *)
        echo "{\"status\": \"error\", \"message\": \"Invalid CGI action $ACTION\"}"
        ;;
esac
