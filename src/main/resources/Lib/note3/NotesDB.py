import decimal
try:
	import json
except ImportError:
	import simplejson as json

class NotesDB(object):
	def __init__(self, filename):
		self.filename = filename
		import os
		if os.path.exists(filename):
			self.entries = json.load(file(self.filename, "r"))
		else:
			self.entries = []
		self.listeners = []
	
	def remove(self, text):
		self.entries.remove(text)
		self.store()
		self.notifyListeners()
	
	def add(self, text):
		self.entries.append(text)
		self.store()
		self.notifyListeners()
	
	def store(self):
		f = file(self.filename, "w")
		json.dump(self.entries, f)
		f.close()

	def notifyListeners(self):
		for l in self.listeners:
			l()
