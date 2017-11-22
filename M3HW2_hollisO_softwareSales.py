#CTI-110
#M3HW2 - Software Sales
#Oliver Hollis
#11-09-2017

# User to enter the number of packages purchased.
#
# Packages retail for $99.00
#
# Discounts are given according to how are bought.
# quanity 10-19          discount  20%
# quanity 20-49          discount  30%
# quanity 30-99          discount  40%
# quanity 100-or more    discount  50%
#
# Program should display the amount of the discount 
# and the total purchase cost with the discount applied

def main():
    # ask customer to input how many packages they are buying

    packageAmount = int(input("How many packages do you want to buy?"))

    # Caculate the discount
    
    if packageAmount < 10:
        print ('No discount.')
        discount=1.0
    elif packageAmount < 20:
        print ('Your discount is 20%.')
        discount=0.8
    elif packageAmount < 50:
        print ('Your discount is 30%.')
        discount=0.7
    elif packageAmount < 100:
        print ('Your discount is 40%.')
        discount=0.6
    else:
        print ('Your discount is 50%.')
        discount=0.5

    # Show total price with dicount

    total_amount = packageAmount * discount * 99.00

    # Calculate the total price before the discount

    full_price = packageAmount * 99.00
    print ("The amount of your discount is $"),format( full_price - total_amount,".2f")
    print ("Your total purchase price is $"),format( total_amount,".2f")
   

main()
 
