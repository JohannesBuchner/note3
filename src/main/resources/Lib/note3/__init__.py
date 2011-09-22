

class Node(object):

	def __init__(self, properties = {}, children = []):
		self.parent_node = None
		self.properties = {}
		#print "creating Node:"
		#print "\tname", properties['name']
		self.children = []
		for c in children:
			#print "\tchild:",c 
			self.children.append(c)
			c.set_parent(self)
		#print "children:", self.children
		for p in properties:
			self.properties[p] = properties[p]
	
	def set_parent(self, parent_node):
		self.parent_node = parent_node
		
	def __str__(self):
		return "Node(properties = " + str(self.properties) + ",\n" + \
			"\tchildren = " + str(self.children) + ")"
	
	__repr__ = __str__


def createGui(structure, bindings, style):
	"""
		Builds the GUI correctly,
		applies the bindings -- setting the implementations;
		finally, applies the style.
	"""
	# create substructure
	children = []
	for c in structure.children:
		children.append(createGui(c, bindings, style))
	# now, create this node.
	name = structure.properties['name']
	#actions = structure.properties['actions']
	print "instantiating %s for %s." % (str(bindings[name]), name) 
	impl = bindings[name]()
	impl.structure = structure
	impl.children = children
	if 'global' in style:
		impl.styles.append(style['global'])
	if name in style:
		impl.styles.append(style[name])
	for c in children:
		c.parent = impl
	return impl


def autobind(bindings, key, vars):
	if not bindings.has_key(key):
		 bindings[key] = {}
	val = '%sImpl' % key
	#print "looking for %s in " % val, vars
	if val in vars:
		print "Autobinding %s to %s" % (key, str(val))
		bindings[key] = vars[val]

def find(struct, vars, bindings = {}):
	print "looking at node: ", struct 
	autobind(bindings, struct.properties['name'], vars)
	print "looking at children: ", struct.children
	for c in struct.children:
		find(c, vars, bindings)
	return bindings

from NotesDB import *

model = NotesDB("notes.db")

# what?
struct = Node(properties={
		'name':'NotesWindow',
	}, children = [
		Node(properties={
			'name':'NotesOverview',
			'actions':['selectChild'],
			'model': model,
		}, children = [
			Node(properties = {
				'name':'NoteView',
				'actions':['edit'],
				'model': model,
			})
		])
	]
)

#struct.children[0].children = []

print "gui structure", struct

#from com.jakeapp.note3 import *

from NoteEditImpl import *
from NotesOverviewImpl import *
from NotesWindowImpl import *

bindings = find(struct, globals(), {})

print "Autobind: ", bindings

# how does it work?
bindings['NotesOverview'] = NotesOverviewImpl
bindings['NoteView'] = NoteEditImpl

# how does it look?
style = {
	'global':{
		'fontsize':11,
	},
 	'NotesOverview':{'listBox.lines':5,
		'size': (200,200),
		'color': (255,0,0)
	},
	'NoteView': {'textBox.lines':10,
		'color': (0,255,0)
	},
	'NoteWindow': {
	}
}
	
def main(args):
	createGui(struct, bindings, style).build().launch()

