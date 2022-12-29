"""Program to calculate factorial recursively"""
def factorial(num):
    result = 1
    if num <= 0 or num == 1:
        return 1
    else:
        for i in range(1,num + 1):
            result = result * i
        return result
        

        
if __name__ == "__main__":
        print(factorial(5))
        
    
