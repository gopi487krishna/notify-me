
# notify-me
Script that uses IFTT to send the status of program being executed as a notification to the mobile device.

Place your credentials as a json file `notify-me.conf` in **/etc/notify-me** in the following format

    {
      "iftt-event-name": event-name,
      "iftt-key": key
    }
