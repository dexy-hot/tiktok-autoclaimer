import re
'''
Console Color Class
By Dexy.
Contact Discord: dexy#7742
'''
class Color():
	def __init__(self,text, b=False, bg=False, u=False):
		self.text = text
		self.start = "\33["
		self.reset = "\033[0m"
		self.u = u
		self.effect = "0;3"
		if b:
			self.effect = "1;3"
		if u:
			self.effect = "4;3"
		if bg:
			self.effect = "4"
		self.colors = {
		"green":"2",
		"red":"1",
		"yellow":"3",
		"blue":"4",
		"purple":"5",
		"cyan":"6",
		"white":"7",
		}
		self.green = self.colorize("2")
		self.black = self.colorize("0")
		self.red = self.colorize("1")
		self.yellow = self.colorize("3")
		self.blue = self.colorize("4")
		self.purple = self.colorize("5")
		self.cyan = self.colorize("6")
		self.white = self.colorize("7")
	def clear(self):
		return re.sub("\\033\[(.*?)m","",self.text)
		
	def alert(self):
		return Color(Color(self.text,bg=1).red,u=self.u).white		
	def info(self):
		return Color(Color(self.text,bg=1).cyan,u=self.u).white
	def head(self):
		return Color(Color(self.text,bg=1).purple,u=self.u).white
	def success(self):
		return Color(Color(self.text,bg=1).green,u=self.u).black
	def colorize(self,color,text = False):
		if not text:
			text = self.text
		finish = self.start + self.effect + color + "m" + text + self.reset

		return finish