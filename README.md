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

