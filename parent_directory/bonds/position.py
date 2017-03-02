class Position:
	def_init_(self,notional,bond):
		self.notional = notional
		self.bond = bond
		
	def buy(self,notional):
		self.notional += notional
		
	def sell(self, notional):
		self.notional -= notional
