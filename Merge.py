from Person import Person
from PersonCollection import PersonCollection
from Log import Log

class Merge:
	
	def merge(pcLeft, pcRight):
		# shared attributes are merged twice! :(
		Log.trace(__class__, "merge() called")
		pcMerge = PersonCollection()
		Merge._merge(pcMerge, pcLeft, pcRight)
		Merge._merge(pcMerge, pcRight, pcMerge)
		Log.trace(__class__, "merge() finished")
		return pcMerge
	
	def _merge(pcMerge, pcMaster, pcSlave):
		Log.trace(__class__, "_merge() called")
		# add headerNames in pcNew
		for kMaster in pcMaster.getHeaderNames():
			pcMerge.addHeader(kMaster)
		# Merge attributes of pcMaster to pcNew
		for pMaster in pcMaster.getPersons():
			pMerge = Merge.getPerson(pcMerge, pMaster)
			if(pMerge == None):
				pMerge = Person()
				pcMerge.addPerson(pMerge)
			pSlave = Merge.getPerson(pcSlave, pMaster)
			if(pSlave == None):
				# do copy of pMaster
				pSlave = Person()
			for kMaster in pcMaster.getHeaderNames():
				aMaster = pMaster.getAttribute(kMaster)
				aSlave = pSlave.getAttribute(kMaster)
				aMerge = Person.ATTR_NOT_AVAILABLE
				# Attribute is empty
				if((aMaster != "" or aMaster != Person.ATTR_NOT_AVAILABLE) and (aSlave == "" or aSlave == Person.ATTR_NOT_AVAILABLE)):
					aMerge = aMaster
				elif((aSlave != "" or aSlave != Person.ATTR_NOT_AVAILABLE) and (aMaster == "" or aMaster == Person.ATTR_NOT_AVAILABLE)):
					aMerge = aSlave
				# Attributes are not empty
				elif(aMaster == aSlave):
					aMerge = aMaster
				else:
					Log.warn(__class__, "merge conflict:\nMaster=" + aMaster + "\n Slave=" + aSlave)
				pMerge.setAttribute(kMaster, aMerge)
		Log.trace(__class__, "_merge() finished")
	
	def getPerson(pc, person):
		for p in pc.getPersons():
			if((person.getAttribute(Person.NAME_FIRST) == p.getAttribute(Person.NAME_FIRST)) and (person.getAttribute(Person.NAME) == p.getAttribute(Person.NAME))):
				return p
		Log.debug(__class__, "getPerson() not found")
		return None
		
#end
