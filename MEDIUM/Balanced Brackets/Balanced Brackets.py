def balancedBrackets(string):
  openingBrackets = '({['
  closingBrackets = ")}]"
  matchingPair = {')':'(','}':'{',']':'['}
  # Keep track the opening brackets
  stack = []
  for item in string:
    if item in openingBrackets:
      stack.append(item)
    elif item in closingBrackets:
      if len(stack)==0: # When no opening brackets exists
        return False
      elif stack[-1]!= matchingPair[item]: # When pair doesn't match
        return False
      else: # When pair matches
        stack.pop()

  return len(stack)==0

