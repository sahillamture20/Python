'''
Evaluate values & variable =
- The bool() function allows you to evaluate any value, and give you True or False in return,

True / Truthy Value =
- Almost any value is evaluated to True if it has some sort of content.
- Any string is True, except empty strings.
- Any number is True, except 0.
- Any list, tuple, set, and dictionary are True, except empty ones.

False / Flasy Value = 
- In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0,
  and the value 'None', and of course the value 'False' evaluates to False.
- If you have a object created from the class having a __len__ function which returns 0 or False,
  then that object is evaluated as False.
'''