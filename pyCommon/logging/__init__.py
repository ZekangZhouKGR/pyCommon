import logging
import sys

logging.basicConfig(level = logging.DEBUG,
    format = '%(asctime)s.%(msecs)03d %(filename)s %(levelname)s %(message)s',
    datefmt = '%a, %d %b %Y %H:%M:%S',
    stream = sys.stdout)
