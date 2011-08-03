from Log import Log

class Person:

	ATTR_NOT_AVAILABLE = "undefined"
	
# BEGIN PREFDEFINE ATTRIBUTES
	NAME = "name"
	NAME_FIRST = "name_first"
	NAME_DISPLAY = "name_display"
	BIRTHDAY = "birthday"
	STREET = "street"
	POSTCODE = "postcode"
	CITY = "city"
	COUNTRY = "country"
	TELEPHONE = "telephone"
	MOBILEPHONE = "mobilephone"
	EMAIL_PRIVATE = "email_private"
	EMAIL = "email"
	COMPANY = "company"
# END PREFDEFINE ATTRIBUTES
	
	def __init__(self):
		self._attributes = {}
			
	def __str__(self):
		return self.getAttribute(Person.NAME) + ", " + self.getAttribute(Person.NAME_FIRST)
		
	def __repr__(self):
		return str(self.toString())
	
	def getAttribute(self, key):
		try:
			attr = self._attributes[key]
			if(attr == "" or attr == None):
				attr = Person,ATTR_NOT_AVAILABLE
			return attr
		except:
			Log.debug(self.__class__, "key does not exist =" + key)
			return Person.ATTR_NOT_AVAILABLE
	
	def setAttribute(self, key, value):
		self._attributes[key] = value
		
	def toString(self):
		s = ""
		for k, v in self._attributes.items():
			s = s + k + ": " + v + ", "
		return s

