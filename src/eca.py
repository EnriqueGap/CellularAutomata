from random import randint
# CellularAutomata 1D

class ECA(object):
	def __init__(self, band_length:int, max_iters:int):
		self.band_length = band_length
		self.max_iters = max_iters
		self.rule_err = False
		self.band_err = False
		self.band = []
		self.rule = []
		self.matrix = []
		
	def setRule(self, rule:int) -> list[int]:
		if (rule>2**8 - 1)|(rule<0):
			binary_rule = "0"*8
			self.rule_err = True
		else:
			binary_rule = bin(rule)[2:]
			binary_rule = "0"*(8-len(binary_rule)) + binary_rule
			self.rule = [int(c) for c in binary_rule]
		return [int(c) for c in binary_rule]

	def setBand(self, band_init:int = None, random_init=True) -> list[int]:
		self.band = []
		if band_init:
			random_init=False
		if random_init:
			band = randint(0,2**self.band_length - 1)
		elif (band_init >2**self.band_length - 1)|(band_init<0):
			band = 0
			self.band_err = True
		else:
			band = band_init
	
		band = bin(band)[2:]
		band = "0"*(self.band_length - len(band)) + band
		self.band = [int(c) for c in band]
		return [int(c) for c in band]

	def iterateBand(self) -> list[int]:
		aux_band = [0]*self.band_length
		for i in range(1, self.band_length-1):
			if self.band[i-1] == 1:
				if self.band[i] == 1:
					if self.band[i+1] == 1:
						aux_band[i] = self.rule[0]
					elif self.band[i+1]==0:
						aux_band[i] = self.rule[1]
				elif self.band[i] == 0:
					if self.band[i+1] == 1:
						aux_band[i] = self.rule[2]
					elif self.band[i+1]==0:
						aux_band[i] = self.rule[3]
			elif self.band[i-1] == 0:
				if self.band[i] == 1:
					if self.band[i+1] == 1:
						aux_band[i] = self.rule[4]
					elif self.band[i+1] == 0:
						aux_band[i] = self.rule[5]
				elif self.band[i] == 0:
					if self.band[i+1] == 1:
						aux_band[i] = self.rule[6]
					elif self.band[i+1] == 0:
						aux_band[i] = self.rule[7]
		self.band = aux_band
		return aux_band

	def evolveBand(self) -> None:
		self.matrix = []
		self.matrix.append(self.band)
		for i in range(0,self.max_iters):
			self.iterateBand()
			self.matrix.append(self.band)
