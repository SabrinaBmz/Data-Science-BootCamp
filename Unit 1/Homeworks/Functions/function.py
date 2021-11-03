# palindrome
def check_pal(word):
    rev_word = reversed(word)
    if list(word) == list(rev_word):
        return False
    return True

print(check_pal("nurses run"))

# prime number
def check_prime(number):
    if number > 1:
        for i in range(2, number // 2):
            if number % i == 0:
                return False
            break
        else:
            return True
    else:
        return False

print(check_prime(3))

# range
def check_range(number):
    if number in range(3, 9):
        return True
    else:
        return False

print(check_range(10))

# factorial
def cal_factorial(number):
    if number < 0:
        return "Negative number"
    elif number == 0:
        return 0, 1
    else:
        for i in range(1, number + 1):
            number = number * i
        return number

print(cal_factorial(6))

# reverse
def reverse_string(str):
    for i in str[:]:
        st = str[i]

# sum
def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum
print(sum_list((1, 2, 4, 5)))

# max
def max_number(n1, n2, n3):
    if (n1 >= n2) and (n1 >= n3):
        max = n1

    elif (n2 >= n1) and (n2 >= n3):
        max = n2
    else:
        max = n3

    return max

print(max_number(3, 5, 9))