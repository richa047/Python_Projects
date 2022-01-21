
#Random password generator
import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p =  "".join(random.sample(s,passlen ))
print (p)


#status:working
#ref:https://towardsdatascience.com/10-python-mini-projects-that-everyone-should-build-with-code-769c6f1af0c4