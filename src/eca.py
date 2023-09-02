from random import randint
# CellularAutomata 1D

class ECA(object):
	def __init__(self, band_length:int, max_iters:int):
		"""
		Create an elemental cellular automaton

		Args::
		band_length :: Determines size of band (world of eca)
		max_iters :: Determines the number of iterations (evolution) of the band
		"""
		self.band_length = band_length
		self.max_iters = max_iters
		self.rule_err = False
		self.band_err = False
		self.band = []
		self.rule = []
		self.matrix = []
		
	def setRule(self, rule:int) -> list[int]:
		"""
		setRule(rule:int) -> list[int]

		Compute the rule to follow by ECA [0,255]
		The ECA has 2 neighbors and two states {0,1}, hence we have 2**8 valid rules

		Args
		rule Decimal expresion of the rule

		Returns
		rule List of integers with length 8. This list has the rule transformed to binary representation
		"""
		if (rule>2**8 - 1)|(rule<0): # Check if is a valid rule [0,255]
			binary_rule = "0"*8  # If not, set the rule 0 by default
			self.rule_err = True
		else:
			binary_rule = bin(rule)[2:] ##Change the number to int to binary
			binary_rule = "0"*(8-len(binary_rule)) + binary_rule #Complete the string to length 8 if neccesary add 0's
			self.rule = [int(c) for c in binary_rule] #Transform the string to list of ints
		return [int(c) for c in binary_rule]

	def setBand(self, band_init:int = None, random_init=True) -> list[int]:
		"""
		setBand(band_init:int = None, random_init=True) -> list[int]

		Initializes the band
		If a number is passed, convert to binary and use it as initialization
		Else use a random number, convert to binary and use it as initialization

		Args
		band_init: Optional, decimal number used to initialize the band
		random_init: Default True, get a random number and use it to initialize the band

		Returns
		List of integers with length of the band. This list has the decimal number passed or random transformed to binary representation
		"""
		self.band = []
		if band_init:	# If a number has passed, turn off the random initalization
			random_init=False
		if random_init: # If none has passed, get a random number between 0 and (2**length of band -1)
			band = randint(0,2**self.band_length - 1)
		elif (band_init >2**self.band_length - 1)|(band_init<0): # Validate if the number passed is in the interval [0,2**length_band -1]
			band = 0	#Else, initialize with 0 by default
			self.band_err = True
		else:
			band = band_init #If it is a valid number, we use it for initialize the band
	
		band = bin(band)[2:] #Convert decimal to binary
		band = "0"*(self.band_length - len(band)) + band #Complete with 0's up to length of the band if neccesary
		self.band = [int(c) for c in band] #Convert the string to list of int's
		return [int(c) for c in band]

	def iterateBand(self) -> list[int]:
		"""
		iterateBand() -> list[int]

		Given an initialization and a rule to follow, evolve the band to their next state

		Returns
		List of integers with length of the band. This list is the next iteration of the current state of the band in the eca
		"""
		aux_band = [0]*self.band_length #Create and auxiliar band to evolve the state of the band
		for i in range(0, self.band_length): #Iterate over the band and check the states {0,1}
			# We work with a periodic band. The end of the band joins with the beggining
			if i-1<0:
				prev = self.band_length-1
			else:
				prev = i-1
			if i+1>(self.band_length-1):
				next = 0
			else:
				next = i+1
			# Now check the status of the current cell and its neighbors and according to the rule passed, update the auxiliar band
			if self.band[prev] == 1:
				if self.band[i] == 1:
					if self.band[next] == 1:
						aux_band[i] = self.rule[0]
					elif self.band[next]==0:
						aux_band[i] = self.rule[1]
				elif self.band[i] == 0:
					if self.band[next] == 1:
						aux_band[i] = self.rule[2]
					elif self.band[next]==0:
						aux_band[i] = self.rule[3]
			elif self.band[prev] == 0:
				if self.band[i] == 1:
					if self.band[next] == 1:
						aux_band[i] = self.rule[4]
					elif self.band[next] == 0:
						aux_band[i] = self.rule[5]
				elif self.band[i] == 0:
					if self.band[next] == 1:
						aux_band[i] = self.rule[6]
					elif self.band[next] == 0:
						aux_band[i] = self.rule[7]
		self.band = aux_band
		return aux_band

	def evolveBand(self) -> None:
		"""
		evolveBand(self) -> None

		Call iterateBand() until reach max_iters passed and save the states in a matrix
		"""
		self.matrix = [] # Matrix to keep the bands
		self.matrix.append(self.band) # Keep the initialization of the band
		for i in range(0,self.max_iters):
			self.iterateBand() # Evolve the ECA
			self.matrix.append(self.band) # Keep the new state of the band