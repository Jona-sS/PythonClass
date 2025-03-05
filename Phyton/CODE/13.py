def my_and(a, b):
    if a:
        return b
    else:
        return a#0 bei bool
def my_or(a, b):
    if a :
        return a
    else:
        return b
#"Adam" or False and "Eva" 
#("Adam" or False) and "Eva" 
#"Adam" or (False and "Eva")
print(my_and(my_or("Adam", False), "Eva"))
print(my_or("Adam", my_and(False, "Eva")))