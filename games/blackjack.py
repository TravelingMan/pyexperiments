#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Blackjack
Because everyone needs to code a card game
"""

from random import randint


class Blackjack():
    def __init__(self):
        self.deck = []
        self.suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

    def make_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))

    def pull_card(self):
        return self.deck.pop(randint(0, len(self.deck) - 1))


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self, dealer_start=True):
        print(f'\n{self.name}')
        print('==============')
        for i in range(len(self.hand)):
            if self.name == 'Dealer' and i == 0 and dealer_start:
                print("- of -")  # Hide first card
            else:
                card = self.hand[i]
                print(f'{card[0]} of {card[1]}')

    def calc_hand(self, dealer_start=True):
        total = 0


game = Blackjack()
game.make_deck()

name_in = input('What is your name? ')
player = Player(name_in)
dealer = Player('Dealer')

for i in range(2):
    player.add_card(game.pull_card())
    dealer.add_card(game.pull_card())

player.show_hand()
dealer.show_hand()