import logging
import logging.config

P1_LOG_SETTINGS = {

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
			'filename' : './p1/p1.log',
			'mode' : 'a',
			'maxBytes' : 10485760
		}

	},
	'formatters' :{
		'brief' : {
			'format' : '%(levelname)-8s %(message)s'
		},
		'normal' : {
			'format' : '%(module)s %(levelname)s %(message)s',
		}
	},
	'loggers' : {

		'm1' : {
			'level' : 'INFO',
			'handlers' : ['fileHandler','consoleHandler']
		}

	}

}

logging.config.dictConfig(P1_LOG_SETTINGS)

fileLogger = logging.getLogger('m1')


def f1():
	fileLogger.info('This is info from f1 function Entry')
	fileLogger.warning('This is warn from f1 function')
	fileLogger.error('This is error from f1 function')
	fileLogger.info('This is info from f1 function Exit')
	return;



def f2():
	fileLogger.info('This is info from f2 function Entry')
	fileLogger.warning('This is warn from f2 function')
	fileLogger.error('This is error from f2 function')
	fileLogger.info('This is info from f2 function Exit')
	return;
