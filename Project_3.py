#
# Written by Brett Moolenschot
# Udacity Introduction to Programming Project 3

def poem_replace( poem , dictionary ):
    '''Will take a poem and a dictionary, and will return the poem with words found in the dictionary replaced with a corresponding value.'''
    split_string = poem.split("\n")
    modified_string = []
    for p in split_string:
        for q in dictionary:
            check = q in p
            if check == True:
                p = p.replace( q , "__" + str(dictionary[ q ]) + "__" )
        modified_string.append(p)

    return ("\n").join(modified_string)

def check_guess( modified_poem , dictionary , word , input ):
    '''Will check if an input word is correct for a position in the poem game.'''
    for p in dictionary:
        if input == p and dictionary[ input ] == word:
            return True

def poem_play( poem_name , poem , dictionary , hint ):
    '''Plays the poem game, takes a poem and a dictionary of words keyed to positions and cycles through to victory or defeat.'''
    print "\nTest your poetry skills! The goal is to replace each of the empty spaces with the correct word in these famous poems.\
            \nWatch out for capital letters.\
            \nGive it a go!\n"
    modified_poem = poem_replace( poem , dictionary )
    word = 1
    guess = 1

    while guess <= 6:
        if poem == modified_poem:
            print "Well done! Here's the whole poem:\n"
            print poem_name
            print "\n" + poem
            print "\nYou've won! Ten points to Gryffindor (or mayber Slytherin?)!"
            break
        if guess == 6:
            print "\nGame Over :("
            print "The poem is " + poem_name
            break

        if guess < 6:
            print "You have " + str(5 - (guess - 1) ) + " guesses remaining."
        if guess > 4:
            print hint
        print "\nHere's the poem:\n"
        print modified_poem
        print ""
        user_input = raw_input("Type in your (educated) guess for position " + str(word) + ": ")

        if check_guess( modified_poem , dictionary , word , user_input ) == True:
            print "\nCongratulations you have the correct word, you genius you!\n"
            modified_poem = modified_poem.replace( "__" + str(word) + "__" , user_input )
            word += 1
            guess = 1

        else:
            if guess < 5:
                print "\nI'm sorry! Try again!"
            guess += 1

def poem_game( poem1 , poem2 , poem3 ):
    '''Starts the whole poem game off giving multiple difficulty levels, selecting the appropriate poem and going for it.'''
    print "*** Welcome to PoemGame ***"
    repeat_play = "Yes"
    while repeat_play == "Yes":
        i = 0
        while i == 0:
            user_input = raw_input("\nPlease select difficulty: Easy, Medium or Hard: ")
            if user_input == "Easy":
                i += 1
                poem_name = poem1[0]
                poem = poem1[1]
                dictionary = poem1[2]
                hint = poem1[3]
                poem_play( poem_name , poem , dictionary , hint )

            if user_input == "Medium":
                i += 1
                poem_name = poem2[0]
                poem = poem2[1]
                dictionary = poem2[2]
                hint = poem2[3]
                poem_play( poem_name , poem , dictionary , hint )

            if user_input == "Hard":
                i += 1
                poem_name = poem3[0]
                poem = poem3[1]
                dictionary = poem3[2]
                hint = poem3[3]
                poem_play( poem_name , poem , dictionary , hint )
        repeat_play = raw_input("\nWould you like to play again? Yes/No: ")
        if repeat_play != "Yes" and repeat_play != "No":
            print "\nSorry you typed that wrong, can you try that again or the game will assume you don't want to play. Please type Yes or No, watch out for capitals."
            repeat_play = raw_input("\nWould you like to play again? Yes/No: ")
    print "Ok, good luck out there. Thanks for playing!"



poem1_name = "Trees by Joyce Kilmer"

poem1_body = "I think that I shall never see\
\nA poem lovely as a tree.\
\n \
\nA tree whose hungry mouth is prest\
\nAgainst the earth's sweet flowing breast;\
\n \
\nA tree that looks at God all day,\
\nAnd lifts her leafy arms to pray;\
\n \
\nA tree that may in summer wear\
\nA nest of robins in her hair;\
\n \
\nUpon whose bosom snow has lain;\
\nWho intimately lives with rain.\
\n \
\nPoems are made by fools like me,\
\nBut only God can make a tree.\
\n "

dictionary1 = { "tree" : 1 , "breast" : 2 , "pray" : 3 , "hair" : 4 , "rain" : 5 }

hint1 = "Hint: Think like the poet, be the poet, own the poem. Think weather, religion, female body parts and stuff like that. Good luck!"

poem1 = [ poem1_name , poem1_body , dictionary1 , hint1 ]

poem2_name = "The Road Not Taken by Robert Frost"

poem2_body = "Two roads diverged in a yellow wood,\
\nAnd sorry I could not travel both\
\nAnd be one traveler, long I stood\
\nAnd looked down one as far as I could\
\nTo where it bent in the undergrowth;\
\n \
\nThen took the other, as just as fair,\
\nAnd having perhaps the better claim,\
\nBecause it was grassy and wanted wear;\
\nThough as for that the passing there\
\nHad worn them really about the same,\
\n \
\nAnd both that morning equally lay\
\nIn leaves no step had trodden black.\
\nOh, I kept the first for another day!\
\nYet knowing how way leads on to way,\
\nI doubted if I should ever come back.\
\n \
\nI shall be telling this with a sigh\
\nSomewhere ages and ages hence:\
\nTwo roads diverged in a wood, and I-\
\nI took the one less traveled by,\
\nAnd that has made all the difference.\
\n "

dictionary2 = { "stood" : 1 , "looked" : 2 , "took" : 3 , "lay" : 4 , "come" : 5 }

hint2 = "Hint: These words are verbs having to do with movements of the body. Also look in context of the poem. Good luck!"

poem2 = [ poem2_name , poem2_body , dictionary2 , hint2 ]

poem3_name = "Sonnet 18 by William Shakespeare"

poem3_body = "Shall I compare thee to a summer's day?\
\nThou art more lovely and more temperate.\
\nRough winds do shake the darling buds of May,\
\nAnd Summer's lease has all to short a date.\
\nSometimes too hot the eye of Heaven shines,\
\nAnd often is his gold complexion dimmed;\
\nAnd every fair from fair sometime declines,\
\nBy chance, or nature's changing course, untrimmed;\
\nBut thy eternal summer shall not fade,\
\nNor lose possession of that fair thou ow'st,\
\nNor shall Death brag thou wand'rest in his shade,\
\nWhen in eternal lines to Time thou grow'st.\
\n  So long as men can breathe, or eyes can see,\
\n  So long lives this, and this gives life to thee."

dictionary3 = { "summer" : 1 , "day" : 2 , "temperate" : 3 , "winds" : 4 , "May" : 5 , "Summer" : 6 , "date" : 7 , "hot" : 8 , "fair" : 9 , "shade" : 10 , "Time" : 11 }

hint3 = "Hint: These words have to do with weather conditions and time related things. Good luck."

poem3 = [ poem3_name , poem3_body , dictionary3 , hint3 ]

poem_game( poem1 , poem2 , poem3 )
