import configparser
import logging
import os


class Config:

    def __init__(self, filename):
        self.config = configparser.ConfigParser(defaults=self._provide_defaults())
        self.logger = logging.getLogger("config")

        if os.path.isfile(filename):
            self.logger.warn("log file not found: %s" % filename)
            self.config.read(filename)

    def _provide_defaults(self):
        return {
            "mqtt": {
                "broker_address": "127.0.0.1"
            }
        }

        # self.config['mqtt'][] = '127.0.0.1'
        # self.config['mqtt']['broker_port'] = 1883
        # self.config['chromecast']['connect_immediately'] = 'yes'

    def get_mqtt_broker_address(self):
        return self.config.get('mqtt', 'broker_address', fallback="127.0.0.1")

    def get_mqtt_broker_port(self):
        return self.config.getint('mqtt', 'broker_port', fallback=1883)

    def get_chromecast_connect_immediately(self):
        return self.config.getboolean('chromecast', 'connect_immediately', fallback=True)
