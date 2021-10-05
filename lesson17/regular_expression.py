# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

import re

mytext = " VAsya 1972, Koly kolay@gmail.com, Pety - Piter(2019)"

"""
\d = Any didgit
\D = Any non didgit
\w = Any Alphabet
\W = Any non Alphabet symbol
\s = brackspace
\S = non brakespace

[0-9]{3}
\w{5} - any word with six alphabet symbols
\w{5}\s
[A-Z][a-z]+
\w

"""

textlookfor = r"@\w+\.\w+"
allresults = re.findall(textlookfor, mytext)

print(allresults)