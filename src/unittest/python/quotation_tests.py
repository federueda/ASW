from models.quotation import Quotation

qu = Quotation(2222,1001,"Monitor",23,200,7)

# Confirm expected data

assert qu.Provider_Code == 2222
assert qu.Purchase_Process == 1001
assert qu.Product_Name == "Monitor"
assert qu.Quantity == 23
assert qu.Unit_Price == 200
assert qu.Delivery_Time == 7

assert qu.Show_data() == "Provider_Code 2222\nPurchase_Process 1001\nProduct_Name Monitor\nQuantity 23\nUnit_Price 200\nDelivery_Time 7\nTotal_Points 0\nRank 0"