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

# Learning how to receive data from a user

input()

prompt = "Hey, what's up? "
user_input = input(prompt)

print("You said:", user_input)

# NEED TO OVERWRITE THE CODE FROM THIS POINT BACKWARDS, BECAUSE
# FORMATING ISSUES!

""" 
REVIEW 6 EXERCICES! 

1 - Write a script that takes input from the user 
and displays that input back

2 - Write a script that takes input from the user and displays the input
in lowercase.

3 - Write a script that takes input from the user and displays 
the number of characters inputted.
"""

# 1 OK!

input("Hi there! Type something here, then I will show ya! -> ")

# 2 OK!

user_lower_word = input("Type here a whole upper case word and then I am going to convert it to lower case -> ")

print("You've type: ", user_lower_word)
print("Look how it becomes in lower case!")
print("Here it is! ->", user_lower_word.lower())

# 3 OK!

user_length_word = input("Hello! I can count the lenght of any word you type! Type it! -> ")

print("The lenght of the word is", len(user_length_word))

# CHALLENGE (write more at home)

country_by_user = input("Hello! Type the name of a country and I am going to answer back to you its first letter! ")

print("The first letter is", country_by_user[0:1].upper())

# Converting string to number

num = input("Enter a number to be doubled: ") # The  input  result  will  always  be  a  string  !!!
doubled_num = float(num) * 2 # Since  the  prompt  did  not  specified  we  convert  to  float(),  but  we  could  convert  to  int()
print(doubled_num)

# Converting number to string

total_pancakes = 10
print("I'm going to eat " + str(total_pancakes) + " pancakes!")

# Another example with an arithmetic expression

total_pancakes = 10
eaten_pancakes = 5
print("Now, only " + str(total_pancakes - eaten_pancakes) + " pancakes left")

""" 
REVIEW 7 EXERCICES!  
  
1 - Create a string containing an integer, then convert that string into
an actual integer object using int(). Test that your new object is
a number by multiplying it by another number and displaying the
result.

2 - Repeat the previous exercise, but use a floating-point number and
float()

3 - Create a string object and an integer object, then display 
them sideby-side with a single print statement by using the str() function.

4 - Write a script that gets two numbers from the user using the
input() function twice, multiplies the numbers together, and
displays the result. If the user enters 2 and 4, your program should
print the following text:
The product of 2 and 4 is 8.0.
"""

# 1 OK!

string_num = '2'

int_string_num = int(string_num)

type(int_string_num)

print(int_string_num)

# 2 OK!

string_num = '4.5'

float_string_num = float(string_num)

type(float_string_num)

print(float_string_num)

# 3 OK!

a_string = 'Hello, I am the number '
a_integer = 1

print(a_string + str(a_integer))

# 4 OK!

num1 = input('Write a integer number here -> ')
num2 = input('Write another integer number here -> ')

calculation = int(num1) * int(num2)

print('The product of', num1, 'and', num2, 'is', float(calculation))

# F-Strings (Formatted String Literals)

name = 'Zaphod'
heads = 2
arms = 3

print(f"{name} has {heads} heads and {arms} arms!")

""" 
REVIEW 8 EXERCICES!  
  
1 - Create a float object named weight with the value 0.2, and create
a string object named animal with the value "newt". Then use these
objects to print the following string using only string concatenation:
0.2 kg is the weight of the newt.

2 - Display the same string by using the .format() method and empty
{} place-holders.

3 - Display the same string using an f-string
"""

# 1 OK!

ob_float = 0.2
animal = "newt"

print(str(ob_float), "is the weight of the", animal)

# 2 OK!

ob_float = 0.2
animal = "newt"

print("{} is the weight of the {}".format(ob_float, animal))

# 3 OK!

ob_float = 0.2
animal = "newt"

print(f"{ob_float} is the weight of the {animal}")

# Using .find() string method

phrase = "the surprise is in here somewhere"
phrase.find("surprise")

# Using the string method .replace()

my_story = "I'm telling you the truth; nothing but the truth!"
my_story.replace("the truth", "lies")

""" 
REVIEW 9 EXERCICES!  
  
1 - In one line of code, display the result of trying to .find() 
the substring "a" in the string "AAA". The result should be -1.

2 - Replace every occurrence of the character "s" with "x" in the string
"Somebody said something to Samantha.".

3 - Write and test a script that accepts user input using the input()
function and displays the result of trying to .find() a particular
letter in that input.
"""

# 1 OK!

print("AAA".find("a"))

# 2 OK!

phrase = "Somebody said something to Samantha"
new_phrase = phrase.replace("S", "x")
new_phrase_2 = new_phrase.replace("s", "x")

print(new_phrase_2)

# 3 OK!

user_input = input("Write something here! ")

print(user_input.find("a"))

# Challenge - Turn Your User Into a L33t H4x0r

"""
Write a script called translate.py that asks the user for some input
with the following prompt: Enter some text:. Then use the .replace()
method to convert the text entered by the user into “leetspeak” by making the following changes to lower-case letters:

• The letter a becomes 4
• The letter b becomes 8
• The letter e becomes 3
• The letter l becomes 1
• The letter o becomes 0
• The letter s becomes 5
• The letter t becomes 7

Your program should then display the resulting string as output. Below is a sample run of the program:
Enter some text: I like to eat eggs and spam.
I 1ik3 70 347 3gg5 4nd 5p4m.
"""

# Translate.py OK!

text = input("Hi there! Write some text here and it will be translated to 'leetspeak'! -> ")

l_a = text.replace("a", "4")
text_phase_2 = l_a.replace("A", "4")
l_b = text_phase_2.replace("b", "8")
text_phase_3 = l_b.replace("B", "8")
l_e = text_phase_3.replace("e", "3")
text_phase_4 = l_e.replace("E", "3")
l_l = text_phase_4.replace("l", "1")
text_phase_5 = l_l.replace("L", "1")
l_o = text_phase_5.replace("o", "0")
text_phase_6 = l_o.replace("O", "0")
l_s = text_phase_6.replace("s", "5")
text_phase_7 = l_s.replace("S", "5")
l_t = text_phase_7.replace("t", "7")
text_final_phase = l_t.replace("T", "7")

print(f"Your text, in 'leetspeak', has become like that: {text_final_phase}")

""" 
REVIEW 10 EXERCICES!  
  
1 - Write a script that creates the two variables, num1 and num2. Both
num1 and num2 should be assigned the integer literal 25,000,000,
one written with underscored and one without. Print num1 and num2
on two separate lines.

2 - Write a script that assigns the floating-point literal 175000.0 to the
variable num using exponential notation, and then prints num in the
interactive window.

3 - In IDLE’s interactive window, try and find the smallest exponent N
so that 2e<N>, where <N> is replaced with your number, returns inf.
"""

# 1 OK!

num1 = 25000000
num2 = 25_000_000

print(num1)
print(num2)

# 2 OK!

num = 175e4

print(num)

# 3 OK!

print(2e400)
