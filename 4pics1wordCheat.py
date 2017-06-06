import itertools
import enchant


d = enchant.Dict("en_US")

b = raw_input("Enter characters without spaces: ")
c = int(raw_input("Enter length of desired word: "))
a = list(b)
for subset in itertools.permutations(a,c):
    y = ''.join(subset)
    if(d.check(y)):
        print y
