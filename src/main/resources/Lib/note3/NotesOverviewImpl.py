#!/usr/bin/env python
#-*- coding:utf-8 -*-

from GuiImpl import *

class NotesOverviewImpl(GuiImpl):
	def build(self, parent):
		self.db = self.structure.properties['model']
		self.db.listeners.append(self.search)

		layout = GridLayout(1, False)
		print parent
		parent.setLayout(layout)
		
		# now we need a searchbox
		group = Composite(parent, 0)
		group.setLayout(GridLayout(2, False))
		label = Label(group, 0)
		label.text = "Search"
		self.searchbox = Text(group, SWT.SINGLE | SWT.SEARCH)
		self.searchbox.layoutData = horizontalFill(GridData())
		group.layoutData = horizontalFill(GridData())
		
		group = Composite(parent, 0)
		group.setLayout(GridLayout(2, False))
		label = Label(group, 0)
		label.text = "Results"
		label.layoutData = topAlign(GridData())
		self.listbox = List(group, SWT.MULTI)
		self.search(self.searchbox.text)
		self.listbox.layoutData = horizontalFill(verticalFill(GridData()))
		group.layoutData = horizontalFill(verticalFill(GridData()))
		
		self.searchbox.addModifyListener(modifyListener(lambda event: self.search(event.widget.text)))
		self.listbox.addSelectionListener(selectListener(lambda event: self.select(event.widget.selectionIndex)))
		
		self.searchbox.addKeyListener(keyPressListener(lambda event: self.listbox.setFocus(), SWT.ARROW_DOWN | SWT.CTRL))
		
		def f(event):
			if event.widget.getSelectionIndex() == 0:
				self.searchbox.setFocus()
		
		self.listbox.addKeyListener(keyPressListener(f, keycode = SWT.ARROW_UP | SWT.CTRL))
		
		def f(event):
			if len(self.items) == 0:
				self.create()
			else: 
				self.listbox.setFocus()
		self.searchbox.addKeyListener(keyPressListener(f, keycode = SWT.CR))
		self.searchbox.addKeyListener(keyPressListener(f, keycode = SWT.LF))
		
		def f(event):
			print "key event:", event, event.keyCode, SWT.LF
			print "\t--- ", event.keyCode == SWT.LF, event.keyCode == SWT.CR
		self.searchbox.addKeyListener(keyPressListener(f))
		
		def f(event):
			if event.widget.getSelectionIndex() == event.widget.getItemCount() - 1:
				for c in self.children:
					c.focus()
		
		self.listbox.addKeyListener(keyPressListener(f, keycode = SWT.ARROW_DOWN | SWT.CTRL))
		
		print "initiating children: ", self.children
		for c in self.children:
			c.build(parent)
		
		for s in self.styles:
			self.apply_style(s)
		
		return self
		
	def select(self, index):
		if index is None:
			text = None
		else:
			text = self.items[index]
		for c in self.children:
			c.selected(text)
	
	def create(self, text = None):
		if text is None:
			text = self.searchbox.text
		print "creating new note:", text
		
		for c in self.children:
			c.selected(text, new = True)
	
	def search(self, text = None):
		if text is None:
			text = self.searchbox.text
		self.items = filter(lambda entry: text.lower() in entry.lower(), self.db.entries)
		self.listbox.items = [i.split("\n")[0] for i in self.items]
		
		# auto-complete search feature
		if len(self.listbox.items) == 1:
			onlyMatch = self.listbox.items[0]
			if self.searchbox.text != onlyMatch and onlyMatch.lower().startswith(self.searchbox.text.lower()):
				oldlen = len(self.searchbox.text)
				self.searchbox.text = onlyMatch
				self.searchbox.setSelection(oldlen, len(onlyMatch))
		
		# select first result
		if self.listbox.selectionCount == 0 and len(self.listbox.items) > 0:
			self.listbox.setSelection(0)
	
	
	def focus(self):
		self.listbox.setFocus()
	
	def apply_style(self, style):
		print "applying style", style
		if 'size' in style:
			self.listbox.setSize(style['size'][0], style['size'][1])
		if 'color' in style:
			c = style['color']
			self.listbox.setBackground(Color(self.listbox.display, c[0], c[1], c[2]))
		pass
	
	

