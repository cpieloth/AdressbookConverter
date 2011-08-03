from Log import Log
from Person import Person
from PersonCollection import PersonCollection
import re

class CSV:
	SUFFIX = ".csv"
	
	def read(fName):
		Log.trace(__class__, "read()")
		pCollection = PersonCollection()
		try:
			file = open(fName, 'r')
			isHeader = True
			#SEP = ',*'
			SEP = "[\,,\s]*"
			EMB = "\""
			regEx = re.compile(EMB + '([^' + EMB + ']*)' + EMB + SEP)
			for line in file:
				i = 0
				person = Person()
				for col in regEx.findall(line):
					if(isHeader):
						pCollection.addHeader(col)
						#self._headerNames.append(col)
					else:
						person.setAttribute(pCollection.getHeaderNames()[i], col)
						i += 1 
				if(isHeader):
					isHeader = False
				else:
					pCollection.addPerson(person)
					
			file.close()
			return pCollection
		except IOError:
			Log.error(__class__, "IOError with file > " + fName)
			return None
		
	def write(fName, pCollection):
		Log.trace(__class__, "write()")
		try:
			file = open(fName, 'w')
			SEP = ","
			EMB = "\""
			# write headerNames first
			sep = ""
			for col in pCollection.getHeaderNames():
				file.write(sep + EMB + col + EMB)
				if(sep != SEP):
					sep = SEP
			file.write("\n")
			# write persons
			for person in pCollection.getPersons():
				sep = ""
				for col in pCollection.getHeaderNames():
					file.write(sep + EMB + person.getAttribute(col) + EMB)
					if(sep != SEP):
						sep = SEP
				file.write("\n")
				
			file.close()
			return True
		except IOError:
			Log.error(__class__, "IOError with file > " + fName)
	

class VCARD:
	SUFFIX = ".vcf"
	
	def read(fName):
		Log.trace(__class__, "read()")
		Log.error(__class__, "Not yet implemented!")
		return None
			
	def write(fName, pCollection):
		Log.trace(__class__, "write()")
		try:
			# write persons
			for person in pCollection.getPersons():
				fName = person.getAttribute(Person.NAME_DISPLAY) + VCARD.SUFFIX
				file = open(fName, 'w')
				file.write("BEGIN:VCARD\nVERSION:2.1\n")
		
				file.write("N:" + person.getAttribute(Person.NAME) + ";" +  person.getAttribute(Person.NAME_FIRST) + '\n')
				file.write("FN:" + person.getAttribute(Person.NAME_DISPLAY) + '\n')
				file.write("TEL;CELL;VOICE:" + person.getAttribute(Person.MOBILEPHONE) + '\n')
				file.write("TEL;HOME;VOICE:" + person.getAttribute(Person.TELEPHONE) + '\n')
				file.write("EMAIL;PREF;INTERNET:" + person.getAttribute(Person.EMAIL_PRIVATE) + '\n')
				# file.write("BDAY:" + person.getAttribute(Person.BIRTHDAY) + '\n')
		
				file.write("END:VCARD")
				file.close()
				return True
		except IOError:
			Log.error(self.__class__, "IOError with file > " + file)


class InOut:
	def read(fName):
		if(fName.endswith(CSV.SUFFIX)):
			return CSV.read(fName)
		elif(fName.endswith(VCARD.SUFFIX)):
			return VCARD.read(fName)
		else:
			Log.error(__class__, "read() - File format not supported!")
			return None
		
	def write(fName, pCollection):
		if(fName.endswith(CSV.SUFFIX)):
			CSV.write(fName, pCollection)
		elif(fName.endswith(VCARD.SUFFIX)):
			VCARD.write(fName, pCollection)
		else:
			Log.error(__class__, "write() - File format not supported!")
