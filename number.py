#wap to check whether a number is palindrome or not
number = int(input())
dig = [int(x) for x in str(number)]
if(dig == dig[::-1]):
    print("number is palindrome")
else:
    print("number is not palindrome")