###solution to exercise 91 from ben stephenson's "the python workbook".

def precedence(operator):
  if operator == '+' or operator == '-':
    return 1
  elif operator == '*' or operator == '/':
    return 2
  elif operator == '^':
    return 3
  else:
    return -1

operator = str(input('Enter an operator: '))
if precedence(operator) != -1:
  print(f'The precedence of that operator is {precedence(operator)}.')
else:
  print('That is not a valid operator.')
