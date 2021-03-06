class Provider:

 #Provider class will describe the objects of providers already registered
 #by the company in its system, through a read of a .CSV file. After reading
 #this file, the provider that is not in this list will not be recognized
 # as REGISTERED PROVIDER when scoring the quotations

	def __init__(self,Provider_ID,Provider_Name,Provider_Address,Local_Company,Quality_Cert):

		self.Provider_ID=Provider_ID
		self.Provider_Name=Provider_Name
		self.Provider_Address=Provider_Address
		self.Local_Company=Local_Company
		self.Quality_Cert=Quality_Cert

	# If needed we can change name through a method
	def Change_Name(self,name):
		self.Provider_Name=name

	# If needed in the process, there is a method provided for printing data
	def Show_data(self):
		return (
		"Provider_ID "+str(self.Provider_ID)+
		"\nProvider_Name "+str(self.Provider_Name)+
		"\nProvider_Address "+str(self.Provider_Address)+
		"\nLocal_Company "+str(self.Local_Company)+
		"\nQuality_Cert "+str(self.Quality_Cert)
			)
