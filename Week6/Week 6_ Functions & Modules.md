### Week 6: Functions & Modules

**Learning Outcome/Trait Assessment:**

- Define and call functions to promote code reusability and modularity.

- Understand the concepts of parameters, arguments, and return values.

- Differentiate between local and global variable scope.

- Import and utilize functions/variables from standard and custom modules.

- **Trait Assessment:** Modular code design, proper function arguments and return values, understanding code organization, effective use of libraries/modules, problem decomposition.

**Detailed Lecture Topics:**

1. **Introduction to Functions:**

   - **Why Functions?** (DRY - Don't Repeat Yourself principle, code organization, modularity, readability, easier debugging).

   - **Defining a Function:**

     - def function\_name(parameters): syntax.

     - Indentation defines the function body.

     - Docstrings for function documentation ("""Docstring here""").

   - **Calling a Function:**

     - function\_name(arguments) syntax.

     - Execution flow: call, execute function body, return to caller.

2. **Parameters and Arguments:**

   - **Parameters:** Variables defined in the function definition that receive values when the function is called.

   - **Arguments:** The actual values passed to the function when it is called.

   - **Positional Arguments:** Arguments matched to parameters by their position.

   - **Keyword Arguments:** Arguments passed with key=value syntax, allowing order independence.

   - **Default Parameter Values:** Providing a default value for a parameter if no argument is passed for it.

   - \*args (Arbitrary Positional Arguments - brief intro): Handling an unknown number of positional arguments.

   - \*\*kwargs (Arbitrary Keyword Arguments - *optional*, for more advanced classes).

3. **Return Values:**

   - The return statement: Sending a value back from the function to the caller.

   - Functions return None implicitly if no return statement is used.

   - Returning multiple values (Python returns them as a tuple, which can be unpacked).

4. **Variable Scope (Local vs. Global):**

   - **Local Variables:** Defined inside a function; only accessible within that function.

   - **Global Variables:** Defined outside any function; accessible from anywhere in the module.

   - The global keyword: Used inside a function to modify a global variable (use with caution, generally prefer passing parameters and returning values).

   - LEGB Rule (Local, Enclosing function locals, Global, Built-in) - conceptual understanding.

5. **Built-in Functions Recap:**

   - Briefly review functions used so far: print(), input(), len(), type(), int(), float(), str(), range(), sum(), max(), min(), sorted().

6. **Modules:**

   - **What is a Module?** A .py file containing Python code (functions, classes, variables).

   - **Why Use Modules?** (Organize code, reusability, share code, access to vast standard library and third-party functionalities).

   - **Importing Modules:**

     - import module\_name: Imports the entire module. Access with module\_name.function().

     - import module\_name as alias: Imports with an alias. Access with alias.function().

     - from module\_name import function\_name, variable\_name: Imports specific items directly into the current namespace. Access directly with function\_name().

     - from module\_name import \* (Wildcard import - explain why this is generally discouraged).

   - **Standard Library Examples:**

     - math module (e.g., math.sqrt(), math.pi).

     - random module (e.g., random.randint(), random.choice()).

**Detailed Labs:**

- **Lab 6.1: Simple Calculator Functions**

  - **Objective:** Students will define and use functions to perform basic arithmetic operations, practicing parameter passing and return values.

  - **Tasks (Common for Local & Colab):**

    1. Create a new Python file (lab6\_1.py) or Colab code cell.

    2. Define four functions: add(a, b), subtract(a, b), multiply(a, b), divide(a, b).

       - Each function should take two numbers as parameters.

       - Each function should return the result of the operation.

       - Add a docstring to each function explaining its purpose.

    3. Implement a simple menu-driven program (using a while loop from Week 3) that allows the user to choose an operation.

    4. Prompt the user for two numbers.

    5. Call the appropriate function based on user choice and print the returned result.

    6. Handle division by zero in the divide function (e.g., return "Error: Division by zero" or a specific value).

    7. **Challenge:** Add a function power(base, exponent) using default parameters (e.g., exponent=2 for squaring if not provided).

- **Lab 6.2: Custom Module and Standard Library Usage**

  - **Objective:** Students will create their own Python module and import it into another script, along with using functions from standard library modules (math, random).

  - **Tasks (Common for Local & Colab):**

    1. **Part 1: Create a Custom Module:**

       - Create a new Python file named my\_utils.py (or my\_utils.ipynb if strictly in Colab, though .py is better for true module concept).

       - Inside my\_utils.py, define at least two functions:

         - greet(name): Prints a greeting message (e.g., "Hello, \[name\]!").

         - is\_prime(number): Returns True if the number is prime, False otherwise.

       - (For Colab, this means a separate Colab notebook or a code cell that writes to a file, which is less common for module concepts, but for simplicity, they can just paste content into separate cells if files are complex).

    2. **Part 2: Use the Custom Module and Standard Modules:**

       - Create another new Python file (main\_program.py) or Colab code cell.

       - At the top of main\_program.py, import your my\_utils module: import my\_utils.

       - Import standard modules: import math, import random.

       - Call my\_utils.greet("Alice").

       - Test my\_utils.is\_prime() with a few numbers (e.g., 7, 10).

       - Use math.sqrt() to calculate the square root of a number.

       - Use random.randint() to generate a random number between 1 and 100.

       - **For Colab specifics:** If my\_utils.py is not easily managed as a separate file, the main\_program cell can simply define the functions from my\_utils within itself or the instructor can pre-upload my\_utils.py to Colab. The best way for true module demo in Colab is to use %%writefile my\_utils.py magic command in one cell to create the file, then import it in another.

**Detailed Activities:**

- **Activity 6.1: Refactoring a Previous Lab Assignment**

  - **Format:** Individual coding.

  - **Instructions:** Choose one of your completed lab assignments from Week 2 (Conditionals) or Week 3 (Loops). Identify repetitive blocks of code or logical units that could be encapsulated into functions. Refactor the code to use these new functions, improving readability and reusability.

  - **Example (Week 2):** The "Number Classifier" lab could have functions like is\_positive\_negative\_zero(num) and is\_even\_odd(num).

  - **Purpose:** Practical application of modular design principles, reinforcing function concepts.

- **Activity 6.2: Discussion: Benefits of Modular Programming & Standard Library Exploration**

  - **Format:** Class discussion or small group brainstorming.

  - **Instructions:**

    1. **Benefits of Modularity:** Discuss scenarios where breaking code into functions and modules significantly helps (e.g., large projects, teamwork, debugging, code testing).

    2. **Standard Library Exploration:** Provide a link to the official Python Standard Library documentation ([docs.python.org/3/library/](https://docs.python.org/3/library/)). Ask students to explore 2-3 modules they find interesting (e.g., datetime, os, sys, collections) and share a brief example of what they could use them for.

  - **Purpose:** Broaden understanding of Python's ecosystem, encourage independent exploration, and emphasize the importance of using existing tools.

### Sample Snippets for Class and Colab Ready

#### ***1. Functions: Definition, Parameters, Return, Scope**

**VS Code (function\_demo.py):**


Python



*\# function\_demo.py  
  
print(*"--- Basic Function Definition and Call ---")  
*def greet():  
    *"""Prints a simple greeting."""  
    print(*"Hello from a function!")  
  
greet() *\# Calling the function  
greet() *\# Call it again! Code reuse!  
  
print(*"\\n--- Functions with Parameters and Arguments ---")  
*def personalized\_greet(name):  
    *"""Greets the user by their provided name."""  
    print(*f"Hello, \{name\}!")  
  
personalized\_greet(*"Alice") *\# Positional argument  
personalized\_greet(*"Bob")  
  
*def describe\_pet(animal\_type, pet\_name):  
    *"""Displays information about a pet."""  
    print(*f"I have a \{animal\_type\}.")  
    print(*f"Its name is \{pet\_name\}.")  
  
describe\_pet(*"dog", *"Buddy") *\# Positional arguments  
describe\_pet(pet\_name=*"Whiskers", animal\_type=*"cat") *\# Keyword arguments (order doesn't matter)  
  
print(*"\\n--- Functions with Default Parameter Values ---")  
*def make\_coffee(size="regular", type="latte"):  
    *"""Describes a coffee order with default values."""  
    print(*f"Making a \{size\} \{type\} coffee.")  
  
make\_coffee() *\# Uses defaults: regular latte  
make\_coffee(*"large") *\# Uses default type: large latte  
make\_coffee(*type=*"espresso", size=*"small") *\# Custom order: small espresso  
  
print(*"\\n--- Functions with Return Values ---")  
*def add\_numbers(num1, num2):  
    *"""Adds two numbers and returns their sum."""  
    sum\_result = num1 + num2  
    *return sum\_result *\# Return the value  
  
result = add\_numbers(*10, *5)  
print(*f"Sum of 10 and 5: \{result\}")  
  
*def get\_circle\_area(radius):  
    *"""Calculates and returns the area of a circle."""  
    *import math *\# Local import (can be done, but usually at top of file)  
    area = math.pi \* (radius \*\* *2)  
    *return area  
  
radius\_val = *7  
area\_val = get\_circle\_area(radius\_val)  
print(*f"Area of circle with radius \{radius\_val\}: \{area\_val:.2f\}")  
  
print(*"\\n--- Returning Multiple Values (as a tuple) ---")  
*def get\_user\_info():  
    *"""Gets user input and returns name and age."""  
    name = *input(*"Enter your name: ")  
    age = *int(*input(*"Enter your age: "))  
    *return name, age *\# Returns as a tuple  
  
*\# name\_from\_func, age\_from\_func = get\_user\_info()  
*\# print(f"User: \{name\_from\_func\}, Age: \{age\_from\_func\}")  
  
print(*"\\n--- Variable Scope: Local vs. Global ---")  
global\_message = *"I am a global message." *\# Global variable  
  
*def show\_scope\_example():  
    local\_message = *"I am a local message." *\# Local variable  
    print(*f"Inside function (local): \{local\_message\}")  
    print(*f"Inside function (global): \{global\_message\}")  
  
show\_scope\_example()  
print(*f"Outside function (global): \{global\_message\}")  
*\# print(local\_message) \# This would cause a NameError  
  
*\# Modifying global variable (use with caution!)  
global\_counter = *0  
*def increment\_global\_counter():  
    *global global\_counter *\# Declare intent to modify global variable  
    global\_counter += *1  
    print(*f"Global counter inside func: \{global\_counter\}")  
  
increment\_global\_counter()  
increment\_global\_counter()  
print(*f"Global counter outside func: \{global\_counter\}")  


**Google Colab (in a code cell):**


Python



*\# function\_demo in Colab  
  
print(*"--- Basic Function Definition and Call ---")  
*def greet():  
    *"""Prints a simple greeting."""  
    print(*"Hello from a function!")  
  
greet() *\# Calling the function  
greet() *\# Call it again! Code reuse!  
  
print(*"\\n--- Functions with Parameters and Arguments ---")  
*def personalized\_greet(name):  
    *"""Greets the user by their provided name."""  
    print(*f"Hello, \{name\}!")  
  
personalized\_greet(*"Alice") *\# Positional argument  
personalized\_greet(*"Bob")  
  
*def describe\_pet(animal\_type, pet\_name):  
    *"""Displays information about a pet."""  
    print(*f"I have a \{animal\_type\}.")  
    print(*f"Its name is \{pet\_name\}.")  
  
describe\_pet(*"dog", *"Buddy") *\# Positional arguments  
describe\_pet(pet\_name=*"Whiskers", animal\_type=*"cat") *\# Keyword arguments (order doesn't matter)  
  
print(*"\\n--- Functions with Default Parameter Values ---")  
*def make\_coffee(size="regular", type="latte"):  
    *"""Describes a coffee order with default values."""  
    print(*f"Making a \{size\} \{type\} coffee.")  
  
make\_coffee() *\# Uses defaults: regular latte  
make\_coffee(*"large") *\# Uses default type: large latte  
make\_coffee(*type=*"espresso", size=*"small") *\# Custom order: small espresso  
  
print(*"\\n--- Functions with Return Values ---")  
*def add\_numbers(num1, num2):  
    *"""Adds two numbers and returns their sum."""  
    sum\_result = num1 + num2  
    *return sum\_result *\# Return the value  
  
result = add\_numbers(*10, *5)  
print(*f"Sum of 10 and 5: \{result\}")  
  
*def get\_circle\_area(radius):  
    *"""Calculates and returns the area of a circle."""  
    *import math *\# Local import (can be done, but usually at top of file)  
    area = math.pi \* (radius \*\* *2)  
    *return area  
  
radius\_val = *7  
area\_val = get\_circle\_area(radius\_val)  
print(*f"Area of circle with radius \{radius\_val\}: \{area\_val:.2f\}")  
  
print(*"\\n--- Returning Multiple Values (as a tuple) ---")  
*def get\_user\_info():  
    *"""Gets user input and returns name and age."""  
    name = *input(*"Enter your name: ")  
    age = *int(*input(*"Enter your age: "))  
    *return name, age *\# Returns as a tuple  
  
*\# name\_from\_func, age\_from\_func = get\_user\_info() \# Uncomment to test with user input  
*\# print(f"User: \{name\_from\_func\}, Age: \{age\_from\_func\}")  
  
print(*"\\n--- Variable Scope: Local vs. Global ---")  
global\_message = *"I am a global message." *\# Global variable  
  
*def show\_scope\_example():  
    local\_message = *"I am a local message." *\# Local variable  
    print(*f"Inside function (local): \{local\_message\}")  
    print(*f"Inside function (global): \{global\_message\}")  
  
show\_scope\_example()  
print(*f"Outside function (global): \{global\_message\}")  
*\# print(local\_message) \# This would cause a NameError  
  
*\# Modifying global variable (use with caution!)  
global\_counter = *0  
*def increment\_global\_counter():  
    *global global\_counter *\# Declare intent to modify global variable  
    global\_counter += *1  
    print(*f"Global counter inside func: \{global\_counter\}")  
  
increment\_global\_counter()  
increment\_global\_counter()  
print(*f"Global counter outside func: \{global\_counter\}")  


#### ***2. Modules: Custom and Standard Library**

**VS Code (two files: my\_utils.py and main\_app.py)**

**my\_utils.py:**


Python



*\# my\_utils.py (This is your custom module)  
  
*def greet(name):  
    *"""Prints a friendly greeting to the given name."""  
    print(*f"Hello, \{name\}! Welcome to my utility functions.")  
  
*def calculate\_area\_rectangle(length, width):  
    *"""Calculates the area of a rectangle."""  
    *return length \* width  
  
*def factorial(n):  
    *"""Calculates the factorial of a non-negative integer."""  
    *if n \< 0:  
        return *"Factorial is not defined for negative numbers."  
    *elif n == 0:  
        return *1  
    *else:  
        res = *1  
        *for i *in *range(*1, n + *1):  
            res \*= i  
        *return res  
  
PI\_VALUE = *3.14159 *\# A constant defined in the module  


**main\_app.py:**


Python



*\# main\_app.py (This is your main program)  
  
*\# --- Importing your custom module ---  
*import my\_utils *\# Imports the entire my\_utils.py file  
  
*\# --- Importing standard library modules ---  
*import math  
*import random *as rnd *\# Import with an alias  
  
print(*"--- Using functions from my\_utils module ---")  
my\_utils.greet(*"Students") *\# Call function using module\_name.function()  
area = my\_utils.calculate\_area\_rectangle(*5, *10)  
print(*f"Area of rectangle: \{area\}")  
  
num\_factorial = my\_utils.factorial(*5)  
print(*f"Factorial of 5: \{num\_factorial\}")  
  
print(*f"PI value from my\_utils: \{my\_utils.PI\_VALUE\}")  
  
print(*"\\n--- Using functions from math module ---")  
sqrt\_val = math.sqrt(*25)  
print(*f"Square root of 25: \{sqrt\_val\}")  
print(*f"Value of pi from math module: \{math.pi\}")  
  
print(*"\\n--- Using functions from random module (with alias) ---")  
random\_num = rnd.randint(*1, *100) *\# Generate random integer between 1 and 100  
print(*f"Random number: \{random\_num\}")  
  
fruits = \[*"apple", *"banana", *"cherry", *"date"\]  
random\_fruit = rnd.choice(fruits) *\# Choose a random element from a sequence  
print(*f"Random fruit: \{random\_fruit\}")  
  
print(*"\\n--- Importing specific items from a module ---")  
*from my\_utils *import greet, PI\_VALUE *\# Import only greet and PI\_VALUE directly  
  
greet(*"Instructors") *\# Can call directly without my\_utils.  
print(*f"PI\_VALUE (directly imported): \{PI\_VALUE\}")  
  
*\# This will cause an error because calculate\_area\_rectangle was not directly imported  
*\# calculate\_area\_rectangle(2,3) \# Uncomment to see error  


**Google Colab (using %%writefile magic command for my\_utils.py)**

**Code Cell 1 (Create my\_utils.py):**


Python



*\# Code Cell 1: Create my\_utils.py in Colab's file system  
%%writefile my\_utils.py  
*\# my\_utils.py (This is your custom module)  
  
*def greet(name):  
    *"""Prints a friendly greeting to the given name."""  
    print(*f"Hello, \{name\}! Welcome to my utility functions.")  
  
*def calculate\_area\_rectangle(length, width):  
    *"""Calculates the area of a rectangle."""  
    *return length \* width  
  
*def factorial(n):  
    *"""Calculates the factorial of a non-negative integer."""  
    *if n \< 0:  
        return *"Factorial is not defined for negative numbers."  
    *elif n == 0:  
        return *1  
    *else:  
        res = *1  
        *for i *in *range(*1, n + *1):  
            res \*= i  
        *return res  
  
PI\_VALUE = *3.14159 *\# A constant defined in the module  


**Code Cell 2 (main\_app.py equivalent in Colab):**


Python



*\# Code Cell 2: main\_app equivalent in Colab  
  
*\# --- Importing your custom module ---  
*import my\_utils *\# Imports the my\_utils.py file created in Cell 1  
  
*\# --- Importing standard library modules ---  
*import math  
*import random *as rnd *\# Import with an alias  
  
print(*"--- Using functions from my\_utils module ---")  
my\_utils.greet(*"Students") *\# Call function using module\_name.function()  
area = my\_utils.calculate\_area\_rectangle(*5, *10)  
print(*f"Area of rectangle: \{area\}")  
  
num\_factorial = my\_utils.factorial(*5)  
print(*f"Factorial of 5: \{num\_factorial\}")  
  
print(*f"PI value from my\_utils: \{my\_utils.PI\_VALUE\}")  
  
print(*"\\n--- Using functions from math module ---")  
sqrt\_val = math.sqrt(*25)  
print(*f"Square root of 25: \{sqrt\_val\}")  
print(*f"Value of pi from math module: \{math.pi\}")  
  
print(*"\\n--- Using functions from random module (with alias) ---")  
random\_num = rnd.randint(*1, *100) *\# Generate random integer between 1 and 100  
print(*f"Random number: \{random\_num\}")  
  
fruits = \[*"apple", *"banana", *"cherry", *"date"\]  
random\_fruit = rnd.choice(fruits) *\# Choose a random element from a sequence  
print(*f"Random fruit: \{random\_fruit\}")  
  
print(*"\\n--- Importing specific items from a module ---")  
*from my\_utils *import greet, PI\_VALUE *\# Import only greet and PI\_VALUE directly  
  
greet(*"Instructors") *\# Can call directly without my\_utils.  
print(*f"PI\_VALUE (directly imported): \{PI\_VALUE\}")  
  
*\# This will cause an error because calculate\_area\_rectangle was not directly imported  
*\# calculate\_area\_rectangle(2,3) \# Uncomment to see error  


**แหล่งที่มา**

1. [https://github.com/MuchachitoEstrella/python-projects](https://github.com/MuchachitoEstrella/python-projects)
