class Quotation:

 #""""Quotation" class will describe the objects of quotations sent by providers
 #that could be registered (points) or not (no points),and will have all the
 #information needed to score the quotation and classify it by Purchase_Process_ID"""

	def __init__(self,Provider_Code,Purchase_Process,Product_Name,Quantity,Unit_Price,Delivery_Time):
		self.Provider_Code=Provider_Code
		self.Purchase_Process=Purchase_Process
		self.Product_Name=Product_Name
		self.Quantity=Quantity
		self.Unit_Price=Unit_Price
		self.Delivery_Time=Delivery_Time
		#self.Delivery_Location=Delivery_Location
		self.Total_Points=0
		self.Rank=0

	def Show_data(self):
		print("Provider_Code "+str(self.Provider_Code))
		print("Purchase_Process "+str(self.Purchase_Process))
		print("Product_Name "+str(self.Product_Name))
		print("Quantity "+str(self.Quantity))
		print("Unit_Price "+str(self.Unit_Price))
		print("Delivery_Time "+str(self.Delivery_Time))
		#print(self.Delivery_Location)
		print("Total_Points "+str(self.Total_Points))
		print("Rank "+str(self.Rank))
