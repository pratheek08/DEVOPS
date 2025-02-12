def square(num):
    """This function computes the square of the number."""
    return num**2

def a_function(string):
    """This prints the value of length of string"""
    return len(string)

def square_list(item_list):
    '''This function will find the square of items in the list'''
    squares = []
    for l in item_list:
        squares.append(l**2)
    return squares

def function(n1, n2=20):
    print("number 1 is:", n1)
    print("number 2 is:", n2)

def keyword_function(n1, n2):
    print("number 1 is:", n1)
    print("number 2 is:", n2)

def function_with_args(*args_list):
    ans = []
    for l in args_list:
        ans.append(l.upper())
    return ans

def square_with_return(num):
    return num**2

def square_no_return(num):
    num**2

lambda_ = lambda argument1, argument2: argument1 + argument2

def scope_example():
    num = 50
    print("Value of num inside the function:", num)

def nested_function():
    string = 'Python functions tutorial'
    x = 5
    def inner_function():
        print(string)
        print(x)
    inner_function()

def abs_example():
    integer = -20
    print('Absolute value of -40 is:', abs(integer))

def bin_example():
    x = 10
    y = bin(x)
    print(y)

def callable_example():
    x = 8
    print(callable(x))

def sum_example():
    s = sum([1, 2, 4])
    print(s)

def any_example():
    l = [4, 3, 2, 0]
    print(any(l))

def eval_example():
    x = 8
    print(eval('x + 1'))

def float_example():
    print(float(9))

def format_example():
    print(format(123, "d"))

def frozenset_example():
    letters = ('m', 'r', 'o', 't', 's')
    fSet = frozenset(letters)
    print('Frozen set is:', fSet)

def globals_example():
    age = 22
    globals()['age'] = 22
    print('The age is:', age)

def iter_example():
    list = [1, 2, 3, 4, 5]
    listIter = iter(list)
    print(next(listIter))

def len_example():
    strA = 'Python'
    print(len(strA))

def list_example():
    String = 'abcde'
    print(list(String))

# Main program to execute the chosen example
def run_example(example_number):
    if example_number == 1:
        print(square(6))  # Example 1: User-defined function (square)
    elif example_number == 2:
        print(a_function("Functions"))  # Example 2: Calling a function (length)
    elif example_number == 3:
        print(square_list([17, 52, 8]))  # Example 3: Pass by reference vs. value (squares)
    elif example_number == 4:
        function(30)  # Example 4: Default argument
    elif example_number == 5:
        keyword_function(50, 30)  # Example 5: Keyword arguments
    elif example_number == 6:
        print(function_with_args('Python', 'Functions', 'tutorial'))  # Example 6: Variable-length arguments
    elif example_number == 7:
        print(square_with_return(52))  # Example 7: Return statement (with return)
    elif example_number == 8:
        square_no_return(52)  # Example 8: Return statement (without return)
    elif example_number == 9:
        print(lambda_(20, 30))  # Example 9: Lambda function
    elif example_number == 10:
        scope_example()  # Example 10: Scope and lifetime of variables
    elif example_number == 11:
        nested_function()  # Example 11: Nested functions
    elif example_number == 12:
        abs_example()  # Example 12: abs() function
    elif example_number == 13:
        bin_example()  # Example 13: bin() function
    elif example_number == 14:
        callable_example()  # Example 14: callable() function
    elif example_number == 15:
        sum_example()  # Example 15: sum() function
    elif example_number == 16:
        any_example()  # Example 16: any() function
    elif example_number == 17:
        eval_example()  # Example 17: eval() function
    elif example_number == 18:
        float_example()  # Example 18: float() function
    elif example_number == 19:
        format_example()  # Example 19: format() function
    elif example_number == 20:
        frozenset_example()  # Example 20: frozenset() function
    elif example_number == 21:
        globals_example()  # Example 21: globals() function
    elif example_number == 22:
        iter_example()  # Example 22: iter() function
    elif example_number == 23:
        len_example()  # Example 23: len() function
    elif example_number == 24:
        list_example()  # Example 24: list() function
    else:
        print("Invalid example number.")

# Prompt user for example number
example_number = int(input("Enter the example number (1-24): "))
run_example(example_number)