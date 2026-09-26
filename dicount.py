price=int(input("Enter the price: "))
q=int(input("Enter the quantity: ")) 
total=price * q
if total>=5000:
    discount_amount=(total *5)/100
    final_amount=total - discount_amount                
    print("Discount amount is:", discount_amount)
else:
    print("No discount")