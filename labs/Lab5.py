def is_prime(num): 

    if num <= 1: 

        return False 

    if num <= 3: 

        return True 

    if num % 2 == 0 or num % 3 == 0: 

        return False 

    i = 5 

    while i * i <= num: 

        if num % i == 0 or num % (i + 2) == 0: 

            return False 

        i += 6 

    return True 

 

def count_primes_between(start, end): 

    count = 0 

    for num in range(max(2, start), end + 1): 

        if is_prime(num): 

            count += 1 

    return count 

 

try: 

    input_number = int(input("Enter a number: ")) 

    if input_number < 2: 

        print("Please enter a number greater than or equal to 2.") 

    else: 

        prime_count = count_primes_between(2, input_number) 

        print(f"There are {prime_count} prime numbers between 2 and {input_number}.") 

except ValueError: 

    print("Invalid input. Please enter a valid number.") 
