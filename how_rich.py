#name - Jefferson Adjetey
#date - January 24, 2021
#purpose -  To compute Brutus's current wealth.

def brutus(CURRENT_YEAR):


    BRUTUS_INTEREST = 1.05  # 5 percent compounded interest rate of the initial deposit
    BRUTUS_INITIAL = 1.0
    year = 0       # The year brutus deposited his first amount
    brutus_balance = 1.0  # Brutus's balance


    while year < CURRENT_YEAR:   # loop to calculate balance
        brutus_balance =  brutus_balance * BRUTUS_INTEREST
        year = year + 1



    print("His balance increased from " + str(BRUTUS_INITIAL) + " initially to " + str(brutus_balance) + " in year " + str(CURRENT_YEAR) + ".")

brutus(2020)