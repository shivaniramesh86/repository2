def add(a,b):
	if b==0:
		return a
	else:
		return add(a+1,b-1)
			
num1=int(input("ENTER THE FIRST NUMBER: "))
num2=int(input("ENTER THE SECOND NUMBER: "))
print("SUM= ",add(num1,num2))
