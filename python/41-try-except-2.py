

# try:
#     # 1
#     # print(10/0)
#     # 2
#     # print('10'/0)
#     # 3
#     print(10/5)
    
# except ZeroDivisionError as e:
#     print(type(e))   # <class 'ZeroDivisionError'>
#     print(f"Error - {e}")   # Error - division by zero
    
# except TypeError as e:
#     print(type(e))   # <class 'TypeError'>
#     print(f"Error - {e}")  # Error - unsupported operand type(s) for /: 'str' and 'int'
    
# # if you don't know what error will be:
# except Exception as e:
#     print(type(e))   # <class 'ZeroDivisionError'>
    
# else:
#     print("There was no error")  # There was no error

# finally:
#     print('Continue...')

# ===============================================

# generate an error:

def divide_nums(a, b):
    if b == 0:
        raise TypeError("Cannot divide by zero")
    return a / b

try:
    divide_nums(10, 0)    
except ZeroDivisionError as e:
    print(type(e))   # <class 'ZeroDivisionError'>
    print(f"Error - {e}")   # Error - division by zero
    
except TypeError as e:
    print(type(e))   # <class 'TypeError'>
    print(f"Error - {e}")  # Error - unsupported operand type(s) for /: 'str' and 'int'
    
# if you don't know what error will be:
except Exception as e:
    print(type(e))   # <class 'ZeroDivisionError'>
    print(f"Error - {e}")
    
else:
    print("There was no error")  # There was no error

finally:
    print('Continue...')