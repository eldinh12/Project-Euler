num = 100

# def square_difference(num):
#     sum_of_square = 0
#     for i in range(1, num + 1):
#         sum_of_square += pow(i, 2)

#     sum = 0
#     for i in range(1, num + 1):
#         sum += i

#     square_of_sum = pow(sum, 2)

#     difference = square_of_sum - sum_of_square
#     return difference

# print(square_difference(num))


def sum_of_square(num):
    sum_of_square = 0
    for i in range(1, num + 1):
        sum_of_square += pow(i, 2)
    return sum_of_square

def square_of_sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i

    square_of_sum = pow(sum, 2)
    return square_of_sum

difference = square_of_sum(num) - sum_of_square(num) 
print(difference)