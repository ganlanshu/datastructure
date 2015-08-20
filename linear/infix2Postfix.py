#coding=utf-8
from stack import Stack

def infixToPostfix(infixExpress):
	opstack=Stack() # to store operators,lower operators will be poped at first
	output=[]
	pre={'(':1,'+':2,'-':2,'^':3,'*':3,'/':3} # use int to hold precedence of operators,( holds the lowest
	if not isinstance(infixExpress,str):
		print ('Warning! expression should be str')
	length=len(infixExpress)
	index=0
	while index < length:
		character = infixExpress[index]
		if character.isdigit():
			output.append(character)
		elif character == '(':
			opstack.push(character)
		elif character in '+-*/^':
			while opstack.size() > 0 and pre[opstack.peek()] >= pre[character]: 
				output.append(opstack.pop())
			opstack.push(character) 
		elif character == ')':
			while opstack.peek() != '(':
				output.append(opstack.pop())	
			opstack.pop()
		index += 1
	
	while opstack.size() > 0: #字符串遍历完毕，若opstack中还有operator，就放入output
		output.append(opstack.pop()) 	
	
	return output

if __name__ == '__main__':
	print infixToPostfix('(1+5)*9/2')
	print infixToPostfix('(1+5)*(9/2)')
	print infixToPostfix('(5*(4+8)-9)/3')
	print infixToPostfix('(1+4)^4/6')
