import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

tarot_meanings = {
    "The Fool": {"upright": "New beginnings.", "reversed": "Recklessness."},
    "The Magician": {"upright": "Manifestation.", "reversed": "Manipulation."},
    "The High Priestess": {"upright": "Intuition.", "reversed": "Secrets."},
    "The Empress": {"upright": "Abundance.", "reversed": "Creative block."},
    "The Emperor": {"upright": "Authority.", "reversed": "Domination."},
    "The Hierophant": {"upright": "Tradition.", "reversed": "Restriction."},
    "The Lovers": {"upright": "Harmony.", "reversed": "Imbalance."},
    "The Chariot": {"upright": "Determination.", "reversed": "Lack of control."},
    "Strength": {"upright": "Courage.", "reversed": "Self-doubt."},
    "The Hermit": {"upright": "Introspection.", "reversed": "Isolation."},
    "Wheel of Fortune": {"upright": "Good luck.", "reversed": "Bad luck."},
    "Justice": {"upright": "Fairness.", "reversed": "Dishonesty."},
    "The Hanged Man": {"upright": "New perspective.", "reversed": "Stalling."},
    "Death": {"upright": "Endings.", "reversed": "Resistance to change."},
    "Temperance": {"upright": "Balance.", "reversed": "Excess."},
    "The Devil": {"upright": "Attachment.", "reversed": "Freedom."},
    "The Tower": {"upright": "Sudden upheaval.", "reversed": "Avoiding disaster."},
    "The Star": {"upright": "Hope.", "reversed": "Despair."},
    "The Moon": {"upright": "Illusion.", "reversed": "Release of fear."},
    "The Sun": {"upright": "Success.", "reversed": "Temporary sadness."},
    "Judgement": {"upright": "Reflection.", "reversed": "Self-judgment."},
    "The World": {"upright": "Completion.", "reversed": "Lack of closure."},
}

class TarotCard:
    def __init__(self, card_name):
        self.card_name = card_name

class TarotDeck:
    def __init__(self):
        self.card_list = []
        self.load_deck()

    def load_deck(self):
        for name in tarot_meanings.keys():
            self.card_list.append(TarotCard(name))

    def draw_single_card(self):
        selected_card = random.choice(self.card_list)
        self.card_list.remove(selected_card)
        return selected_card

class TarotReader:
    def __init__(self):
        self.current_deck = TarotDeck()

    def draw_multiple_cards(self, card_count=1):
        drawn_cards = []
        for _ in range(card_count):
            drawn_cards.append(self.current_deck.draw_single_card())
        return drawn_cards

    def get_interpretations(self, drawn_cards):
        results_list = []
        for card in drawn_cards:
            is_upright = random.choice([True, False])
            card_orientation = "Upright" if is_upright else "Reversed"
            card_meaning = tarot_meanings[card.card_name]["upright" if is_upright else "reversed"]
            results_list.append({
                "name": card.card_name,
                "orientation": card_orientation,
                "meaning": card_meaning,
                "is_upright": is_upright
            })
        return results_list
