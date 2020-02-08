class Quotation:

 # Quotation class will describe the objects of quotations sent by providers
 # that could be registered (points) or not (no points),and will have all the
 # information needed to score the quotation and classify it by Purchase_Process_ID

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
		return (
		"Provider_Code "+str(self.Provider_Code)+
		"\nPurchase_Process "+str(self.Purchase_Process)+
		"\nProduct_Name "+str(self.Product_Name)+
		"\nQuantity "+str(self.Quantity)+
		"\nUnit_Price "+str(self.Unit_Price)+
		"\nDelivery_Time "+str(self.Delivery_Time)+
		#print(self.Delivery_Location)
		"\nTotal_Points "+str(self.Total_Points)+
		"\nRank "+str(self.Rank)
		)
