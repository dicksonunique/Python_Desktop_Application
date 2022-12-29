'''A program to compute pallindrome'''
def pallindrome(text):
    reverse_test = text[::-1]
    if text == reverse_test:
        return F"{text} is a pallindrome"
    else:
        return F"{text} is not a pallindrome"


if __name__ == "__main__":
    t = 'poooe'
    print(pallindrome(t))
    

    
