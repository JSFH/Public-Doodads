Constant_Deep=3

def Paren (thingy, openparen, closeparen):
   if (openparen>0 and closeparen<3):
       Paren(thingy+'(', openparen-1, closeparen+1)
   if (closeparen>0):
       Paren(thingy+')', openparen, closeparen-1)
   if (openparen==0 and closeparen==0):
       print thingy
       

openparen=Constant_Deep
closeparen=0
thingy=''
Paren(thingy, openparen, closeparen)
