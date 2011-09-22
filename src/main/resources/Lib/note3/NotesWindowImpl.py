
from GuiImpl import *

class NotesWindowImpl(GuiImpl):
	
	def build(self, parent = None):
		self.display = Display()
		self.shell = widgets.Shell(self.display)
		
		for c in self.children:
			c.build(self.shell)
		
		return self
		
	def launch(self):
		#self.shell.pack()
		self.shell.open()
		while not self.shell.isDisposed():
			v = self.display.readAndDispatch()
			if not v:
				self.display.sleep()
		self.shell.dispose()
	
	def apply_style(self, style):
		pass
	
	

