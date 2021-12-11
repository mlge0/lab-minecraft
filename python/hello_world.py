
# define first function
def first_function(msg):
    print(msg)

# define second function
def sum_two_integers(a, b):
    c = a + b
    return c

# define math problem
def math_problem_solver(a, b):
    c = (-12 * a) / (18 * a * b)
    return c
 

# invoke first function
message = "macintosh"
first_function(message)

# invoke second function
number_1 = 2 
number_2 = 446 
sum = sum_two_integers(number_1, number_2)

print(f"{number_1} plus {number_2} is {sum}")

# invoke math problem
solution = math_problem_solver(-12, 18)
print(solution)
