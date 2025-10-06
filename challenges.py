def add_chocolate(shopping_list: list):
    """My housemate is a real health-nut, but I like chocolate. This function 
    adds the string "chocolate" to any list it receives, and returns the 
    modified list. That way our shopping list is always correct.

    Arguments:
        - shopping_list: a list of strings

    Returns:
        - the same list, with the string "chocolate" added to the end
    """
    shopping_list.append("chocolate")
    return shopping_list
shopping_list = []
print(add_chocolate(shopping_list))



def lou_bega(lyrics_list: list):
    """This function accepts a list of strings and adds the words 
    "A little bit of " to the front of each.
    
    Arguments:
        - lyrics_list: a list of strings
    
    Returns:
        - the same list, but each string now has "A little bit of " 
        prepended to it.

    Example input: 
        [
            "Monica in my life", 
            "Erica by my side", 
            "Rita's all I need"
        ]
        
    Example output: 
        [
            "A little bit of Monica in my life", 
            "A little bit of Erica by my side", 
            "A little bit of Rita's all I need"
        ]
 
       """
    #option 1
    # for i, lyric in enumerate(lyrics_list):
    #     lyrics_list[i] = "A little bit of " + lyric 
    # return lyrics_list
    
    #option 2
    # new_list = [] # create empty list
    # for lyric in lyrics_list: # loop item in lyrics list
    #     lyric = "A little bit of " + lyric # existing lyric = "A little bit of + "
    #     new_list.append(lyric)
    # return new_list

    # option 3 - for and return MUST be the same indentation!!!!!!!
    new_list = []
    for lyric in lyrics_list:
        new_lyric = ("A little bit of " + lyric)
        new_list.append(new_lyric)
    return new_list 

    # lyrics_list = [
    #         "Monica in my life",  
    #         "Erica by my side", 
    #         "Rita's all I need"
    #     ]
    
# for lyrics in lyrics_list:
#  print(f"A little bit of {lyrics}")



#     for each_lyrics in lyrics_list:
#         print(string, each_lyrics)
#     return lyrics_list

# string="A little bit of "
# result = lou_bega(string)
# print(result)

# string = "A little bit of"
# lyrics_list = ["Monica in my life", "Erica by my side", "Rita's all I need"]
# for lyrics in lyrics_list:
#     print(string, lyrics)


def assemble_guest_list():
    """This function repeatedly prompts the user for the name of a dinner guest.
    Each string the user supplies is added to a list. If/when the user hits 
    "Enter" without typing anything, the function stops asking and 
    returns the list.
    
    Arguments: None!
    
    Returns:
        - a list of strings supplied by the user
    """
    
    guest_list = []
    name = input("What is the dinner guest name?: ")
    while name != "":
        guest_list.append(name)
        name = input("What is the dinner guest name?: ")
    return guest_list

    # while name == input("What is the dinner guest name?: "):
    #    guest_list = guest_list.append(name)
    #    name = input("What is the dinner guest name?: ")
    # while name == "":
    #     return guest_list
    
#Make an empty list called guest_list
#Ask the user to type a guest name

#While the user typed something (not blank):
#    Add that name to guest_list
#    Ask the user for another guest name

#When the user presses Enter without typing anything:
#    Stop asking
#Return the guest_list


def is_prime(some_number: int): # A bit trickier!
    """This function tests to see if the input is a prime number.
    Whenever a prime number is divided by an integer larger than 1 and smaller
    than itself, the result includes a remainder.

    NOTE: The lowest prime number is 2. 1 and 0 are not prime.
    
    Arguments:
        - some_number: an integer to be tested for prime-ness

    Returns:
        - a boolean representing whether or not some_number is prime
    """

    pass 
    
    # Hint: 
    #   int(1.5) == 1.0

    if some_number < 2:
        return False
    if some_number ==2:
        return True
    for i in range (2, some_number): # range = between 2 and the number up to (not including some_number). Range does not include the endpoint.
        if (some_number % i ==0): # if the number divides by any number starting from 2 but 1 less than the some_number and there is no remainder its not a prime number.
            return False
    return True
