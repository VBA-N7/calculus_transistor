class common_transistor(object):
	"""docstring for common_transistor"""
	def __init__(self,Rb1 = None,Rb2 = None,Rc = None,Re = None,Rg = None,Cg = None,Vcc = None,eg = None,Beta = None,Vbe = None):
		super(common_transistor, self).__init__()
		# Resistance de polarisation
		self.Rb1 = Rb1
		self.Rb2 = Rb2
		self.Rc = Rc
		self.Re = Re
		self.Rg = Rg
		# Condensateur de polarisation
		self.Cg = Cg
		# Parametres des sources
		self.Vcc = Vcc
		self.eg = eg
		# Parametres propre au transistor 
		if Beta is not None:
			self.Beta = Beta
		else:
			self.Beta = 300
		if Vbe is not None: 
			self.Vbe = Vbe
		else:
			self.Vbe = 0.6
		self.UT = 26e-3
		self.VA = 130

	def calcul_thevenin(self):
		try:
			self.Rth = R_para(self.Rb1,self.Rb2)
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

def R_para(R1,R2):
	return (R1*R2)/(R1+R2)
	pass

if __name__ == "__main__":
	temp = common_transistor(Rb1 = 47e3,Rb2 = 22e3,Vcc = 12,Re = 2.2e3,Rc = 2.7e3)
	temp.calcul_parametres_dynamiques()

