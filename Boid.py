class Boid(object):
	"""docstring for Boid"""
	def __init__(self, position, orientation, velocity):
		super(Boid, self).__init__()
		self.position = position
		self.orientation = orientation
		self.velocity = velocity
	def setPosition(self,newPosition):
		self.position = newPosition
	def setOrientation(self,newOrientation):
		self.orientation = newOrientation
	def setVelocity(self,newVelocity):
		self.velocity = newVelocity
	def getPosition(self):
		return self.position
	def getOrientation(self):
		return self.orientation
	def getVelocity(self):
		return self.velocity

pos = ['x','y','z']
ori = ['x','y','z']
vel = 0.5
b = Boid(pos,ori,vel)
print b