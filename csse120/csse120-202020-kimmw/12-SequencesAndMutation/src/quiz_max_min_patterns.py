#Q8.a
def get_max_8a(numbers):
    biggest=numbers[0]
    # for k in range(1, len(numbers)):
    #     if(numbers[k]>biggest):
    #         biggest= numbers[k]
    # return biggest


    for k in numbers:
        if k>biggest:
            biggest=k
    return biggest







#Q8.b

def get_max_8b(numbers):
    index_of_biggest= 0
    for k in range(1, len(numbers)):
        if(numbers[index_of_biggest]< numbers[k]):
            index_of_biggest=k
    return numbers[index_of_biggest]




#Q9
def get_max_9(numbers):
    if (len(numbers) < 1):
        return None
    index_of_biggest = 1
    for k in range(1, len(numbers),2):
        if (numbers[index_of_biggest] < numbers[k]):
            index_of_biggest = k
    return numbers[index_of_biggest]

#Q10

def get_max_10(numbers):
    biggest= None
    for value in numbers:
        if value>0:
            if biggest is None or value>biggest:
                biggest=value
    return biggest






numbers= [-3, 4, 10, 0, 5]
print("Expected: 10")
print("Actual 8a: ", get_max_8a(numbers))
print("Actual 8b: ", get_max_8b(numbers))

print("expected9: 4")
print("actual 9: ", get_max_9(numbers))


print( get_max_10([-1,-2,-3]))