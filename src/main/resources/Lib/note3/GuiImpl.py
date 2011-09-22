
import org.eclipse.swt.widgets.Composite
import org.eclipse.swt.widgets.Display
import org.eclipse.swt.widgets.Label
import org.eclipse.swt.widgets.Shell
import org.eclipse.swt.widgets.Text
import org.eclipse.swt.widgets.List

import org.eclipse.swt.events.ModifyEvent
import org.eclipse.swt.events.ModifyListener
import org.eclipse.swt.events.KeyListener
import org.eclipse.swt.events.SelectionListener
from org.eclipse.swt.events import *
import org.eclipse.swt.graphics.Color
from org.eclipse.swt.graphics import *
import org.eclipse.swt.widgets.Display
from org.eclipse.swt.widgets import *
import org.eclipse.swt.layout.GridLayout
import org.eclipse.swt.layout.GridData
from org.eclipse.swt.layout import *
import org.eclipse.swt.browser.Browser
from org.eclipse.swt.browser import *
import org.eclipse.swt.SWT
from org.eclipse.swt import *
#import org.eclipse.swt.printing.Printer
#from org.eclipse.swt.printing import *
#import org.eclipse.swt.program.Program
#from org.eclipse.swt.program import *
#import org.eclipse.swt.opengl.GLCanvas
#from org.eclipse.swt.opengl import *
#import org.eclipse.swt.custom.Bullet
#from org.eclipse.swt.custom import *
#import org.eclipse.swt.dnd.DND
#from org.eclipse.swt.dnd import *

class GuiImpl(object):
	structure = None
	children = None
	parent = None
	styles = []
	
	def build(self):
		pass
		
	def launch(self):
		pass	
	
	def apply_style(self, style):
		pass
	
def modifyListener(f):
	class MyEventListener(ModifyListener):
		def modifyText(self, event):
			f(event)
	return MyEventListener()

def selectListener(f):
	class MySelectListener(SelectionListener):
		def widgetSelected(self, event):
			f(event)
		widgetDefaultSelected = widgetSelected
	return MySelectListener()

def keyPressListener(f, keycode = None):
	class MyKeyListener(KeyListener):
		def keyPressed(self, event):
			if keycode is None or event.keyCode == keycode:
				f(event)
	return MyKeyListener()
def keyReleaseListener(f, keycode = None):
	class MyKeyListener(KeyListener):
		def keyReleased(self, event):
			if keycode is None or event.keyCode == keycode:
				f(event)
	return MyKeyListener()

def __listener(f):
	class MyListener(Listener):
		def handleEvent(self, event):
			print self, "event: ", event
			f(event)
	return MyListener()


def verticalFill(data):
	data.verticalAlignment = GridData.FILL
	data.grabExcessVerticalSpace = True
	return data
def horizontalFill(data):
	data.horizontalAlignment = GridData.FILL
	data.grabExcessHorizontalSpace = True
	return data
def topAlign(data):
	data.verticalAlignment = SWT.BEGINNING
	return data
	

