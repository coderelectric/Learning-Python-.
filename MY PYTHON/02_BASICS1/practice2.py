# to find the largest number in three numbers 

a = int(input(" ENETER THE FIRST NUMBER :    "))
b = int(input(" ENETER THE SECOND NUMBER :    "))
c = int(input(" ENETER THE THIRD NUMBER :    "))

if a<b and c<b :
    print(b," is the largest number among" )

elif b<a and c<a:
    print(a," is the largest number among")

else  :
    print(c," is the largest number among")

t=  max(a,b,c)   #shortcut
print(t)