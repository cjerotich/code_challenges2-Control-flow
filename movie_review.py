#Define our function to accept a single number called rating
#If the rating is equal to or less than 5, return "Avoid at all costs!"
#If the rating was less than 9, return "This one was fun."
#If neither of the if statement conditions were met, return "Outstanding!"

# Write your movie_review function here:
def movie_review(rating):
  if(rating <= 5):
    return "Avoid at all costs!"
  if(rating < 9):
    return "This one was fun."
  return "Outstanding!"

# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."
