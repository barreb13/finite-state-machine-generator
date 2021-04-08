# Project Title
Assignment 5: Finite-State-Machine Generator

Author: Brent Barrese

# Description
This is a Finite-State-Machine generator program that is written in Python 3. It is a generator program that is used in other, more specific Finite-State-Machine Python programs. This example is used with a flaoting point FSM as well as an hours of service FSM. The program outputs to standard output and can be redirected at the user's choice. A couple of ways to use this are to print to an output file or to redirect to a cpp file and then compile that c++ program. This program will help generate a C++ program that compiles with no errors.

# How To Use
To use this machine, you will need to run it with another FSM executable Python program. The programs need to be in the same directory. Another FSM program written in Python will import fsm.py. 

Example of how to run this:

*./hos.py > hosOutput.txt*

# Expectations
It is expected that the Python FSM description file such as "hos.py" or "floatingPoint.py" will be in the same directory as fsm.py. 

# Reflection
This was a very interesting and unique program to work with. It was interesting to see what is possible with Python and generating C++ code that compiles correctly. The cost savings are significant and I am sure will add up over time since you only need to write the fsm.py one time and then the generator programs to run it.

I wasn't sure if I was going to get C++ code that compiles, but I was eventually able to get it and run it. It does compile and run. I was able to give it input and change states.

# References Used 
Professor Bernstein's Lecture

Professor Bernstein's Office Hours

https://stackoverflow.com/questions/3182183/how-to-create-a-list-of-objects 

https://www.geeksforgeeks.org/declare-an-empty-list-in-python/ 
