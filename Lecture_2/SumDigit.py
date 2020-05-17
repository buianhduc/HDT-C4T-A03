def sum_digit(num):
    if(num == 0): return 0
    else:
        return (sum_digit(int(num/10))+int(num%10))

print(sum_digit(1234))
