# Resubmission for Udacity Introduction to Programming Project 3
# Brett Moolenschot

def poem_replace( poem ):
    """Return poem with blank elements to be filled.

    Looks into a list of answers contains within a correctly formmatted poem and returns the body of the poem
    with the answer words replaced with __i__, i representing the index of the answer within the answer list.

    Args:
        poem: This must be a dictionary with the following two keys below:
            poem["body"]: The body of the poem in the form of a string.
            poem["answers"]: A list of answers to be inserted in the poem.

    Returns:
        A string containing the body of the original poem with answer spaces inserted.
    """
    modified_poem = poem["body"]
    for entry in poem["answers"]:
        check = entry in poem["body"]
        if check == True:
            modified_poem = modified_poem.replace( entry , "__" + str( poem["answers"].index( entry ) + 1 ) + "__")
    return modified_poem

def answer_insert( modified_poem , answer_list , answer ):
    """Return modified poem with correct answer reinserted.

    Recieves a correct answer, checks for the index of the answer with the answer list,
    reinserts it into into a poem modified by the poem_replace function and returns the newly modified poem.
    Prints prompts depending on whether the poem is completely solved or not.

    Args:
        modified_poem: The original poem modified by the poem_replace fucntion.
        answer_list: The list of answers found in poem["answers"].
        answer: The correct answer supplied by the user.

    Returns:
        A string containing the updated modified poem.
        Prints a Congratulations if the poem is completely solved, else a prompt to the next answer.
    """
    modified_poem = modified_poem.replace( "__" + str( answer_list.index( answer ) + 1 ) + "__" , answer )
    if len( answer_list ) == ( answer_list.index( answer ) + 1 ):
        print "\nYou've solved the puzzle! Congratulations."
    else:
        print "\n***You've got it! On to the next one:"
    return modified_poem

def poem_play( poem ):
    """Return the result of poem game.

    Executes the majority of the user interaction for the poem game against a single poem and returns a win or loss result.

    Args:
        poem: A correctly formatted dictionary containing poem["answers"] and poem["body"]

    Returns:
        A true or false result depending on the outcome of the game.
    """
    modified_poem = poem_replace( poem )
    for word in poem["answers"]:
        max_guess = 5
        guess = 0

        while guess < max_guess:
            print "\nYou have " + str( max_guess - guess ) + " guesses remaining."
            print modified_poem
            if guess == max_guess - 1:
                print poem[ "hint" ]

            user_input = raw_input("\nPlease enter your guess here: ")
            if user_input == word:
                modified_poem = answer_insert( modified_poem , poem["answers"] , user_input )
                break
            guess += 1
        if guess == max_guess:
            return False
    if modified_poem == poem["body"]:
        return True

def play_check( play ):
    """Return a false result if an incorrect value has been entered for a replay query."""
    if play == "yes" or play == "no":
        if play == "no":
            print "\nSee you soon! (Hopefully)"
        if play == "yes":
            print "\nHere we go!"
    else:
        return False

def poem_game_run( problems ):
    """Prompt user difficulty selection, initiate the poetry game and query a replay once game is complete.

    Executes the poetry game from the highest level.

    Args:
        problems: A list of poems available to play with each poem being a dictionary containing the following structure:
                    poem1 = { "title" : poem1_name , "level" : "Easy" , "body" : poem1_body , "answers" : answers1 , "hint" : hint1 }

    Returns:
        The poetry game and a replay query following a win or lost.
    """
    print "*** POEM GAME ***" + "\n\nFill in gaps in these famous poems and prove your poetry skills are the best. Hope you are ready!"
    play = "yes"
    while play == "yes":
        poem_select = "Unspecified"
        while poem_select == "Unspecified":
            level = raw_input("\nPlease select your difficulty (Easy, Medium, Hard): ").lower()
            for poem in problems:
                if poem["level"] == level:
                    poem_select = poem

        result = poem_play( poem_select )
        if result == False:
            print "\nIt seems you've lost. The poem is:" + poem_select["title"] + poem_select["body"]
        if result == True:
            print "\nYou're a genius! The poem is:" + poem_select["title"] + poem_select["body"]
        play = raw_input("\nWould you like to play again (Yes/No): ").lower()
        while play_check( play ) == False:
            play = raw_input("\nPlease insert a correct option. Yes/No: ").lower()

poem1_name = "\n\nTrees by Joyce Kilmer"
poem1_body = "\n\nI think that I shall never see\
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

answers1 = ( "tree" , "breast" , "pray" , "hair" , "rain" )
hint1 = "\nHint: Think like the poet, be the poet, own the poem. Think weather, religion, female body parts and stuff like that. Good luck!"
poem1 = { "title" : poem1_name , "level" : "easy" , "body" : poem1_body , "answers" : answers1 , "hint" : hint1 }

poem2_name = "\n\nThe Road Not Taken by Robert Frost"
poem2_body = "\n\nTwo roads diverged in a yellow wood,\
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
answers2 = [ "stood" , "looked" , "took" , "lay" , "come" ]
hint2 = "\nHint: These words are verbs having to do with movements of the body. Also look in context of the poem. Good luck!"
poem2 = { "title" : poem2_name , "level" : "medium" , "body" : poem2_body , "answers" : answers2 , "hint" : hint2 }

poem3_name = "\n\nSonnet 18 by William Shakespeare"
poem3_body = "\n\nShall I compare thee to a summer's day?\
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
answers3 = [ "summer" , "day" , "temperate" , "winds" , "May" , "Summer" , "date" , "hot" , "fair" , "shade" , "Time" ]
hint3 = "\nHint: These words have to do with weather conditions and time related things. Good luck."
poem3 = { "title" : poem3_name , "level" : "hard" , "body" : poem3_body , "answers" : answers3 , "hint" : hint3 }

problems = [ poem1 , poem2 , poem3 ]

poem_game_run( problems )
