import random
import time
 

operators = ["+", "-", "*"]

min_operand = 1

max_operand = 20

totalProblems = 10

 

def generate_problem():

    left = random.randint(min_operand, max_operand)

    right = random.randint(min_operand, max_operand)

    operator = random.choice(operators)

 

    expression = str(left) + " " + operator + " " + str(right)

    answer = eval(expression)

    return expression, answer

wrong = 0
input("Press enter to start")
print("---------------------------------")
startTime = time.time()

for i in range(totalProblems):

   expression, answer = generate_problem()

   while True:

      guess = input("Problem #" + str(i + 1) + ": " + expression + " = ")

      if guess == str(answer):

         break
         wrong += 1
         
endTime = time.time()
totalTime = round(endTime - startTime, 2)
         
print("---------------------------------")
print("Nice job! You finished in", totalTime, "seconds, with")