#!/usr/bin/env python

import os
import sys
import requests
import logging
import json
import getpass


# Triggers the notification on the mobile app
###############################################################
def trigger(webHookUrl,payload):
    try:
        response = requests.post(ifttWebHookUrl,data=payload)
    except requests.exceptions.RequestException as e:
        logger.error(e.response)
###############################################################

#iftt info
config_file = open('/etc/notify-me/notify-me.conf','r')
config_data = json.load(config_file)


ifttWebHookUrl = "https://maker.ifttt.com/trigger/{0}/with/key/{1}".format(config_data["iftt-event-name"],config_data["iftt-key"])

#initialize the logger
logging.basicConfig(filename = "/tmp/notify-me.log", format = "%(asctime)s %(message)s", filemode = 'w')
logging.getLogger("urllib3").setLevel(logging.CRITICAL)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#Executing the command
commandName = sys.argv[1]
commandStatus = os.system(commandName+' > /dev/null')

statusmessage = ""
if commandStatus == 0:
    statusmessage = "{}: execution successful".format(commandName)
    payload = {'value1':getpass.getuser(),'value2':statusmessage}
    trigger(ifttWebHookUrl,payload)
    
else:
    statusmessage = "{}: execution failed".format(commandName)
    logger.error(statusmessage)
