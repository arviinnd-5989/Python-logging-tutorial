import logging
logging.basicConfig(filename='example.log', filemode='w',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Oresund and Malmo')