"""
https://edabit.com/challenge/jmZe7R4ibXkrQbogr     EXPERT--------
Validate Password
Write a regular expression that checks to see if a password is valid. For a password to be valid, it must meet the following requirments:

The password must contain at least one uppercase character.
The password must contain at least one lowercase character.
The password must contain at least one number.
The password must contain at least one special character ! ? * #
The password must be at least 8 characters in length.
Examples
"Password*12" ➞ True

"passWORD12!" ➞ True

"Pass" ➞ False
Notes
The lowercase char, uppercase char, special char, and number can appear at any part of the password.
You will only be writing a regular expression; do not write a function.
"""
import re

r = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!?*#]).{8,}'