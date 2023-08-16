# All the pieces you need for this exercise are in here. You might not
# use them all, that's okay. Don't worry about getting it on the first
# try just think about something that works for you and try it.

some_string_variable="abcd"

# Functions and Usefull tests
some_string_variable[2] # -> "c" 
some_string_variable.index("c") # -> 2
some_string_variable.islower() # -> True
some_string_variable.isupper() # -> False
some_string_variable.upper() # -> "ABCD"
"ABCD".lower() # -> "abcd" 
some_string_variable.isalpha() # -> True
"a" in ["c", "d", "a"] # -> True 
"a" in "abc" # -> True 

# Alphabet
from string import ascii_uppercase, ascii_lowercase
lower_string = "abcdefghijklmnopqrstuvwxyz" 
upper_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

# index[zero]:  0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25  
# ----------------------------------------------------------------------------------------------------------------------------------------------
# index[ascii]:97   98   99   100  101  102  103  104  105  106  107  108  109  110  111  112  113  114  115  116  117  118  119  120  121  122 
lower_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# ----------------------------------------------------------------------------------------------------------------------------------------------
# index[ascii]:65   66   67   68   69   70   71   72   73   74   75   76   77   78   79   80   81   82   83   84   85   86   87   88   89   90
upper_array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Loops
start = 0
stop = len(some_string_variable) # -> 4
step = 1
for i in range(start, stop, step):
    print(some_string_variable[i]) # -> "a", "b", "c", "d"

for character in lower_string:
    print(character) # -> "a", "b", "c",..., "x", "y", "z"

for character in ascii_lowercase:
    print(character) # -> "a", "b", "c",..., "x", "y", "z"

for character in lower_array:
    print(character) # -> "a", "b", "c",..., "x", "y", "z"

# Math
15 % 10 # -> 5 
15 - 10 * (15 // 10) # -> 5
ord("a") # -> 97 
chr(65) # -> "A"
