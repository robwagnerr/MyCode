def sales_tax():

    amount = input("Enter the amount of the purchase: ")
    amount = format(float(amount), '.2f')
    statetax = format(float(amount) * 0.05, '.2f')
    countytax = format(float(amount) * 0.025, '.2f')
    totaltax = format(float(statetax) + float(countytax), '.2f')
    saletotal = format(float(amount) + float(totaltax), '.2f')

    print("Purchase Amount: " + str(amount))
    print("State Tax: " + str(statetax))
    print("County Tax: " + str(countytax))
    print("Total Tax: " + str(totaltax))
    print("Sale Total: " + str(saletotal))


def compound_interest():

    startingprinc = input("Enter the starting principal: ")
    irate = input("Enter the annual interest rate: ")
    irate = float(irate) / 100
    periodicity = input("How many times per year is the interest compounded? ")
    ihorizon = input("For how many years will the account earn interest? ")
    ihorizon = format(float(ihorizon), '.0f')

    fv = format(float(startingprinc) * (1 + float(irate) / float(periodicity)) ** (float(periodicity) * float(ihorizon)), '.2f')

    print("At the end of " + str(ihorizon) + " years you will have $ " + str(fv))


def dollar_game():

    pennies = input("Enter the number of pennies: ")
    pennies = float(pennies) * .01
    nickels = input("Enter the number of nickels: ")
    nickels = float(nickels) * .05
    dimes = input("Enter the number of dimes: ")
    dimes = float(dimes) * .10
    quarters = input("Enter the number of quarters: ")
    quarters = float(quarters) * .25

    totalval = pennies + nickels + dimes + quarters

    if float(totalval) < 1.0:
        print("Sorry, the amount you entered was less than one dollar.")
    elif float(totalval) > 1.0:
        print("Sorry, the amount you entered was more than one dollar.")
    elif float(totalval) == 1.0:
        print("Congratulations!")
        print("The amount you entered was exactly one dollar!")
        print("You win the game!")


def quantity_discount():

    quant = int(input("Enter the number of packages purchased: "))
    price = 99.00
    subtotal = price * float(quant)
    
    if quant >= 0 and quant < 10:
        totaldisc = 0
    elif quant >= 10 and quant < 20:
        totaldisc = .1 * float(subtotal)
    elif quant >= 20 and quant < 50:
        totaldisc = .2 * float(subtotal)
    elif quant >= 50 and quant < 100:
        totaldisc = .3 * float(subtotal)
    elif quant >= 100:
        totaldisc = .4 * float(subtotal)

    totaldisc = format(totaldisc, '.2f')
    totalamount = float(subtotal) - float(totaldisc)
    totalamount = format(totalamount, '.2f')

    print("Discount Amount: $ " + str(totaldisc))
    print("Total Amount: $ " + str(totalamount))


def shipping_charge():

    weight = input("Enter the weight of the package: ")
    weight = float(weight)
    totalcost = 0.00

    if weight >= 0.00 and weight <= 2.00:
        totalcost = 1.50 * float(weight)
        totalcost = format(float(totalcost), '.2f')
        print("Shipping Charge: $ " + str(totalcost))
    elif weight > 2.00 and weight <= 6.00:
        totalcost = 3.00 * float(weight)
        totalcost = format(float(totalcost), '.2f')
        print("Shipping Charge: $ " + str(totalcost))
    elif weight > 6.00 and weight <= 10.00:
        totalcost = 4.00 * float(weight)
        totalcost = format(float(totalcost), '.2f')
        print("Shipping Charge: $ " + str(totalcost))
    elif weight > 10.00:
        totalcost = 4.75 * float(weight)
        totalcost = format(float(totalcost), '.2f')
        print("Shipping Charge: $ " + str(totalcost))


def budget_analysis():
   
    budgeted = float(input("Enter amount budgeted for the month: "))
    budgloop = True
    spent = 0

    while budgloop is True:
        spending = float(input("Enter an amount spent(0 to quit): "))
        spent = spending + spent
        if spending == 0:
            budgloop = False
    
    if spent < budgeted:
        under = budgeted - spent
        under = float(under)
        under = format(under, '.2f')
        budgeted = format(float(budgeted), '.2f')
        spent = format(float(spent), '.2f')
        print("Budgeted: $ " + str(budgeted))
        print("Spent: $ " + str(spent))
        print("You are $ " + str(under) + " under budget. WELL DONE!")
    elif spent == budgeted:
        budgeted = format(float(budgeted), '.2f')
        spent = format(float(spent), '.2f')
        print("Budgeted: $ " + str(budgeted))
        print("Spent: $ " + str(spent))
        print("Spending matches budget. GOOD PLANNING!")
    elif spent > budgeted:
        over = spent - budgeted
        over = float(over)
        over = format(over, '.2f')
        budgeted = format(float(budgeted), '.2f')
        spent = format(float(spent), '.2f')
        print("Budgeted: $ " + str(budgeted))
        print("Spent: $ " + str(spent))
        print("You are $ " + str(over) + " over budget. PLAN BETTER NEXT TIME!")


def average_rainfall():

    yrs = input("Enter the number of years: ")
    yrs = int(yrs)
    mnths = int(yrs) * 12
    yrloop = 0
    mnth = 0
    sumrainfall = 0

    for yrloop in range(1, (yrs + 1)):
        print("For year  " + str(yrloop) + " :")
        for mnth in range(1, 13):
            rainfall_mnth = input("Enter the rainfall amount for the month: ")
            rainfall_mnth = float(rainfall_mnth)
            sumrainfall = rainfall_mnth + sumrainfall

    sumrainfall = format(float(sumrainfall), '.2f')
    avgrainfall = format(float(sumrainfall) / float(mnths), '.2f')

    print("For  " + str(mnths) + " months")
    print("Total rainfall:  " + str(sumrainfall) + " inches")
    print("Average monthly rainfall:  " + str(avgrainfall) + " inches")


def factorial():

    integer = input("Enter a nonnegative integer: ")
    integer = int(integer)
    loopnum = 1
    totalfac = 1

    for loopnum in range(0, integer):
        totalfac = (loopnum + 1) * totalfac
        loopnum += 1

    print("The factoral of " + str(integer) + " is " + str(totalfac))


def morse_code():

    codestring = str(input("Enter the string to be converted to Morse code: "))

    morsecodelist = {'A': '.-',     'B': '-...',   'C': '-.-.', 
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..',
        
            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.' 
            }

    codestring.upper()

    for i in codestring:
        if i != " ":
            print(morsecodelist[i.upper()] + ",", end="")
        elif i == " ":
            print(" ", end="")

    print("")


def main():
    sales_tax()
    compound_interest()
    dollar_game()
    quantity_discount()
    shipping_charge()
    budget_analysis()
    average_rainfall()
    factorial()
    morse_code()

if __name__=="__main__":
    main()





