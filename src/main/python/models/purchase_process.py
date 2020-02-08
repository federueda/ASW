class Purchase_Process:

 # Purchase_Process class will describe the objects of items needed to buy for
 # the company (purchase process), that will be read from a .csv file with
 # information as ProcessID, ProdName, Qty, DelTime, Loc.

	def __init__(self,Purchase_Process,Product_Name,Quantity_Required):
		self.Purchase_Process=Purchase_Process
		self.Product_Name=Product_Name
		self.Quantity_Required=Quantity_Required
		#self.Delivery_Time_Required
		#self.Location_Required

	def Show_data(self):
		return (
		"Purchase_Process "+str(self.Purchase_Process)+
		"\nProduct_Name "+str(self.Product_Name)+
		"\nQuantity_Required "+str(self.Quantity_Required)
		)
