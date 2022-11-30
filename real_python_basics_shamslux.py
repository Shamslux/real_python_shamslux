""" 
HELLO, WORLD! - FIRST PART OF COURSE BASED ON THE BOOK "PYTHON BASICS", FROM REAL PYTHON GROUP

IMPORTANT! - Some examples I did take from the book, but others I've created by myself, playing with the book's own examples
trying to create mine and also having fun while doing it!

About me: Shamslux, from Brazil, Junior BI Analyst and Data Engineer! =)
My passion for human languages is part of my love for computer languages, hehe.
Human languages we can communicate if you are wishing to conctact me:
Portuguese, French, Esperanto, Spanish (the ones probably I can use and understand better)
Modern Hebrew and Arabic (I will struggle, but we can try to chat in them)

Fun fact! -> I was a Middle/High-School teacher about 1 yr ago! =O
I had no previous background in Data Science, hihi!

Feel free to contact me on GitHub and to take this code to help yourself too!
""" 

# And so, a new programmer is born! =P

print("Hello, world!")

# Let's create an error to check how the syntax error pointer is coming to rescue us!
#print("Hello, world!) - Commented to avoid the quotation marks problem!

# Now, let's create a problem to create a runtime error.

print(Hello, world) 

""" 
REVIEW 1 EXERCICES!  

1 - Write a script that IDLE won’t let you run because it has a syntax
error.

2 - Write a script that only crashes your program once it is already
running because it has a run-time error.
"""

# My solutions!

# 1 OK!

#print("Hello, user!) - Commented to avoid the quotation marks problem!

# 2 OK!

priint("Hello, user!")

# Starting to learn about VARIABLES!

phrase = "Hello, world!"
print(phrase)

""" 
REVIEW 2 EXERCICES!  

1 - Using the interactive window, display some text on the screen by
using the print() function.

2 - Using the interactive window, display a string of text by saving the
string to a variable, then reference the string in a print() function
using the variable name.

3 - Do each of the first two exercises again by first saving your code in
a script and running it
"""

# 1 and 2 OK!

text_to_display = "Hi, I am learning Python!"
print(text_to_display)

# 3 - I am using this single script to keep all basic data from the course.

# Learning how to INSPECT variables in Python!

phrase = "Hello, world!"
phrase

# Discovering how INSPECT can help observe the difference between two "similar" data types

x = 2
y = "2"

print(x)
print(y)

x
y

# Inspecting a built-in funcion!

print

# Result: <built-in function print>

# Learning about comments! (Although I was already able to create them, hehe)

# This is a sample of the borning of a new progammer!
# Probably I am typing more in the commentaries than the final code! =P
# Commentaries are useful to allow us remember what we did in months ago after creating a code, hahahaha!

phrase = "Hello, world!"
print(phrase) # Adding  a  in  line  comment  according  to  PEP8  good  practices  !!  (Two  spaces  between  words!)

# Checking "data types" (classes) with the function type()

type("Hello, world")

# Using len() to check the lenght of a string.

phrase = "I am now learning about strings"
length_phrase = len(phrase)
length_phrase

# Adjusting multiline strings to be according to PEP8 guide (lines no bigger than 79 characters)

paragraph = "This planet has - or rather had - a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."

print(paragraph)

# It is possible to use backslashes (\) to handle with the big string or...

paragraph = """This planet has - or rather had - a problem, which was
this: most of the people living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concerned with the movements of small
green pieces of paper, which is odd because on the whole it wasn't
the small green pieces of paper that were unhappy."""
print(paragraph)

# It is also possible to use triple quotes ("""). The difference is
# that the first method has a output with one single line. The second
# method preserves the black spaces and they are kept in the output!

""" 
REVIEW 3 EXERCICES!  

1 - Print a string that uses double quotation marks inside the string.

2 - Print a string that uses an apostrophe inside the string.

3 - Print a string that spans multiple lines, with whitespace preserved.

4 - Print a string that is coded on multiple lines but displays on a single line.
"""

# 1 OK!

string_double_quotes = 'This is an example of a "double quotted string"'

print(string_double_quotes)

# 2 OK!

string_apostrophe = "Now I can use an apostrophe in Lucius' Bar"

print(string_apostrophe)

# 3 OK!

string_multiline_whitespace = """I am testing now how to preserve       
the whitespaces                                                    """

print(string_multiline_whitespace)

# 4 OK!

string_with_backslashes = "Lorem ipsum dolor sit amet, consectetur adipiscing\
elit. Sed lacinia vehicula risus, sit amet finibus tortor venenatis non. Ut\
lacus neque, venenatis quis eros vel, cursus elementum risus. Ut mollis ex\
blandit turpis finibus iaculis. Nunc sed facilisis tortor. Cras sed quam\
vel lacus tincidunt molestie vitae nec felis. Nam pulvinar tortor mi, eu\
vestibulum magna porta vel. In mollis interdum erat, eget auctor enim porttitor at."

print(string_with_backslashes)

# String concatenation

evolution1 = "Abra"
evolution2 = "Kadabra"
evolution3 = "Alakazam"

pokemon_cycle = evolution1 + "->" + evolution2 + "->" + evolution3

print(pokemon_cycle) # Pokémon  !  Legendary  strategy  game  !  It  made  me  want  to  learn  how  to  program  in  the  past  !  =P

# Indexing strings

country = "Brazil"

country[0]

country[-1]

# Slicing strings

country = "Brazil"

country[0:3]

""" 
REVIEW 4 EXERCICES!  

1 - Create a string and print its length using the len() function.

2 - Create two strings, concatenate them, and print the resulting
string.

3 - Create two strings and use concatenation to add a space inbetween them. Then print the result.

4 - Print the string "zing" by using slice notation on the string
"bazinga" to specify the correct range of characters.
"""
# 1 OK!

country = "Brazil"

print(len(country))

# 2 OK!

word1 = "sand"
word2 = "storm"

joining_words = word1 + word2

print(joining_words)

# 3 OK!

word1 = "Hey,"
word2 = "friend!"

joining_words = word1 + " " + word2

print(joining_words)

# 4 OK!

given_word = "bazinga"

given_word[2:6]

# String Methods! 

name = "Stan Lee"

print(name.lower()) # .lower()  forces  all  letters  to  become  lower  case

print(name.upper()) # .upper()  forces  all  letters  to  become  upper  case

name_whitespaces = "    Stan Lee    "
name_whitespaces

name_whitespaces.strip() # In  this  case  it  is  better  to  inspect  than  to  print!

pokemon = "Pikachu"

pokemon.startswith("Pi")
pokemon.endswith("chu")

""" 
REVIEW 5 EXERCICES!  

1 - Write a script that converts the following strings to lowercase:
 "Animals", "Badger", "Honey Bee", "Honeybadger". Print each lowercase
string on a separate line.

2 - Repeat Exercise 1, but convert each string to uppercase instead of
lowercase.

3 - Write a script that removes whitespace from the following strings:
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
Print out the strings with the whitespace removed

4 - Write a script that prints out the result of .startswith("be") on each
of the following strings:
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

5 - Using the same four strings from Exercise 4, write a script that
uses string methods to alter each string so that .startswith("be")
returns True for all of them.
"""

# 1 OK!

string_a = "Animals"
string_b = "Badger"
string_c = "Honey Bee"
string_d = "Honeybadger"

print(string_a.lower())
print(string_b.lower())
print(string_c.lower())
print(string_d.lower())

print(string_a.lower(), string_b.lower(), string_c.lower(), string_d.lower()) # I  thought  it  could  work  then  it  really  worked  !!  =D

# 2 OK!
 
string_a = "Animals"
string_b = "Badger"
string_c = "Honey Bee"
string_d = "Honeybadger"

print(string_a.upper(), string_b.upper(), string_c.upper(), string_d.upper())

# 3 OK!

string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "

string1.lstrip() 
string2.rstrip()
string3.strip()

# 4 OK!

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

print(string1.startswith("be")) 
print(string2.startswith("be")) # Only  this  one  is  TRUE  because  the  method  is  case  sensitive  !!!
print(string3.startswith("be"))
print(string4.startswith("be"))

# 5 OK!

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

string1_new = string1.lower()
string3_new = string3[0:2].lower() + string2[2:]
string4_new = string4.lower()

print(string1_new.startswith("be"))
print(string2.startswith("be"))
print(string3_new.startswith("be"))
print(string3_new.startswith("be"))












