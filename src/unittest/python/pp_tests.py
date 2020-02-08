from models.purchase_process import Purchase_Process


pp = Purchase_Process(2222,"Monitor",20)
assert pp.Purchase_Process == 2222
assert pp.Product_Name == "Monitor"
assert pp.Quantity_Required == 20

assert pp.Show_data() == "Purchase_Process 2222\nProduct_Name Monitor\nQuantity_Required 20"