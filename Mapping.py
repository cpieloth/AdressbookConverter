import re
from Person import Person
from PersonCollection import PersonCollection
from Log import Log

class Mapping:
	
	def __init__(self, file):
		self._mapping = {}
		self._defaultValues = {}
		self._read(file)
		
	def _read(self, file):
		try:
			file = open(file, 'r')
			#SEP = ","
			SEP = "[\,,\s]"
			EMB = "\""
			regEx = re.compile(EMB + '([^' + EMB + ']+)' + EMB + SEP + EMB + '([^' + EMB + ']+)' + EMB + SEP + EMB + '([^' + EMB + ']*)' + EMB)
			for line in file:
				cols = regEx.match(line)
				if(cols != None): #TODO Gruppengroesze pruefen
					self._mapping[cols.group(1)] =  cols.group(2)
					self._defaultValues[cols.group(2)] =  cols.group(3)
			file.close()
			return True
		except IOError:
			Log.error(self.__class__, "IOError with file > " + file)
				
	def doMapping(self, pcSrc):
		pcDest = PersonCollection()
		# add headerNames to destination personCollection
		for kDest in self._mapping.values():
			pcDest.addHeader(kDest)
		# add srcPersons to destPersons with new headerNames
		for pSrc in pcSrc.getPersons():
			pDest = Person()
			for kSrc, kDest in self._mapping.items():
				attr = pSrc.getAttribute(kSrc)
				if((attr == Person.ATTR_NOT_AVAILABLE  or attr == "") and self._defaultValues[kDest] != ""):
					attr = self._defaultValues[kDest]
				pDest.setAttribute(kDest, attr)
			pcDest.addPerson(pDest)
		return pcDest
