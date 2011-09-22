
from GuiImpl import *

class NoteEditImpl(GuiImpl):
	storedText = None
	
	def selected(self, text, new = False):
		self.storedText = text
		if text is None:
			self.textbox.text = ""
		else:
			self.textbox.text = text
		if new:
			self.db.add(newtext)
	
	def changed(self, newtext):
		if self.storedText is not None:
			if self.storedText == newtext:
				return
			print "removing ", self.storedText
			self.db.remove(self.storedText)
		self.storedText = newtext
		print "storing ", self.storedText
		self.db.add(newtext)
	
	def build(self, parent):
		print "building NoteEditImpl"
		self.textbox = Text(parent, SWT.MULTI)
		self.textbox.layoutData = horizontalFill(verticalFill(GridData()))
		self.db = self.structure.properties['model']
		
		self.textbox.addModifyListener(modifyListener(lambda event: self.changed(event.widget.text)))
		
		def f(event):
			if event.widget.caretLineNumber == 0:
				self.parent.focus()

		self.textbox.addKeyListener(keyPressListener(f, keycode = SWT.ARROW_UP | SWT.CTRL))
		
		for s in self.styles:
			print "NoteEditImpl style:", s
			self.apply_style(s)
		
	def focus(self):
		self.textbox.setFocus()
	
	def apply_style(self, style):
		if 'color' in style:
			c = style['color']
			self.textbox.setBackground(Color(self.textbox.display, c[0], c[1], c[2]))
		pass
	
	

