# Button.py
# Written by: Shasta Ramachandran
# Date: 10/13/15
# This is the correct button class, loaded from the book. I have made a provision for color

from graphics import *
class Button:
	"""A button is a labeled rectangle in a window.
	It is activated or deactivated with the activate()
	and deactivate() methods. The clicked(p) method
	returns true if the button is active and p is inside it."""
	def __init__ (self, win, center, width, height, label, color):
		""" Creates a rectangular button, eg:
		qb = Button(myWin, centerPoint, width, height, ’Quit’, "purple") """
		w,h = width/2.0, height/2.0
		x,y = center.getX(), center.getY()
		self.color = color
		self.xmax, self.xmin = x+w, x-w
		self.ymax, self.ymin = y+h, y-h
		p1 = Point(self.xmin, self.ymin)
		p2 = Point(self.xmax, self.ymax)
		self.rect = Rectangle(p1,p2)
		self.rect.setFill("linen")
		self.rect.draw(win)
		self.label = Text(center, label)
		self.label.draw(win)
		self.deactivate()
	def clicked(self, p):
		"Returns true if button active and p is inside"
		return (self.active and
				self.xmin <= p.getX() <= self.xmax and
				self.ymin <= p.getY() <= self.ymax)
	def getLabel(self):
		"Returns the label string of this button."
		return self.label.getText()
	def activate(self):
		"Sets this button to ’active’."
		self.rect.setFill(self.color)
		self.label.setFill("black")
		self.rect.setWidth(2)
		self.active = True
	def deactivate(self):
		"Sets this button to ’inactive’."
		self.rect.setFill("linen")
		self.label.setFill("linen")
		self.rect.setWidth(1)
		self.active = False
	def use(self, p):
		"Clicks and deactivates this button."
		retval = self.clicked(p)
		if(self.clicked(p)):
			self.deactivate()
		return retval
	def setLabel(self, message):
		"""Sets the label to message."""
		self.label.setText(message)