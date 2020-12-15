import queue
import threading
from os import path

import apprise

from utils.logger import log

TIME_FORMAT = "%Y-%m-%d @ %H:%M:%S"

APPRISE_CONFIG_PATH = "config/apprise.conf"


class NotificationHandler:
    enabled_handlers = []

    def __init__(self):
        if path.exists(APPRISE_CONFIG_PATH):
            log.info(f"Initializing Apprise handler using: {APPRISE_CONFIG_PATH}")
            self.apb = apprise.Apprise()
            config = apprise.AppriseConfig()
            config.add(APPRISE_CONFIG_PATH)
            # Get the service names from the config, not the Apprise instance when reading from config file
            for server in config.servers():
                log.info(f"Found {server.service_name} configuration")
                self.enabled_handlers.append(server.service_name)
            self.apb.add(config)
            self.queue = queue.Queue()
            #self.start_worker()
            self.enabled = True
        else:
            self.enabled = False
            log.info(f"No Apprise config found at {APPRISE_CONFIG_PATH}.")
            log.info(f"For notifications, see {APPRISE_CONFIG_PATH}_template")

    def send_notification(self, message, ss_name=[], **kwargs):
        if self.enabled:
            self.__send_message(message, ss_name)
            #self.queue.put((message, ss_name))

    def __send_message(self, message, ss_name):
        apb = apprise.Apprise()
        config = apprise.AppriseConfig()
        config.add(APPRISE_CONFIG_PATH)
        apb.add(config)
        if ss_name:
            apb.notify(body=message, attach=ss_name)
        else:
            apb.notify(body=message)

    def message_sender(self):
        while True:
            message, ss_name = self.queue.get()
            log.info(f"Dequeuing message: {message}")
            try:
                self.__send_message(message="test start")
            except:
                log.info(f"Error when notifying")

            if ss_name:
                log.info(f"Sending with ss_name")
                self.apb.notify(body=message, attach=ss_name)
            else:
                log.info(f"Sending with only message")
                self.apb.notify(body=message)
            log.info(f"Sent")
            self.queue.task_done()

    def start_worker(self):
        threading.Thread(target=self.message_sender, daemon=True).start()
