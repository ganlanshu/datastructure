#encoding=utf-8

from stack import Stack

def parenthe_check(symbol_string):
    """
    验证输入的string中括号是否平衡，即'('和')'是否成对出现,借助stack来实现比较简单
    """
    if not isinstance(symbol_string,str):
        print 'Warning! param should be string'
    s=Stack()
    index=0
    length=len(symbol_string)
    while index < length:
        symbol=symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            if s.size() > 0:
                s.pop()
            else:
                print '")" can not before "(", not balanced'
                return False
        index += 1

    if s.size() == 0:
        return True
    else:
        return False


def parChecker(symbolString):
    """
    这是http://interactivepython.org/courselib/static/pythonds/BasicDS/SimpleBalancedParentheses.html给出的方案,只判定'('和')'
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty(): #'('出现之前不能有别的字符，否则就是不平衡，中断循环
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def parCheckerGeneral(symbolString):
    """
    适用范围更广，[,{,(都可以，自己写的 
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '[{(':
            s.push(symbol)
        else:
            if s.is_empty(): #左括号出现之前不能有右括号，否则就是不平衡，中断循环
                balanced = False
            else:
                if type_match(s.peek(),symbol): #symbol 和stack的top是同一种括号    
                    s.pop()
                else:
                    balanced = False #如这样的就不平衡 { [](})
        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False

def type_match(left,right):
    """
    判断括号是否为同一种类型
    """
    if left == '[' and right == ']':
        return True
    elif left == '(' and right == ')':
        return True
    elif left == '{' and right == '}':
        return True
    return False

def parchecker(symbolstring):
    """
    这是教材上的，总是比我高出一些啊,[{(
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolstring) and balanced:
        symbol = symbolstring[index]
        if symbol in "([{": #此处我最初用的是 symbol == 'a' or 'b' or 'c' 逻辑错误，后改为 symbol in ['(','[','{'],还是不好，直接用str的in多好
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop() #把pop提前,少了一次s.peek()
                if not matches(top,symbol):
                    balanced = False
        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


if __name__ == '__main__':
    print ('() balanced judge parenthe_check("()()") %s' %parenthe_check('()()'))
    print ('() balanced judge from course parChecker("()()") %s' %parChecker('()()'))
    print 'brackets ({[ balanced judge from parCheckerGeneral("{[()]}") %s' % parCheckerGeneral("{[()]}")
    print 'brackets ({[ balanced judge from parCheckerGeneral("{{[()]}") %s' % parCheckerGeneral("{{[()]}")
    print 'brackets ({[ balanced judge from online course parchecker("{{[()]}") %s' % parchecker("{{[()]}")
    
