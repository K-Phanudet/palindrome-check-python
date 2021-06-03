import re
import math

def isPalindrome(txt):
    txt = "".join(re.findall("[a-zA-Z]",txt)).lower()
    mid = math.ceil(len(txt)/2)
    if len(txt)%2 == 0 :
        mid -= 1
    front , back = 0 , -1 
    while(front<=mid):
        if txt[front] != txt[back]:
            return False
        front+=1
        back-=1
    return True