#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')
#  一副牌有52张牌，每一张属于4种花色的一个和13个等级的一个。
#  4种花色是黑桃（Spades），红心（Hearts），方块（Diamonds），梅花（Clubs），
#  以桥牌中的逆序排列。13个等级是A、2、3、4、5、6、7、8、9、10、J、Q、K。 根据你玩的游戏的不同，A 可能比 K 大或者比 2 小。

#  像suit_names和rank_names 这样的变量,是定义在类内部但在方法之外, 被称为类属性。因为他们是被关联到 Card 类对象上的.
#  这个术语将它们同 suit 和 rank 这样的变量区分开来，后者被称为实例属性， 因为他们被关联到了特定的实例。


class Card:
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    # suit_names = ['Club', 'Diamonds', 'Hearts', 'Spades']
    # Club, Diamond, Heart, Spade = Suit('Club', '♣'), Suit('Diamond', '♦'), Suit('Heart', '♥'), Suit('Spade', '♠')
    suit_names = ['♣', '♦', '♥', '♠']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s  %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, self.rank
        return t1 < t2


#   生成一副牌的最简单方法是使用嵌套循环。外层循环枚举 0 到 3 的花色。内层循环枚举 1 到 13 的等级。
#   每一个迭代都用当前的花色和等级创建一张新的牌。然后放入 self.cards 中。
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    # 出牌
    def pop_card(self):
        return self.cards.pop()

    # 加牌
    def add_card(self, card):
        self.cards.append(card)

    # 洗牌
    def shuffle(self):
        random.shuffle(self.cards)


class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    # 进行代码封装
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

queen_of_diamonds = Card(1, 12)
card1 = Card(2, 11)
hand = Hand('new hand')
deck = Deck()
card = deck.pop_card()
hand.add_card(card)


def run():
    print "hello"
    print(queen_of_diamonds)
    print(card1)
    print deck
    print hand.cards
    print hand.label
    print hand

if __name__ == "__main__":
    run()

