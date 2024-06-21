#name - Jefferson Adjetey
#date - January 24, 2021
#purpose -  To compute the first year in which Brutus’s balance exceeds Portia’s balance.



BRUTUS_INTEREST = 1.05  # 5 percent compounded interest rate of the initial deposit
PORTIA_INTEREST = 1.04  # 4 percent compounded interest rate of the initial deposit
BRUTUS_INITIAL = 1.0
PORTIA_INITIAL = 100000.0
year = 0        # The year first amount was deposited
brutus_balance = 1.0  # brutus balance
portia_balance = 100000  # portia balance›‹



#loop that computes when Brutus's balance exceeds portia's balance
while brutus_balance < portia_balance:
    brutus_balance = brutus_balance * BRUTUS_INTEREST
    portia_balance = portia_balance * PORTIA_INTEREST
    year = year + 1

print("In " + str(year) + ", Brutus's balance of " + str(brutus_balance) + " will exceed Portia's balance of " + str(portia_balance) + ".")