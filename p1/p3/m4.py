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
			'format' : '%(module)s  %(levelname)s %(message)s',
		}
	},
	'loggers' : {
		'm4' : {
			'level' : 'INFO',
			'handlers' : ['fileHandler', 'consoleHandler']
		}

	}

}

logging.config.dictConfig(P1_LOG_SETTINGS)

fileLogger = logging.getLogger('m4')



def f6():
	fileLogger.info('This is info from f6 function Entry')
	fileLogger.warning('This is warn from f6 function')
	fileLogger.error('This is error from f6 function')
	fileLogger.info('This is info from f6 function Exit')
	return;
