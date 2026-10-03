#!/system/bin/sh
# Busybox HTTPD CGI handler for Galaxy 5G Modem & Band Master v2.0
# Author: hoc

printf "Content-Type: application/json\r\nAccess-Control-Allow-Origin: *\r\nCache-Control: no-cache, no-store\r\n\r\n"

QUERY="${QUERY_STRING}"
if [ "$REQUEST_METHOD" = "POST" ] && [ -n "$CONTENT_LENGTH" ] && [ "$CONTENT_LENGTH" -gt 0 ] 2>/dev/null; then
    read -n "$CONTENT_LENGTH" POST_DATA
    if [ -n "$POST_DATA" ]; then
        QUERY="$POST_DATA"
    fi
fi

get_param() {
    raw=$(echo "$QUERY" | tr '&' '\n' | grep "^$1=" | head -n 1 | cut -d '=' -f 2- | tr -d '\r\n')
    echo "$raw" | sed 's/%2C/,/g; s/%20/ /g; s/%2B/+/g; s/%2F/\//g'
}

ACTION=$(get_param action)
VAL=$(get_param val)
[ -z "$VAL" ] && VAL=$(get_param bands)
SLOT=$(get_param slot)
CODE=$(get_param code)
PCI=$(get_param pci)
ARFCN=$(get_param arfcn)
LABEL=$(get_param label)
PARAM=$(get_param param)
[ -z "$PARAM" ] && PARAM=$(get_param prop)

[ -z "$ACTION" ] && ACTION="status"

MM="/data/adb/modules/galaxy-modem-master/system/bin/modem_master"
if [ ! -x "$MM" ]; then
    MM="/system/bin/modem_master"
fi
if [ ! -x "$MM" ]; then
    MM="/data/adb/modem_master"
fi

case "$ACTION" in
    status)
        sh "$MM" status
        ;;
    set_network_mode)
        sh "$MM" set_network_mode "$VAL" "$SLOT"
        ;;
    set_nr_mode)
        sh "$MM" set_nr_mode "$VAL"
        ;;
    set_endc)
        sh "$MM" set_endc "$VAL"
        ;;
    set_lte_ca)
        sh "$MM" set_lte_ca "$VAL"
        ;;
    set_vonr)
        sh "$MM" set_vonr "$VAL"
        ;;
    set_volte)
        sh "$MM" set_volte "$VAL" "$SLOT"
        ;;
    set_vilte)
        sh "$MM" set_vilte "$VAL" "$SLOT"
        ;;
    set_vowifi)
        sh "$MM" set_vowifi "$VAL" "$SLOT"
        ;;
    set_wfc_mode)
        sh "$MM" set_wfc_mode "$VAL"
        ;;
    set_smsip)
        sh "$MM" set_smsip "$VAL" "$SLOT"
        ;;
    set_rcs)
        sh "$MM" set_rcs "$VAL" "$SLOT"
        ;;
    set_mobile_data)
        sh "$MM" set_mobile_data "$VAL"
        ;;
    set_data_roaming)
        sh "$MM" set_data_roaming "$VAL" "$SLOT"
        ;;
    set_smart_data_switch)
        sh "$MM" set_smart_data_switch "$VAL"
        ;;
    restart_radio)
        sh "$MM" restart_radio
        ;;
    launch_servicemode)
        sh "$MM" launch_servicemode "$CODE"
        ;;
    set_cell_target)
        sh "$MM" set_cell_target "$ARFCN" "$PCI"
        ;;
    add_target_cell)
        sh "$MM" add_target_cell "$ARFCN" "$PCI" "$LABEL"
        ;;
    remove_target_cell)
        sh "$MM" remove_target_cell "$ARFCN" "$PCI"
        ;;
    clear_target_cells)
        sh "$MM" clear_target_cells
        ;;
    apply_target_cells)
        sh "$MM" apply_target_cells
        ;;
    set_kernel_tweak)
        sh "$MM" set_kernel_tweak "$PARAM" "$VAL"
        ;;
    set_radio_prop)
        sh "$MM" set_radio_prop "$PARAM" "$VAL"
        ;;
    lock_bands)
        sh "$MM" lock_bands "$VAL" "$SLOT"
        ;;
    clear_band_lock)
        sh "$MM" clear_band_lock
        ;;
    revert)
        sh "$MM" revert
        ;;
    *)
        echo "{\"status\": \"error\", \"message\": \"Invalid CGI action: $ACTION\"}"
        ;;
esac
exit 0
