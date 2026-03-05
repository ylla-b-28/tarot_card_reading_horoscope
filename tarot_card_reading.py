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