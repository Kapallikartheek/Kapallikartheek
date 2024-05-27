from datetime import datetime

name=input("Enter your name:")
#list of items
lists='''
rice         Rs 30/kg
sugar        Rs 25/kg
Salt         RS 10/kg
oil          Rs 100/ltr
panner       RS 100/kg
horlicks     RS 200/kg
maagi        Rs 30/100g
corn powder  Rs 90/kg
coffe powder Rs 60/500g
kaju         Rs 100/200g
colgate      Rs 100/250g
'''
#declaration
price=0
pricelist=[]
toatlprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates per items
items={'rice':30,
       'sugar':25,
       'salt':10,
       'oil':100,
       'panner':100,
       'horlicks':200,
       'maggi':30,
       'corn powder':90,
       'coffe powder':60,
       'kaju':100,
       'colgate':100}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or press 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("plese enter your items:")
        quantity=int(input("plese enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            toatlprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(toatlprice*5)/100
            finalprice=gst+toatlprice
        else:
            print("sorry this items not avilable....")
    else:
        print("you enter wrong number plese check....")
    inp=input("you want print bill yes or no:")   
    if  inp=='yes':
        pass
        if finalprice!=0:
            print(27*"=","kartheek supermarket",26*"=")
            print(33*" ","Nellore")
            print("Name:",name,24*" ","Date:",datetime.now())
            print((75*"-"))
            print("Sno", 11*" ", 'items', 14*" ", 'quantity', 10*" ", 'price')

            # Print each item's details in a formatted manner
            for i in range(len(plist)):
                print(f"{i:<4}", 10*" ", f"{ilist[i]:<20}", f"{qlist[i]:<8}", 10*" ", f"{plist[i]:<6}")

                    
                
            print(75*"-")
            print(50*" ",'totalprice:','Rs',toatlprice) 
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-") 
            print(50*" ",'finalprice:','Rs',finalprice)   
            print(75*"-") 
            print(13*" ","****THANKS FOR VISITING, HAVE A GOOD DAY****")
            print(75*"-")  







                
                










            




















