#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# Card 类有一个超类级别的初始化函数用于各子类

class Card:
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

class NumberCard(Card):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)

class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__("A", suit, 1, 11)

class FaceCard(Card):
    def __init__(self, rank, suit):
        super().__init__({11:'J',12:'Q',13:'K'}[rank],suit,10,10)


def card2(rank, suit):
    if rank == 1:
        return AceCard('A',suit)
    elif 2<= rank <11:
        return NumberCard(str(rank),suit)
    else:
        name = {11:'J', 12,'Q', 13:'K'}[rank]
        return FaceCard(name,suit)

deck = [card(rank,suit) for rank in range(1,14) for suit in (Club, Diamond, Heart, Spade)]

def card10(rank,suit):
    if rank == 1:
        return AceCard(rank, suit)
    elif 2<= rank < 11:
        return NumberCard(rank, suit)
    elif 11<= rank <14:
        return FaceCard(rank,suit)
    else:
        raise Exception ("Rank out of range")



def run():
    print "hello"


if __name__ == "__main__":
    run()
    card10(12,'Q')