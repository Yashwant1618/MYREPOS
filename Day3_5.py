
data = 400 #global variable 
def function1():
    data=12  #local variable 
    print(f"Data inside function1 = {data}")
    data+=5
    print(f"Data modified inside function1 = {data}")

function1()
print(f"Data = {data}")