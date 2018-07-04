def main():
    """This is the control function which response according to user response"""
    current_prime=2
    
    while True:
        response=input('Do you want the next prime number Y/N(yes or no)')
        
        if response=='Y':
            print(current_prime)
            
            current_prime=genPrime(current_prime)                        
        else:
            break

def genPrime(current_prime):
    """This function generates the next prime number"""
    new_prime=current_prime+1
    while True:
        if not isPrime(new_prime):
            new_prime+=1
        else:
            break
    return new_prime

def isPrime(number):
    if number==2:
        return True
    elif number%2==0:
        return False
    elif number==3:
        return True
    else:
        for x in range(3,number):
            if number%x==0:
                return False
    return True
if __name__=='__main__':
    main()