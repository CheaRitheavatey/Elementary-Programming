# We are given a (big big) array a of n numbers (n>0 assumed).
# example
# sum_of_products([12,13]) = 12 + 13 + 12*13 = 181
# sum_of_products([2,3,7]) = 2 + 3 + 7 + 2*3 + 2*7 + 3*7 + 2*3*7 = 95 

def sum_of_products(a):
    result = 1
    for i in a:
        result *= (1+i)
    return result - 1




# Example usage
print(sum_of_products([-9, 17, 21, 35, 6, 4, 2, 1, 0, 1, 1, 1, 2, 3, 4, 7, 129]))  # Output: -11955879936001

# Example usage
print(sum_of_products([12, 13]))  # Output: 181
print(sum_of_products([2, 3, 7])) # Output: 95

print(sum_of_products([-9,17,21,35,6,4,2,1,0,1,1,1,2,3,4,7,129]))