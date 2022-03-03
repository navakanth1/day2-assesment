#wap to check whether a str is palindrom or not
string = input()
st = string[::-1]
if(st ==string):
    print("str is palindrome")
else:
    print("str is not palindrome")