import sys
import os
from os.path import expanduser
import logging

from configparser import ConfigParser as BaseConfigParser


logger = logging.getLogger(__name__)


class ConfigParser(BaseConfigParser):
    """docstring for ConfigParser"""
    LOCAL_PATH = 'config.ini'
    USER_PATH = ['.config', 'pyCommon', 'config.ini']

    def __init__(self):
        super(ConfigParser, self).__init__()
        self._set_default()
        USER_PATH = os.path.join(expanduser('~'), *self.USER_PATH)
        self.safe_read(USER_PATH)
        self.safe_read(self.LOCAL_PATH)

    def safe_read(self, path):
        if os.path.isfile(path):
            try:
                self.read(path)
                return True
            except Exception as e:
                logger.warning('failed to load %s', path)
        return False

    def read(self, path):
        logger.info('read config from %s', path)
        super(ConfigParser, self).read(path)

    def _set_default(self):
        pass

    def save(self, path = None):
        path = path if path is not None else self.LOCAL_PATH
        with open(path, 'w', encoding='utf-8') as f:
            self.write(f)
        
        
def main(ap):
    config = ConfigParser()


if __name__ == '__main__':
    main(None)