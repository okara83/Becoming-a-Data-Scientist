"""
https://edabit.com/challenge/e69u7eJYnSz3kiLAn

Hash Juggling
Create a function that:

Creates a sha256 hash from a list of strings.
Sort the hash string, alphas first digits second, maintaining the original order of alphas and digits (e.g. "7a2f7fdf31a4b" would be sorted as "affdfab727314").
Returns a new sha256 hash from the sorted string.
Examples
hash_ops(["string1", "string2", "string3"]) ➞ "2d3b990149219819705bfe290571a9dcf5cf2a2528a2c711a57bd430ce32497f"

hash_ops(["quick", "brown", "fox"] ) ➞ "7a2f7fdf31a4b14dd4f67e5ca8da3dabd7eac825eac259682e43d7e477b3d378"

hash_ops(["i", "am", "not", "a", "crook"]) ➞ "d94ffa741e59d434b9e9e2ed32c2efc128238ba29eaa79cd0283d17a04a2d93f"
Notes
Remember to encode your strings.
"""
import hashlib
def hash_ops(lst):
    a = list(hashlib.sha256(''.join(lst).encode('utf-8')).hexdigest())
    sorted_a = sorted(a, key=str.isdigit)
    target = hashlib.sha256(''.join(sorted_a).encode('utf-8')).hexdigest()
    return target

#hash_ops(["string1", "string2", "string3"]) #➞ "2d3b990149219819705bfe290571a9dcf5cf2a2528a2c711a57bd430ce32497f"
hash_ops(["quick", "brown", "fox"] ) #➞ "7a2f7fdf31a4b14dd4f67e5ca8da3dabd7eac825eac259682e43d7e477b3d378"
#hash_ops(["i", "am", "not", "a", "crook"]) #➞ "d94ffa741e59d434b9e9e2ed32c2efc128238ba29eaa79cd0283d17a04a2d93f"