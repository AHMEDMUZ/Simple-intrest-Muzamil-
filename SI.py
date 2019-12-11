# Calcution of SI

#input
p=float(input ("what is the principal amount ?"))
R=float(input("what is the rate of intrest?"))
t=float(input("what is the tenure ?"))
r=(R/100)
#x=(1+(rd))**n

        
#processing
#emi=p*rd*(x/(x-1))
amt = p*(1+(r*t))



#output
print("the total amount to be paid is " ,amt)
