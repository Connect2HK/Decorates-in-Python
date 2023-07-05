def fun(text):
  def wrapper(use):
    modified_text=use.upper()
    return (text(modified_text))
  return wrapper

#without using decorators 
def show(name):
  print(f"i am ,{name}")
show("an Engineer")

#output will be -- i am, an Engineer

#Using @decorators 
#output is - i am, AN ENGINEER
@uppercase_decorator
def show_decorators(name):
  print(f"i am, {name}")

show_decorators("an engineer")



    
