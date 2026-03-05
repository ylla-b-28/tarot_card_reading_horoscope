import random
import openai
import os
import tkinter as tk
from tkinter import messagebox

class TarotCard:
    def __init__(self, name):
        self.name = name

class TarotDeck:
    def __init__(self):
        self.cards = []
        self.load_cards()

    def load_cards(self):
        major_arcana = [
            "The Fool",
            "The Magician",
            "The High Priestess",
            "The Empress",
            "The Emperor",
            "The Hierophant",
            "The Lovers",
            "The Chariot",
            "Strength",
            "The Hermit",
            "Wheel of Fortune",
            "Justice",
            "The Hanged Man",
            "Death",
            "Temperance",
            "The Devil",
            "The Tower",
            "The Star",
            "The Moon",
            "The Sun",
            "Judgement",
            "The World",
        ]

        for card_name in major_arcana:
            self.cards.append(TarotCard(card_name))

    def draw_card(self):
        return random.choice(self.cards)
