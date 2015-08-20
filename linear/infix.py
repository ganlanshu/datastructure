#coding=utf-8
from stack import Stack

    
#postfix evaluation,如 AB*CD*+ 换成算术表达式是 A*B + C*D
# AB+CD+*  = (A+B)*(C+D),算法是从左到右遍历输入值，如果是operands就存入stack，until遇到operator，对stack顶部的2个元素进行operator操作，值存入stack top，until stack只有一个元素，就是表达式的值

def postfixEval(postfixString):
    """
    AB+CD+*  = (A+B)*(C+D),算法是从左到右遍历输入值，如果是operands就存入stack，until遇到operator，对stack顶部的2个元素进行operator操作，值存入stack top，until stack只有一个元素，就是表达式的值
    """
    tokens=postfixString.split()
    operandStack=Stack()
    for token in tokens: 
        if token in '0123456789':
        #if isinstance(int(token),int): 
            operandStack.push(token)
        
        elif token in '+-*/' and operandStack.size() >= 2:
            op2 = int(operandStack.pop())
            op1 = int(operandStack.pop())
            #print op2,op1
            operandStack.push(operation(token,op1,op2))    
        else:
            print('Warning! at least two elements before operator + - * /')    

    return operandStack.pop()#最后剩下的一个元素为表达式的计算结果


def operation(operator,op1,op2):
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    return op1/op2


if __name__ == '__main__':
    print postfixEval('8 9 * 2 + 7 /')
