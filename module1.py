import logging
from module2 import mod2

# create logger
logger = logging.getLogger('module1')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler(filename = 'module.log', mode='w')
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

#add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message for module1')
logger.info('info message for module1')
logger.warning('warn message for module1')
logger.error('error message for module1')
logger.critical('critical message for module1')

mod2()