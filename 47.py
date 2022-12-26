'''Write a Python function to check whether a number is in a given range'''


def test_range(n):
    for i in range(3,9):
        if n==i:
            print( " %s is in the range"%str(n))
            break
    else :
        print("The number is outside the given range.")
test_range(5)
test_range(10)
