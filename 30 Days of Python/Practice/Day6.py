# Day 6 of 100DaysOfCode Practice

# _____________1_______________
#Functions with Outputs
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"
print(format_name("RIshaBh", "CuRIous"))

# _____________2_______________
# Docstrings for documentation of function
# Use """ This is documentation code in function defination """

# _____________3_______________
# Scope
enemies = 1
def increase_enemies():
  """ This function gives increase value of enemies"""
  enemies = 2
  print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")

# _____________4_______________
# modify global variable
# use of global in function
def function():
  global enemies
  enemies+=3
  print(f"enemies inside a function[modify global variable] {enemies}") 
function()
print(f"enemies outside a function[after modify global variable] {enemies}")