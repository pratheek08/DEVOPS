def example1():
    # Using single quotes
    str1 = 'Hello Python'
    print(str1)
    # Using double quotes
    str2 = "Hello Python"
    print(str2)
    # Using triple quotes
    str3 = '''''Triple quotes are generally used for
    represent the multiline or
    docstring'''
    print(str3)

def example2():
    str = "HELLO"
    print(str[0])
    print(str[1])
    print(str[2])
    print(str[3])
    print(str[4])
    # It returns the IndexError because 6th index doesn't exist
    try:
        print(str[6])
    except IndexError:
        print("Index Error: string index out of range")

def example3():
    str = "JAVATPOINT"
    # Start Oth index to end
    print(str[0:])
    # Starts 1th index to 4th index
    print(str[1:5])
    # Starts 2nd index to 3rd index
    print(str[2:4])
    # Starts 0th to 2nd index
    print(str[:3])
    # Starts 4th to 6th index
    print(str[4:7])

def example4():
    str = 'JAVATPOINT'
    print(str[-1])
    print(str[-3])
    print(str[-2:])
    print(str[-4:-1])
    print(str[-7:-2])
    # Reversing the given string
    print(str[::-1])
    try:
        print(str[-12])
    except IndexError:
        print("IndexError: string index out of range")

def example5():
    str = "HELLO"
    try:
        str[0] = "h"
    except TypeError:
        print("TypeError: 'str' object does not support item assignment")
    str = "hello"
    print(str)

def example6():
    str1 = "JAVATPOINT"
    try:
        del str1[1]
    except TypeError:
        print("TypeError: 'str' object doesn't support item deletion")
    try:
        del str1
        print(str1)
    except NameError:
        print("NameError: name 'str1' is not defined")

def example7():
    str = "Hello"
    str1 = " world"
    print(str*3) # prints HelloHelloHello
    print(str+str1) # prints Hello world
    print(str[4]) # prints o
    print(str[2:4]) # prints ll
    print('w' in str) # prints False as w is not present in str
    print('wo' not in str1) # prints False as wo is present in str1
    print(r'C://python37') # prints C://python37 as it is written
    print("The string str : %s"%(str)) # prints The string str : Hello

def example8():
    # using triple quotes
    print('''''They said, "What's there?"''')
    # escaping single quotes
    print('They said, "What\'s going on?"')
    # escaping double quotes
    print("They said, \"What's going on?\"")

def example9():
    Integer = 10
    Float = 1.290
    String = "Devansh"
    print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(Integer,Float,String))

def example10():
    # Python code to show the difference between creating a list and a tuple
    list_ = [4, 5, 7, 1, 7]
    tuple_ = (4, 1, 8, 3, 9)
    print("List is: ", list_)
    print("Tuple is: ", tuple_)

def example11():
    # Updating the element of list and tuple at a particular index
    list_ = ["Python", "Lists", "Tuples", "Differences"]
    tuple_ = ("Python", "Lists", "Tuples", "Differences")
    list_[3] = "Mutable"
    print(list_)
    try:
        tuple_[3] = "Immutable"
        print(tuple_)
    except TypeError:
        print("Tuples cannot be modified because they are immutable")

def example12():
    # Code to show the difference in the size of a list and a tuple
    list_ = ["Python", "Lists", "Tuples", "Differences"]
    tuple_ = ("Python", "Lists", "Tuples", "Differences")
    # printing sizes
    print("Size of tuple: ", tuple_.__sizeof__())
    print("Size of list: ", list_.__sizeof__())

def example13():
    # printing directory of list
    print(dir(list_))

def example14():
    # Printing directory of a tuple
    print( dir(tuple_), end = ", ")

def main():
    print("Enter the example number (1-14):")
    example_number = int(input())
   
    if example_number == 1:
        example1()
    elif example_number == 2:
        example2()
    elif example_number == 3:
        example3()
    elif example_number == 4:
        example4()
    elif example_number == 5:
        example5()
    elif example_number == 6:
        example6()
    elif example_number == 7:
        example7()
    elif example_number == 8:
        example8()
    elif example_number == 9:
        example9()
    elif example_number == 10:
        example10()
    elif example_number == 11:
        example11()
    elif example_number == 12:
        example12()
    elif example_number == 13:
        example13()
    elif example_number == 14:
        example14()
    else:
        print("Invalid example number")

if __name__ == "__main__":
    main()