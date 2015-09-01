#coding=utf-8

def toStr(integer,base):
    """
    converting integer to a str in base between 2 and 16, stack can do it also
    """
    convertString = '0123456789ABCDEF'
    if integer < base :
        return convertString[integer]
    else:
        return toStr(integer//base,base) + convertString[integer % base]


def strReverse(input):
    """
    reverse input str using recursion
    """
    if not isinstance(input,str):
        print ('Warning! str please')

    if len(input) == 1:
        return input
    else:
        return input[-1] + strReverse(input[:-1])


def isPalindrome(input):
    """
    判断input是否是回文,必须考虑最后剩下的是1个字符或2个字符，才可以应用len(input)为奇数或偶数
    """
    if len(input) == 1:
        return True
    elif len(input) == 2:
        return  input[0] == input[-1]
    else:
        return input[0] == input[-1] and isPalindrome(input[1:-1])

def palindromeTest(input):
    #去掉input中的空格，标点 
    input = [i.lower() for i in input if i.isalpha()] 
    input = ''.join(input) 
    #print input
    #print len(input)

    return isPalindrome(input)




if __name__ == '__main__':
    print toStr(89,2)
    print strReverse('xiaoshi')
    print palindromeTest('kayak') 
    print palindromeTest('aibohphobia') 
    print palindromeTest('Live not on evil') 
    print palindromeTest('Reviled did I live, said I, as evil I did deliver') 
    print palindromeTest("Go hang a salami; I’m a lasagna hog.")    
    print palindromeTest('Able was I ere I saw Elba') 
    print palindromeTest('Kanakanak – a town in Alaska') 
    print palindromeTest('Wassamassaw – a town in South Dakota')
