import logging

import pyCommon
from pyCommon.config import ConfigParser
from pyCommon.console import console_entry


logger = logging.getLogger(__name__)


def initArgumentParser(ap):
    ap.add_argument('-c', '--config', help = '读取配置', default = None)
    return ap


@console_entry(initArgumentParser)
def main(ap):
    logger.info('start main ...')

    conf = ConfigParser()
    if ap.config is not None:
        conf.safe_read(ap.conf)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])