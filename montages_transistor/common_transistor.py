class CommonTransistor(object):
	"""docstring for common_transistor"""
	def __init__(self, rb1=None, rb2=None, rc=None, re=None, rg=None, cg=None, vcc=None, eg=None, beta=None, vbe=None):
		super(CommonTransistor, self).__init__()
		# Resistance de polarisation
		self.Rb1 = rb1
		self.Rb2 = rb2
		self.Rc = rc
		self.Re = re
		self.Rg = rg
		# Condensateur de polarisation
		self.Cg = cg
		# Parametres des sources
		self.Vcc = vcc
		self.eg = eg
		# Parametres propre au transistor
		if beta is not None:
			self.Beta = beta
		else:
			self.Beta = 300
		if vbe is not None:
			self.Vbe = vbe
		else:
			self.Vbe = 0.6
		self.UT = 26e-3
		self.VA = 130

	def calcul_thevenin(self):
		try:
			self.Rth = (self.Rb2*self.Rb1)/(self.Rb1+self.Rb2)
			self.Vth = (self.Rb2/(self.Rb1+self.Rb2))*self.Vcc
			print("Valeurs de thevenin :")
			print("Vth = {}V\nRth = {} Ohms".format(round(self.Vth,2),round(self.Rth,2)))
		except Exception:
			print("Missing resistance value or Vcc value")
		pass

	def calcul_polarisation(self):
		try:
			self.calcul_thevenin()
			self.Icq = (self.Vth - self.Vbe)/((self.Rth / self.Beta)+self.Re)
			self.Vceq = self.Vcc - (self.Rc + self.Re)*self.Icq
			print("Parametres de polarisation statique")
			print("Icq = {:.2e}A\nVceq = {:.2e}V".format(self.Icq,self.Vceq))			
		except Exception:
			print("One or more thevenin value missing")
		pass

	def calcul_parametres_dynamiques(self):
		try:
			self.calcul_polarisation()
			self.gm = (self.Icq*1e3) / self.UT
			self.rb = self.Beta * (self.UT / self.Icq)
			self.r0 = self.VA / self.Icq
			print("Parametres de polarisation dynamique :")
			print("Gm = {:.2e} mA/V\nrb = {:.2e} Ohms\nr0 = {:.2e} Ohms".format(self.gm,self.rb,self.r0))
		except Exception:
			print("One or more static parameters missing")			

		pass

if __name__ == "__main__":
	temp = CommonTransistor(Rb1=47e3, Rb2=22e3, Vcc=12, Re=2.2e3, Rc=2.7e3)
	temp.calcul_parametres_dynamiques()
