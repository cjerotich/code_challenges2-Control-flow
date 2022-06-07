
#Define the function to accept a single parameter called num

#Use a combination of <, > and and to create a contradiction in an if statement.
#If the condition is true, return True, otherwise return False. The trick here is
#that because we’ve written a contradiction, the condition should never be
#true, so we should expect to always return False.

# Write your always_false function here:
def always_false(num):
  if num > num and num < num:
    return True
  else:
    return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
#should print False
print(always_false(-1))
#should print False
print(always_false(1))
#should print False
