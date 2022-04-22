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
            break
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
        valid = "1234567890"
        if valid.find(i):
            print("invalid entry for an integer")
            break
    else:
        result = int(inp)
        return result
 


x = inputIntV2("Enter an integer")
x = int(x)
