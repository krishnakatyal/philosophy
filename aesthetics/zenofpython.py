import sys
import os

"""
How pythonic is your code? 

Compute a Python score based on how close code is to the principles
given by the Zen of Python. Use this script as `python zenofpython.py file`
in which `file` is the file to be assessed for pythonic qualities.

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one—and preferably only one—obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea—let's do more of those!
"""

with open(sys.argv[1], "r") as file:
    score = 0 
    linecount = 0
    linelens = []
    for line in file:
        linelens.append(len(line))
        linecount += 1	
    score += sum(linelens)/linecount	
    
print(score)
