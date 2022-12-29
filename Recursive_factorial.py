"""Program to calculate factorial recursively"""
def factorial(num):
    result = 1
    if num == 0 or num == 1:
        return 1
    for i in range(num):
        result = num * factorial(num-1)
        return result
        
if __name__ == "__main__":
        print(factorial(2))
    
