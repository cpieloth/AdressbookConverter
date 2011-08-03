class Level:
	
	NAME = "";
	VALUE = 0
	
	def __init__(self, name, value):
		self.NAME = name
		self.VALUE = value

class Log:
	
	ERROR = Level("ERROR", 1)
	WARN = Level("WARN", 2)
	INFO = Level("INFO", 4)
	TRACE = Level("TRACE", 8)
	DEBUG = Level("DEBUG", 16)
	
	ALL = 65535
	NORMAL = ERROR.VALUE + WARN.VALUE + INFO.VALUE

	logMask = NORMAL
	
	def log(level, clazz, message):
		if ((Log.logMask & level.VALUE) == level.VALUE):
			print("[" + level.NAME + "] " + str(clazz) + ": " + message)
	
	def error(clazz, message):
		Log.log(Log.ERROR, clazz, message)
			
	def warn(clazz, message):
		Log.log(Log.WARN, clazz, message)
			
	def info(clazz, message):
		Log.log(Log.INFO, clazz, message)
			
	def trace(clazz, message):
		Log.log(Log.TRACE, clazz, message)
			
	def debug(clazz, message):
		Log.log(Log.DEBUG, clazz, message)
