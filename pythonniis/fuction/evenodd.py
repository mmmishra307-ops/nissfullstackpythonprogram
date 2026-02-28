def check():
	print("enter a number")
	n=int(input())
	if n%2==0:
		return True
	else:
 	    return False
 	
if check():
  print("even number")
else:
    print("odd number")

