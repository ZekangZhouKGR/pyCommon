import logging
import sys
## 规划
### DEBUG基本应用
### 运维日志
### 用户日志

__application__ = 'pyCommon'

logging.basicConfig(level = logging.DEBUG,
    # format = '%(asctime)s.%(msecs)03d %(thread)d %(pathname)s:%(lineno)d %(levelname)s %(message)s',
    format = '%(asctime)s.%(msecs)03d %(thread)d %(name)s:%(lineno)d %(levelname)s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    stream = sys.stdout)

root = logging.getLogger(__application__)
root.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
logger.info('start {} logger with {} level'.format(__application__, root.level))