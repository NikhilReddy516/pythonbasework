import logging
import logging.config

P2_LOG_SETTINGS = {

	'version' : 1,
	'disable_existing_loggers': False,
    'handlers' : {

		'consoleHandler' : {
			'class' : 'logging.StreamHandler',
			'level' : 'WARNING',
			'formatter' : 'normal',
			'stream' : 'ext://sys.stdout'

		},

		'fileHandler' : {
			'class' : 'logging.handlers.RotatingFileHandler',
			'level' : 'INFO',
			'formatter' : 'normal',
			'filename' : './p1/p2/p2.log',
			'mode' : 'a',
			'maxBytes' : 10485760
		}

    },

    'formatters' : {
		'breif' : {
			'format' : '%(levelname)s %(message)s'
		},
		'normal' : {
			'format' : '%(module)s  %(levelname)s %(message)s'
		}
    },

    'loggers' : {
		'm2' : {
			'level'  : 'INFO',
			'handlers' : ['fileHandler', 'consoleHandler']
		}
    }

}

logging.config.dictConfig(P2_LOG_SETTINGS)

fileLogger = logging.getLogger('m2')



def f3():

	fileLogger.info('This is info from f3 function Entry')
	fileLogger.warning('This is warn from f3 function')
	fileLogger.error('This is error from f3 function')
	fileLogger.info('This is info from f3 function Exit')
	return




def f4():
	fileLogger.info('This is info from f4 function Entry')
	fileLogger.warning('This is warn from f4 function')
	fileLogger.error('This is error from f4 function')
	fileLogger.info('This is info from f4 function Exit')
	return
