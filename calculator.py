def calculate(num1,num2,character):
		
		if character not in "+-*/":
			return "only +-/*"

		if character == '+':
				return (str(num1)+" "+character+str(num2)+"="+str(num1+num2))
		elif character == '-':
			
				return (str(num1)+" "+character+str(num2)+"="+str(num1-num2))
		elif character == '*':
			
				return (str(num1)+" "+character+str(num2)+"="+str(num1*num2))
		elif character == '/':
			
				return (str(num1)+" "+character+str(num2)+"="+str(num1/num2))


while True:	
	num1=int(input("please enter first number: "))
	num2=int(input("please enter second number:"))
	character=input("choose between +,-,*,/")

			
	print(calculate(num1,num2,character))			

	
			
			
		
		
"""def minus():
		if character=="-":
	def multiply():
		if character=="*":"""
