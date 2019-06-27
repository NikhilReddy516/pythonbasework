import logging
import logging.config

MAIN_LOG_SETTINGS = {

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
			'filename' : './main.log',
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

		'main' : {
			'level' : 'INFO',
			'handlers' : ['fileHandler','consoleHandler'],
			'propagate' : False
		}
	}


}


logging.config.dictConfig(MAIN_LOG_SETTINGS)

fileLogger = logging.getLogger('main')


from p1 import m1,m3
from p1.p2 import m2
from p1.p3 import m4



def main():

	fileLogger.info('This is info from main function Entry')
	fileLogger.warning('This is warn from main function')
	fileLogger.error('This is error from main function')
	m1.f1()
	m1.f2()
	m2.f3()
	m2.f4()
	m3.f5()
	m4.f6()
	fileLogger.info('This is info from main function Exit')

	return



if(__name__ == '__main__'):
	main()
