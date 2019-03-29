bid = []
buy_nums = []
item_n = []
price = []
desc = []
no_bids = []
bid_cnt = []    
bid_no = []
sell = []
t_fee = []
stop = 0
item_buy = 0
again = 0
number = 0
total_input = 1
no_sold = 0
no_notsold = 0
no_bid = 0

while total_input != 0:
    item_input = int(input("Enter Number of items being input: "))
    if item_input < 3:
        print("INVALID - Input at least 10 items")
        
    else:
        total_input = 0

#task 1
for i in range(0,item_input):
    i_num = input("Enter Item Number:")
    item_n.append(i_num)
    r_price = int(input("Enter Reserve Price:"))
    price.append(r_price)
    bid.append(0)
    descrip = input("Item Description:")
    desc.append(descrip)
    no_bids.append(0)
    t_fee.append(0)
    sell.append('NOT SOLD')
    
    
print("---------------------------------------------------------------------")
print("Item ID   Price   Desc")
for i in range(0,item_input):
    print(item_n[i],"       ", price[i],"     ",desc[i])
print("---------------------------------------------------------------------")

    
#task 2    
while stop != 1:
    if again == 0:
        buy = input("Would you like to bid? (y/n) ")
    else:
        buy = 'y'
    if buy == 'y':
        buyer_num =  int(input("Enter Buyer Number: "))
        buy_nums.append(buyer_num)
        buy_id = input("Enter item ID you wish to buy: ")
        for i in range(0,item_input):
            if buy_id == item_n[i]:
                again_id = buy_id
                print(item_n[i])
                print(price[i])
                print(desc[i])
                print("Highest Bid is:", bid[i])
                buy_bid = int(input("Enter Your Bid value:"))

                if buy_bid > bid[i]:
                    bid[i] = buy_bid
                    print("Bid Successful!")
                    no_bids[i] += 1
                
                else:
                    print("INVALID - Bid is smaller than highest bid")
    
        same_bid = input("Would you like to bid again? (y/n)")
        if same_bid == 'n':
            item_buy = 1
            stop = 1
        else:
            again = 1
    elif buy == 'n':
        stop =  1


print("---------------------------------------------------------------------")
for i in range(0,item_input):
    print("ITEM ID: ", item_n[i], "   Number of bids for this item: ", no_bids[i])
print("---------------------------------------------------------------------")

#task 3
for i in range(0, item_input):
    if bid[i] >= price[i]:
        sell[i] = "SOLD"
        no_sold +=1
        fee = int(bid[i])
        t_fee[i] = fee * 1.1
        print("Total fee for item", item_n[i], ": ",t_fee[i])
    else:
        sell[i] = "NOT SOLD"
        print("Item ID of item below reserve price: ",item_n[i], "    Its bid Bid Number: ",bid[i] )
        no_notsold += 1

    if bid[i] == 0:
        
        print("ItemID with 0 bid: ", item_n[i])
        no_bid += 1
        
        
    

print("---------------------------------------------------------------------")
print("Number of items sold: ",no_sold)
print("Number of items NOT sold: ",no_notsold)
print("Number of items with NO bids: ",no_bid)
'''for lol in range(0,item_input):
    print(sell[lol])'''











