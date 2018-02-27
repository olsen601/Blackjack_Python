import BlackJack_v2
import sqlite3
from unittest import TestCase
from unittest.mock import Mock, patch
from BlackJack_v2 import deck_generator
from BlackJack_v2 import game

class TestBlackjack(TestCase):

    #TODO test_deck_generator
    @patch('BlackJack_v2.deck_generator')
    @patch('BlackJack_v2.deck_generator')
    def test_deck_generator(self, mock_deck, mock_deck2):
        self.assertCountEqual(mock_deck, mock_deck2)

    #TODO test_deal_card
    @patch('BlackJack_v2.deck_generator')
    def test_deal_card(self, mock_deck):
        card = BlackJack_v2.deal_card()
        self.assertNotIn(card, mock_deck)

    #TODO test_hand
    @patch('BlackJack_v2.deck_generator')
    def test_hand(self, mock_deck):
        test_hand = BlackJack_v2.hand()
        for test_card in test_hand:
            self.assertNotIn(test_card, mock_deck)
        self.assertEqual(2, len(test_hand))

    #TODO test_score
    def test_score(self):
        test_hand1 = ['5 of Clubs','10 of Hearts']
        test_hand2 = ['8 of Diamonds','King of Spades']
        test_hand3 = ['Ace of Spades','King of Diamonds']
        test_hand4 = ['Ace of Diamonds','Ace of Clubs','Ace of Spades','Ace of Hearts','10 of Clubs']
        self.assertEqual(15, BlackJack_v2.score(test_hand1))
        self.assertEqual(18, BlackJack_v2.score(test_hand2))
        self.assertEqual(21, BlackJack_v2.score(test_hand3))
        self.assertEqual(14, BlackJack_v2.score(test_hand4))
        self.assertNotEqual(24, BlackJack_v2.score(test_hand4))

    #TODO test_hit

    #TODO test_evaluation

    #TODO test_blackjack

    #TODO test_game
    
