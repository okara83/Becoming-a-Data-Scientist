Here are the most important regex operators:

. The wild-card operator (‘dot’) matches any character in a string except the newline character ‘\n’. For example, the regex ‘…’ matches all words with three characters such as ‘abc’, ‘cat’, and ‘dog’.  

* The zero-or-more asterisk operator matches an arbitrary number of occurrences (including zero occurrences) of the immediately preceding regex. For example, the regex ‘cat*’ matches the strings ‘ca’, ‘cat’, ‘catt’, ‘cattt’, and ‘catttttttt’. 

? The zero-or-one operator matches (as the name suggests) either zero or one occurrences of the immediately preceding regex. For example, the regex ‘cat?’ matches both strings ‘ca’ and ‘cat’ — but not ‘catt’, ‘cattt’, and ‘catttttttt’. 

+ The at-least-one operator matches one or more occurrences of the immediately preceding regex. For example, the regex ‘cat+’ does not match the string ‘ca’ but matches all strings with at least one trailing character ‘t’ such as ‘cat’, ‘catt’, and ‘cattt’. 

^ The start-of-string operator matches the beginning of a string. For example, the regex ‘^p’ would match the strings ‘python’ and ‘programming’ but not ‘lisp’ and ‘spying’ where the character ‘p’ does not occur at the start of the string.

$ The end-of-string operator matches the end of a string. For example, the regex ‘py$’ would match the strings ‘main.py’ and ‘pypy’ but not the strings ‘python’ and ‘pypi’. 

A|B The OR operator matches either the regex A or the regex B. Note that the intuition is quite different from the standard interpretation of the or operator that can also satisfy both conditions. For example, the regex ‘(hello)|(hi)’ matches strings ‘hello world’ and ‘hi python’. It wouldn’t make sense to try to match both of them at the same time.

AB  The AND operator matches first the regex A and second the regex B, in this sequence. We’ve already seen it trivially in the regex ‘ca’ that matches first regex ‘c’ and second regex ‘a’. 