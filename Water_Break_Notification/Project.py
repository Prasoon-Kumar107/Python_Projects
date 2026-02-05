from plyer import battery,notification
import time
while(True):
    status = battery.status
    notification.notify(
        title=f"Reminder and battery status",
        message=f"Take a break and drink some water! and Battery Status is:{status}",
        timeout=5  # seconds
    )
    time.sleep(60)

