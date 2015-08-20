#coding=utf-8

from stack import Stack

#使用devide by 2 方法，把10进制数字转化为2进制的

def devideBy2(decimal):
	#不断用2整除decimal，until 结果为0,并保存每一次的余数，最后把remainder倒置过来就是2进制数,思路来自course，代码自己写的
	if not isinstance(decimal,int):
		print ('Warning! int and decimal please') 
	s = Stack()
	while decimal > 0:
		decimal,rem = divmod(decimal,2)	
		s.push(rem)

	
	bins=''	
	while not s.is_empty():
		bins = bins + str(s.pop())
	
	return bins

def divideBy2(decNumber):
	#来自online course
	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % 2
		remstack.push(rem)
		decNumber = decNumber // 2

	binString = ""
	while not remstack.is_empty():
		binString = binString + str(remstack.pop())

	return binString


#除了2进制，可以转换成任意进制，从2-16,方法同上，需要注意大于10时，remainder从10到15,需要用ABCDEF代替，用list的index很容易实现
def BaseConverter(decimal,base):
	"""
	十进制转化成任意进制(只限于2-16)
	"""	
	if not 2<=base<=16:
		print('Warning! base between 2 and 16')
		return
	digits = '0123456789ABCDEF'
	s=Stack()
	while decimal > 0 :
		decimal,rem = divmod(decimal,base)
		s.push(rem)

	newString=''	
	while not s.is_empty():
		newString = newString + digits[s.pop()]
	
	return newString



if __name__ == '__main__':

	print devideBy2(8)
	print devideBy2(78)
	print divideBy2(100)	
	print BaseConverter(98,16)	
	print BaseConverter(25,8)	
	print BaseConverter(256,16)	
	print BaseConverter(52,26)	
