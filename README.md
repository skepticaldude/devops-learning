# devops-learning
this is me documenting my devops journey here on github
## Goal 
Document DevOps projects and progress.

# linux
## Here are some of my linux notes
In my latest lab, I focused on fundamental Linux commands for identifying user and system information—small commands, but very useful in everyday system work.

What I practiced:

Using whoami to identify the current logged-in user

Displaying the system date and time with date

Formatting output using options like +%R (time) and +%x (date)

Running multiple commands on a single line using a semicolon

This lab reinforced how efficiency in the command line comes from understanding simple tools and combining them effectively. These basics show up everywhere in scripting, automation, and system administration, so mastering them early matters.



# python
#important sidenote!
If you know that a try...except block is the "safety net for errors" and a while loop is a "repeater," you can design solutions. 
this basically means this helps to keep the system stable and running regardless of encountering errors in our code, it's basically a saftey net for everything we're doing, then loop is simple a repeater as specified
i'll be moving this to my cherrytree but later, i have to complete my labs! 

## update 21st of january 2026
i uploaded a mini project i worked on with python, this is still me working on my DevOps skills!

## update 26th of january 2026
i added a program printing even or odd numbers, still working with python!

i added a script demonstrating loops and exception handling which is the number_analyzer.py 

just incase there's confusion in the python commit messages i moved all the files i learnt with to a new folder after learning 

i think i understand github a little better now, and it really is an excellent tool for documentation, linus did something here!

wrote a small script that performs a countdown, i understand loops better now the range especially how it includes the start, stop and step in the parenthesis *still dont know if it's an argument* hopefully it'll make understanding nested loops a lot easier!

## function in python 
today i'll be working with functions in python

Functions are defined using the def keyword followed by the function name and parameters in parentheses. The function body is indented.
This function takes a name parameter and returns a greeting string. We then call the function with the argument "Alice" and print the result.
The return statement is used to return a value from the function. If no return statement is present, the function returns None.
Functions can be used to encapsulate reusable code and perform specific tasks. It's the main building block of Python programs.

we wrote a function program to calculate the area of something, i think i understand how parameters works a bit better now 

I'm learning on default arguments
Default arguments allow you to initialize parameters with a fallback value if no argument is provided during the function call.

still yet to understand functions on returning multiple values 
ill add a project so i can come back to this!!

this is the note generated from labex! i'll come back to this hopefully

Python Multi-Value Returns
Concept: Functions can return multiple results separated by commas.
Mechanism: Python packs these values into a Tuple.
Unpacking: You can assign the results directly to multiple variables in one line.
Pro Tip: If you only need the maximum and want to ignore the minimum, developers often use an underscore for the unwanted value:
_, maximum = min_max([1, 5, 3])

Spoiler: Python will throw a ValueError because it expects the number of variables to match the number of returned items exactly!

#### scope in functions 
Definition Before Invocation
The Core Rule:
A function must be defined (using the def keyword) before it can be called (executed). Because Python reads code from top to bottom, it needs to store the function name in memory before it can use it.

Key Points:

Top-Down Flow: Python processes script instructions sequentially.
NameError: If you call a function before its definition, Python will raise a NameError: name '...' is not defined.
Exception (Inside Other Functions): You can call a function inside another function even if the definition appears later in the file, provided the final "trigger" call happens after both are defined.

this simply means that you must call a function esp locally before it runs  ###########
remember:
To modify a global variable inside a function, use the global keyword:

#### summary on modularization with functions
I explored two fundamental concepts in Python programming: functions and modules. I have mastered defining and using functions, understanding scope, creating modules, and organizing code into packages.

What I Accomplished:
Functions & Scope: I started by creating simple functions and progressed to complex concepts like function scope and managing global variables.

Modularization: I learned how to create modules to separate related functions and variables into different files, making my code significantly more maintainable and reusable.

Import Strategies: I explored various ways to import functionality, including importing specific functions and using aliases. This allows me to write concise, readable code while avoiding naming conflicts.

Package Organization: I learned how to structure a package by organizing modules into a directory hierarchy—a vital skill for managing larger, professional-scale projects.

Why This Matters:
Mastering functions and modules is crucial for writing efficient, well-organized Python code. These skills are the foundation for building complex programs and collaborating on larger projects. I am committed to practicing these concepts regularly and exploring the vast ecosystem of Python packages to further enhance my development capabilities.

### this is on the python function modularization folder
In this project, I developed a specialized Python module containing functions for space mission calculations and successfully integrated them into a main program.

Key Skills Applied:
Functional Programming: I practiced defining precise functions tailored for specific mission parameters.

Module Integration: I successfully imported custom functions from external files into a main script, ensuring clean code separation.

Practical Calculation: I used these tools to perform complex calculations, bridging the gap between mathematical logic and executable code.

Why it's important:
Developing these skills has allowed me to better organize my code and create reusable components. This modular approach is essential for scaling larger Python projects and maintaining a professional workflow.

i'm still yet to confirm if the modularization works here on github

### lists in python
Python Lists: Quick Summary

1. Definition

Lists are ordered, mutable (changeable) collections of items.
They are defined using square brackets [].
Example: fruits = ["apple", "banana", "cherry"]

2. Key Characteristic: Mutability

Unlike tuples, lists can be modified after creation.
You can change intermediate items: fruits[1] = "blueberry"

3. Common Operations

Accessing: Use index (e.g., fruits[0] for the first item, fruits[-1] for the last).
Adding:
.append(item): Adds to the end.
.insert(index, item): Adds at a specific position.
Removing:
.remove(item): Removes a specific value.
.pop(): Removes and returns the last item.

4. Versatility

Lists can store multiple data types at once (integers, strings, and even other lists).
Example: mixed_list = [1, "hello", 3.14]


### python tuples
Python Tuples: Quick Reference
1. Definition

Ordered and Immutable sequences.
Defined using parentheses ().
Example: coordinates = (10, 20)

2. Immutability

Once created, you cannot change, add, or remove elements.
my_tuple[0] = 5 will raise a TypeError.

3. Single-Item Tuples

Must include a trailing comma, otherwise Python treats it as a standard value (e.g., an integer or string).
Correct: single = (42,)
Incorrect: not_a_tuple = (42)

4. Operations

Indexing: Access items like lists: my_tuple[0].
Unpacking: Assign elements to variables in one step:
x, y = (10, 20)
Multiple Returns: Commonly used by functions to return more than one value.


### Python Sets: Summary Note
Definition:
A Set is an unordered collection of unique elements. Sets are written with curly braces {}.

Key Characteristics:

Unordered: The items do not have a defined order; they may appear in a different order every time you use them.
Unique: Duplicate elements are automatically removed.
Unindexed: You cannot access items by referring to an index (e.g., my_set[0] will raise an error).
Common Operations:

Creation:

my_set = {"apple", "banana", "cherry"}
 comment: Or using the constructor
numbers = set([1, 2, 2, 3]) # Result: {1, 2, 3}
Adding & Removing:

add("item"): Adds an element to the set.
remove("item"): Removes a specific element (raises error if not found).
Set Mathematics:

set1.union(set2): Combines all elements from both sets.
set1.intersection(set2): Returns only elements present in both sets.
set1.difference(set2): Returns elements in set1 that are NOT in set2.
Membership Testing:

"apple" in my_set: Returns True or False. This is extremely fast in sets compared to lists.

### Python Dictionaries: Summary Note
Definition:
A Dictionary is a collection of key-value pairs. It is used to store data values like a map or a real-world phone book.

Key Characteristics:

Key-Value Pairs: Every item has a key (the label) and a value (the data).
Mutable: You can change, add, or remove items after the dictionary is created.
Unique Keys: Each key must be unique. If you assign a new value to an existing key, the old value is overwritten.
Efficient: Finding a value by its key is extremely fast.
Common Operations:

Creation:

# Using curly braces
person = {"name": "Alice", "age": 25}
Accessing & Modifying:

person["name"]: Accesses the value associated with the key "name".
person["age"] = 26: Updates the value for an existing key.
person["city"] = "New York": Adds a new key-value pair.
Removing Items:

del person["age"]: Removes the key "age" and its value.
person.pop("name"): Removes the key and returns the value.
Useful Methods:

.keys(): Returns a list of all keys.
.values(): Returns a list of all values.
.items(): Returns a list of tuples (key, value), perfect for looping.
In your current Lab:
In contact_manager.py, you are using a Nested Dictionary. The contacts dictionary uses a string (the name) as a key, and another dictionary as the value:
contacts["Alice"] = {"phone": "123", "email": "alice@email.com"}
