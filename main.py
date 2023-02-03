print("== Math Multiples Game ==")
print()
print("You'll input a number and you try to get the correct answer to it's multiples of up to 10 ")
print()
number = int(input("What's your multiple?  "))
print(number)

counter = 0
for multiple in range (1, 11):
  correct = number * multiple
  print (number, "x", multiple)
  answer = int(input("=  "))
  if answer == correct:
    print("Correct!!! 👍🏾")
    counter += 1
  else:
    print("Not correct. Keep practicing")
    exit()

if counter == 10:
  print("Perfect 10/10. Congratulations!!! 🎉🍾🥳🥂")
else:
  print("You got", counter, "out of 10 correct.")