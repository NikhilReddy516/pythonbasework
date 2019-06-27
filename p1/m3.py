import logging
import logging.config

P1_LOG_SETTING = {
    'version' : 1,
	'disable_existing_loggers': False,
    'handlers' : {

        'consoleHandler' : {
            'class' : 'logging.StreamHandler',
            'level' : 'WARNING',
            'formatter' : 'normal',
            'stream' : 'ext://sys.stdout'
        },

        'fileHandler' :{
            'class' : 'logging.handlers.RotatingFileHandler',
            'level' : 'INFO',
            'formatter' : 'normal',
            'filename' : './p1/p1.log',
            'mode' : 'a',
            'maxBytes' : 10485760

        }


    },

    'formatters' : {

        'brief' : {
            'format' : '%(levelname)s %(message)s'
        },

        'normal' : {
            'format' : '%(module)s  %(levelname)s %(message)s'
        }


    },

    'loggers' : {
        'm3' : {
			'level' : 'INFO',
            'handlers' : ['fileHandler', 'consoleHandler']
        }

    }

}


logging.config.dictConfig(P1_LOG_SETTING)

fileLogger = logging.getLogger('m3')


def f5():
    fileLogger.info('This is info from f5 function Entry')
    fileLogger.warning('This is warn from f5 function')
    fileLogger.error('This is error from f5 function')
    fileLogger.info('This is info from f5 function Exit')
    return
