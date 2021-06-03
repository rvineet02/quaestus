import pandas as pd 

# Import functions from testing-libs.py and talib_functions.py to compare and test 
import talib_functions
import testing_libs

# Compares RSI from TechRSI and RSI to check values 
def compareRSI():

    mine = testing_libs.RSI(useData(getData("MSFT")))
    mine.sort_index(inplace=True)
    tlb = talib_functions.TalibRSI(useData(getData("MSFT")))
    # tlb starts one extra day in 1986 so removing it
    tlb = tlb[1:]
    tlb.sort_index(inplace=True)

    # Making the two Series into one df to see values side-by-side    
    df = pd.concat([mine, tlb], axis=1)
    print(df.tail())

    # Prints true or false value by value keeping the index 
    # print(mine != tlb.values)

