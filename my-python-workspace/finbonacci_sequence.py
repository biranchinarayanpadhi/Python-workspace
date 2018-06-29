def generate_fibonacci(max_limit):
    list_of_sequence=[0,1]
    for number in range(max_limit):
        list_of_sequence.append(list_of_sequence[-1]+list_of_sequence[-2])    
    return list_of_sequence

def main():
    max_limit=int(input('Enter the number upto which you want the fibo sequence'))
    returned_fibo_list=generate_fibonacci(max_limit)
    print(returned_fibo_list)

if __name__=='__main__':
    main()
