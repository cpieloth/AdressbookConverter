import re
from Person import Person

from Log import Log

class PersonCollection:
	
	def __init__(self):	
		self._headerNames = []
		self._persons = []
		
	def getHeaderNames(self):
		return self._headerNames
	
	def addHeader(self, header):
		# TODO change to set
		if(self._headerNames.count(header) == 0):
			self._headerNames.append(header)
		
	def deleteHeader(self, header):
		self._headerNames.remove(header)
		
	def getPersons(self):
		return self._persons
	
	def addPerson(self, person):
		self._persons.append(person)

	def deletePerson(self, person):
		self._persons.remove(person)
