factors = lambda n: [x for x in range(1,n+1) if n%x==0]
is_prime = lambda n: len(factors(n))==2
primefactors = lambda n: list(filter(is_prime ,factors(n)))
    
def main():
    result_dict={}
#    number whose prime factors are to be retrived= NPF
    NPF=int(input('enter the number whose prime factors are rrequired'))
#    result=prime_factorization(NPF) 'call this function if you want to use another method \
#                                     and comment the next line'
    result=primefactors(NPF)
    result_dict[NPF]=result
    print(result_dict)

if __name__=='__main__':
    main()

'These two function is used for another method of finding prime_factorization'

#def prime_factorization(N):
#    prime_factors=[1]
#    number_with_prime_factors={}
#    numbers=1
#    while numbers<N:
#       if N%numbers==0:
#           if isPrime(numbers):
#               prime_factors.append(numbers)
#       numbers+=1
#    number_with_prime_factors[N]=prime_factors
#    return number_with_prime_factors

#def isPrime(n):
#    count=0
#    for numbers in range(1,n+1):
#        if n%numbers==0:
#            count+=1
#    if count==2:
#        return True
#    else:
#        return False

