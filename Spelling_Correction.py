#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1

def edit_distance(s,t):
    distance = 0
    first_string = list(s)
    second_string = list(t)
    while len(first_string) != len(second_string):
        if len(first_string) > len(second_string):
            if first_string[0] == second_string[0] or first_string[0].capitalize() == second_string[0].capitalize():
                del first_string[-1]
                distance += 1
            else:
                del first_string[0]
                distance += 1
        elif first_string[0] == second_string[0] or first_string[0].capitalize() == second_string[0].capitalize():
            del second_string[-1]
            distance += 1
        else:
            del second_string[0]
            distance += 1
    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            first_string[i] = second_string[i]
            distance += 1
    return distance



#For example:

# Delete the 'a'
print edit_distance('audacity', 'udacity')
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
print edit_distance('audacity', 'Udacity')
#>>> 2

# Five replacements
print edit_distance('peter', 'sarah')
#>>> 5

# One deletion
print edit_distance('pete', 'peter')
#>>> 1
