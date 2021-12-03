#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 22:51:59 2021

@author: Andrew Killeen (drewkilleen@me.com)

This is a specific application of the common need to apply a grade to a test score
(i.e 95% is an A+). In my Glucose/Ketone Calculator app I wanted to provide a text
grade rather than just a numeric score. The bisect module does it nicely. Typically,
I see this achieved in Python with if-then-else but it's ugly, confusing, and
tedious to modify or extend. Some other languages would probably use a case statement
(not an option in Python) but it's still ugly.  I like this approach for several
reasons, but mostly because it's very Pythonic (two lists and index function).

Bisect returns an int index from 1 to len(grade_breakpoints), hence the -1 to provide
an index from 0 to 4 to select an element in the grades list in this example.
You can even mix float and int breakpoints.
  
Change the gki and rerun it to see what it returns for various gki values which
typically range from 2.9 (Super) to 7.5 (low) when someone is in ketosis.
A GKI of 9+ is not in ketosis.  Like golf scores, a lower gki is better. 
"""
"ljhgjhgjhgk"
# =============================================================================
# The Glucose / Ketone Index (GKI) runs from 0 to 9 for a person in Ketosis
# =============================================================================

gki = 4.5

# =============================================================================
# Method 1 - My preferred method
# =============================================================================
from bisect import bisect

grade = ""
grades = ("Doctor's Supervision Only!","Super","Moderate","Low","Not in Ketosis")
grade_breakpoints = (0,1,3,6,9)
grades_index = bisect(grade_breakpoints,gki)-1
grade = grades[grades_index]
print("Method 1: Your Ketosis Level is: ",grade)
    
# =============================================================================
# Method 2 - Note the use of Python's 'inf' infinite value.
#           This is the only time I've found a use for it, so cool!
# =============================================================================
grade = ""
score_grade = ((1, "Doctor's Supervision Only!"),
               (3, "Super",),
               (6, "Moderate"),
               (9,"Low"),
               (float('inf'),"Not in Ketosis"))
for score, grade in score_grade:
    if gki < score:
        print("Method 2: Your Ketosis Level is: ",grade)
        break
    
# =============================================================================
# Method 3 - The ugly standard solution, it looks like Basic FGS!
# =============================================================================
grade =""  
if gki >= 9:
    grade = "Not in Ketosis"
elif gki >=  6:
    grade = "Low"
elif gki >= 3:
    grade = "Moderate"
elif gki >= 1:
    grade = "Super"
else:
    grade = "Doctor's Supervision Only!" 
    
print("Method 3: Your Ketosis Level is: ",grade)