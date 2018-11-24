class Pop:
	def __init__(self, position, value):
		self.position = position
		self.value = value
	
	def __eq__(self, o: object) -> bool:
		if isinstance(o, Pop):
			if o.position[0] == self.position[0] and o.position[1] == self.position[1] and o.value == self.value:
				return True
		return False
