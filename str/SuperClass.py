#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'zhen'

# Card超类和三个子类，这三个子类是Card的变种。两个实例变量直接由参数值设置，并通过初始化方法计算：


class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()


class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    def _points(self):
        return 1, 11


class FaceCard(Card):
    def _points(self):
        return 10, 10

cards = [AceCard('A', '♠'), NumberCard('2', '♠'), NumberCard('3', '♠'), ]


class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

Club, Diamond, Heart, Spade = Suit('Club', '♣'), Suit('Diamond', '♦'), Suit('Heart', '♥'), Suit('Spade', '♠')
cards = [AceCard('A', Spade), NumberCard('2', Spade), NumberCard('3', Spade), ]


def run():
    print "hello"
    print cards


if __name__ == "__main__":
    run()    