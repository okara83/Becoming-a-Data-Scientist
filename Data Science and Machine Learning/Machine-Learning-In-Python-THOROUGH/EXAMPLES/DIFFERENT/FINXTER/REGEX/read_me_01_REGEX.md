
* re.findall(pattern, string): Checks if the string matches the pattern and returns all occurrences of the matched pattern as a list of strings. 

* re.search(pattern, string): Checks if the string matches the regex pattern and returns only the first match as a match object. The match object is just that: an object that stores meta information about the match such as the matching position and the matched substring.

* re.match(pattern, string): Checks if any string prefix matches the regex pattern and returns a match object.

* re.fullmatch(pattern, string): Checks if the whole string matches the regex pattern and returns a match object.

* re.compile(pattern): Creates a regular expression object from the pattern to speed up the matching if you want to use the regex pattern multiple times.

* re.split(pattern, string): Splits the string wherever the pattern regex matches and returns a list of strings. For example, you can split a string into a list of words by using whitespace characters as separators.

* re.sub(pattern, repl, string): Replaces (substitutes) all occurrences of the regex pattern with the replacement string repl and return a new string