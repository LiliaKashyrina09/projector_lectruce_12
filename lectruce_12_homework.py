#Task 1

def is_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('user_type') != 'admin':
            raise ValueError("Permission denied")
        return func(*args, **kwargs)
    return wrapper

@is_admin
def show_customer_receipt(user_type: str):
    print("Customer receipt displayed successfully.")

try:
    show_customer_receipt(user_type='user')
except ValueError as e:
    print(e) 

try:
    show_customer_receipt(user_type='admin')
except ValueError as e:
    print(e) 



#Task 2
def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Found 1 error during execution of your function: {type(e).__name__}: no such key as {str(e)}")
    return wrapper

@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})  
some_function_with_risky_operation({'key': 'bar'}) 



#Task 3 
def check_types(func):
    def wrapper(*args, **kwargs):
        for arg_val, (arg_name, arg_type) in zip(args, func.__annotations__.items()):
            if not isinstance(arg_val, arg_type):
                raise TypeError(f"Argument {arg_name} must be {arg_type.__name__}, not {type(arg_val).__name__}")
        
        return func(*args, **kwargs)
    
    return wrapper

@check_types
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2)) 

try:
    print(add("1", "2"))  
except TypeError as e:
    print(e)  

#Task 4
def memoize(func):
    cache = {}  

    def wrapper(*args):
        if args in cache:  
            return cache[args]  
        else:
            result = func(*args) 
            cache[args] = result  
            return result

    return wrapper

@memoize
def compute_expensive_operation(x):
    print(f"Computing for {x}")  
    return x * x  

print(compute_expensive_operation(4))  
print(compute_expensive_operation(4))  
print(compute_expensive_operation(5))  
print(compute_expensive_operation(5))  



#Task 5
import time

def rate_limiter(calls_per_minute):
    interval = 60 / calls_per_minute
    last_called = [0]  

    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            elapsed = current_time - last_called[0]
            if elapsed < interval:
                print("Function call too soon. Try again later.")
                return  
            last_called[0] = current_time  
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limiter(calls_per_minute=1) 
def say_hello():
    print("Hello!")

say_hello() 
say_hello()  

