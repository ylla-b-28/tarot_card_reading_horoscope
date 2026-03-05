import random
import tkinter as tk
from tkinter import Label

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

class TarotApp:
    image_label: Label

    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Daily Horoscope")
        self.main_window.geometry("500x800")
        self.main_window.configure(bg="#2c3e50")

        self.main_frame = tk.Frame(main_window, bg="#2c3e50")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.title_label = tk.Label(self.main_frame, text="Tarot Horoscope", font=("Arial", 24, "bold"), fg="#f1c40f",
                                    bg="#2c3e50")
        self.title_label.grid(row=0, column=0, pady=20)

        self.image_label = tk.Label(self.main_frame, bg="#34495e", width=30, height=20, relief="sunken", bd=2)
        self.image_label.grid(row=1, column=0, pady=10)

        self.output_text = tk.Label(self.main_frame, text="Choose cards and click Draw", font=("Arial", 12),
                                    wraplength=400, fg="white", bg="#2c3e50")
        self.output_text.grid(row=2, column=0, pady=10)

        self.count_selection = tk.StringVar(main_window)
        self.count_selection.set("1")

        self.dropdown_menu = tk.OptionMenu(self.main_frame, self.count_selection, "1", "2", "3")
        self.dropdown_menu.config(bg="#ecf0f1", fg="black")
        self.dropdown_menu.grid(row=3, column=0, pady=5)

        self.draw_button = tk.Button(self.main_frame, text="DRAW CARDS", font=("Arial", 12, "bold"),
                                     command=self.run_reading, bg="#e67e22", fg="white", padx=20, pady=10)
        self.draw_button.grid(row=4, column=0, pady=20)

    def run_reading(self):
        tarot_reader = TarotReader()
        user_count = int(self.count_selection.get())
        reading_results = tarot_reader.get_interpretations(tarot_reader.draw_multiple_cards(user_count))

        final_display_text = ""
        for item in reading_results:
            final_display_text += f"{item['name']} ({item['orientation']}): {item['meaning']}\n\n"
            self.refresh_card_image(item['name'], item['is_upright'])

        self.output_text.config(text=final_display_text)

    def refresh_card_image(self, card_name, is_upright):
        try:
            image_path = f"images/{card_name.lower().replace(' ', '_')}.png"
            loaded_img = Image.open(image_path)
            if not is_upright:
                loaded_img = loaded_img.rotate(180)
            loaded_img = loaded_img.resize((250, 400), Image.LANCZOS)
            self.current_card_photo = ImageTk.PhotoImage(loaded_img)
            self.image_label.config(image=self.current_card_photo, text="")
        except:
            self.image_label.config(image='', text=f"Missing: {card_name}", fg="white")

if __name__ == "__main__":
    app_root = tk.Tk()
    tarot_instance = TarotApp(app_root)
    app_root.mainloop()
