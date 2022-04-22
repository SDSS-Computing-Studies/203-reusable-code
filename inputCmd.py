#!python3

def inputIntV1(question):
  """
  input parameters: 
  string question - this is the question that you will ask people when you prompt for input
  """
  while True:
      inp = input(question)
      try:
          result = int(inp)
      except Exception as e:
          print("invalid entry for an interger")
  return result
          
def inputIntV2(question):
  """
    input parameters: 
    string question - this is the question that you will ask people when you prompt for input
  """
  while True:
      inp = input(question)
        for i in inp:
          if i not in ["1234567890"]:
            print("invalid entry for an integer")
            break
        else:
          result = int(inp)
          return result
 

x = inputIntV1("Enter an integer")
print(f"The integer is {x}")
x = inputIntV2("Enter another integer")
print(f"The second integer is {x}")
    
