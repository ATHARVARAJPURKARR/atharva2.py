term=int(input("ENTER NO. OF TERMS IN SERIES"))
n1=0
n2=1
count=0
if term<=0:
    print("ENTER +VE NUMBER OF TERMS")
elif term==1:
    print("FIBONACCI SERIES:",n1)
else:
    print("FIBONACCI SERIES:")
    while count<term:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count=count+1