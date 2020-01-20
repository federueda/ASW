class Provider:

 #"""Provider class will describe the objects of providers already registered
 #by the company in its system, through a read of a .CSV file. After reading
 #this file, the provider that is not in this list will not be recognized
 #as REGISTERED PROVIDER when scoring the quotations"""

	def __init__(self,Provider_ID,Provider_Name,Provider_Address,Local_Company,Quality_Cert):
		#se le adigna a cada atributo el respectivo valor por medio del paso de parametros
		self.Provider_ID=Provider_ID
		self.Provider_Name=Provider_Name
		self.Provider_Address=Provider_Address
		self.Local_Company=Local_Company
		self.Quality_Cert=Quality_Cert

	#If needed we can change name through a method
	def Change_Name(self,name):
		self.Provider_Name=name

	#If needed in the process, there is a method provided for printing data
	def Show_data(self):
		print("Provider_ID "+str(self.Provider_ID))
		print("Provider_Name "+str(self.Provider_Name))
		print("Provider_Address "+str(self.Provider_Address))
		print("Local_Company "+str(self.Local_Company))
		print("Quality_Cert "+str(self.Quality_Cert))