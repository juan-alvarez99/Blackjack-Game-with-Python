"""
Portfolio Repository
Created by: Juan Alvarez
Date: 04.12.2022
Github: https://github.com/juan-alvarez99
Linkedin: https://www.linkedin.com/in/juan-alv/
========================================================================================================
========================================================================================================
This project consists in a simple version of the Atlanta Classic Blackjack using Python basic programming
This are the rules:
    - user vs computer: the player that gets closer to 21 points wins
    - J, Q and K score 10 points
    - A can score 11 points if the total points in someone's hand is less or equal to 21, otherwise it scores 1 point
    - The rest of the deck score as many points as the number of the card (2=2, 3=3,..., 10=10)
    - In this casino we use several decks to avoid card-counting: the probability of dealing a certain card is always the same, no matter how many times had it been dealed before
    - Firstly, two cards are dealed to each player, the user can only see the first card of the computer's hand
    - The user can ask to be dealed as many cards as he wants to increase his/her hand
    - If the user goes over 21, the game is over, regardless of what the computer has
    - When the user has finished is computer's turn. 
    - The computer is only going to ask for another card when it's below 17 points
    - BLACKJACK: is the best hand of the game. It can only be score with the first two cards dealed at the beginning of the game. This cards should be: A + (10/J/Q/K)

Did you like it? You can play as many times as you want!
Enjoy!

========================================================================================================
========================================================================================================
"""

import random
from art import logo
from art import ascii_cards


cards = {'A':11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10}

def deal_card():
    """
    Return a random card from the deck
    """
    # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(list(cards.keys()))


def print_card(hand):
    """
    Print all the cards in a hand
    """
    for card in hand:
        print(ascii_cards[card], end = " ")
    print("") # End of line


def count_hand_value(hand):
    """
    Takes a deck of cards and return the score calculated from the cards.
    Return 0 when the hand it's a Blackjack
    """
    value = 0

    for card in hand:
        if type(card) is int:
            value += card
        elif card == 'A':
            value += 11
        else:
            value += 10

    # If the value exceeds 21, aces worth 1 point instead of 11
    if value > 21:
        value -= 10*hand.count('A')

    # If the hand is a Blackjack return 0
    elif len(hand) == 2 and value == 21:
        value = 0
    return value


def final_result(user_score, computer_score):
    if user_score > 21:
        print("You went over. You lose!")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif user_score == computer_score:
        print("It's a draw!")
    elif computer_score == 0:
        print("Computer has a Blackjack. You lose!")
    elif user_score == 0:
        print("You have a Blackjack. You win!")
    elif user_score > computer_score:
        print("You score higher than the computer. You win!")
    else:
        print("Computer's score is better than yours. You lose!")


def blackjack():

    print(logo)

    user = {}
    computer = {}

    # initial deal
    user["hand"] = [deal_card(), deal_card()]
    computer["hand"] = [deal_card(), deal_card()]

    # User's turn
    end_users_turn = False
    while not end_users_turn:
        user["score"] = count_hand_value(user["hand"])

        print_card(user["hand"])
        print(f"\tYour hand is {user['hand']}, current score = {user['score']}")
        print(f"\tComputer's first card: {computer['hand'][0]}")

        if user["score"] > 21 or user["score"] == 0:
            end_users_turn = True

        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if another_card == 'y':
                user["hand"].append(deal_card())
            else:
                end_users_turn = True


    # Computer's turn
    computer["score"] = count_hand_value(computer["hand"])

    if user["score"] <= 21:
        while computer["score"] < 17 or computer["score"] == 0:
            computer["hand"].append(deal_card())
            computer["score"] = count_hand_value(computer["hand"])

    # Show the final result
    print_card(user["hand"])
    print(f"\tYour final hand is {user['hand']}, final score = {user['score']}")
    
    print_card(computer["hand"])
    print(f"\tComputer's final hand {computer['hand']}, final score: {computer['score']}")

    # Show who wins
    final_result(user["score"], computer["score"])
        


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    blackjack()

# End of the program
print("See you soon!")


