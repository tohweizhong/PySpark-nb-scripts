
# genrand.py
# random data generator

# based on column names and number of rows, return a dummy dataframe
# data generated can be either strings of integers
# strings will be 6 characters long
# integers will be from 0 to 5 inclusive

# input:
# @ column names     | list of strings
# @ id column        | integer (0-based)
# @ stringcols       | list of integers (0-based)
# @ intcols          | list of integers (0-based)
# @ number of rows   | integer

import pandas as pd
import string
import random

def genrand(colnames, idcol, stringcols, intcols, nrows):
        
        # check indices
        conc = stringcols + intcols
        conc.sort()
        if set(conc) != set(range(0, len(colnames))):
                return None
        
        # empty dataframe
        df = pd.DataFrame(np.nan, index = [i for i in range(0, nrows)], columns = colnames)

        # id column
        id = ["ID_" + str(i) for i in range(0, nrows)]
        df.ix[:,idcol] = id

        # function to generate random strings
        def stringgen(size = 6, chars = string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size))
        
        # fill the other columns
        for i in range(0, len(colnames)):
        
                if i == idcol:
                        next
                elif i in stringcols:
                        randstrings = [stringgen() for j in range(0, nrows)]
                        df.ix[:,i] = randstrings
                elif i in intcols:
                        randnums = [random.randint(0, 6) for j in range(0, nrows)]
                        df.ix[:,i] = randnums
                 
        return df                
        
## Example
#colnames = ['timestamp', 'imsi', 'msisdn', 'cellid', 'eventtype', 'lat', 'lng', 'imei']
#idcol = 1
#stringcols = [0, 1, 2, 3, 4, 7]
#intcols = [5, 6]
#nrows = 1000
#df = genrand(colnames, idcol, stringcols, intcols, nrows)

