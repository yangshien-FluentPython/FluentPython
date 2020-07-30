# -*- coding: utf-8 -*-
# author: yse
# time: 2020-07-02

import collections
import random


Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck(object):
    ranks = [str(x) for x in range(2, 11)] + list('JQKA')
    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# print len(deck)
# print random.choice(deck)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


deck = FrenchDeck()
for i in sorted(deck, key=spades_high):
    print i
