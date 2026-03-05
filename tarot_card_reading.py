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
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Daily Horoscope 2026")
        self.main_window.geometry("800x700")
        self.main_window.configure(bg="#2c3e50")

        self.title_label = tk.Label(main_window, text="Tarot Horoscope", font=("Arial", 18, "bold"), fg="#f1c40f",
                                    bg="#2c3e50")
        self.title_label.pack(pady=5)

        self.cards_frame = tk.Frame(main_window, bg="#2c3e50")
        self.cards_frame.pack(pady=10)

        self.card_labels = []
        self.current_photos = []

        self.setup_slots(1)

        self.output_text = tk.Label(main_window, text="Choose cards and click Draw", font=("Arial", 10),
                                    wraplength=600, fg="white", bg="#2c3e50", height=5)
        self.output_text.pack(pady=2)

        self.count_selection = tk.StringVar(main_window)
        self.count_selection.set("1")

        self.dropdown_menu = tk.OptionMenu(main_window, self.count_selection, "1", "2", "3")
        self.dropdown_menu.config(bg="#ecf0f1", fg="black")
        self.dropdown_menu.pack(pady=2)

        self.draw_button = tk.Button(main_window, text="DRAW CARDS", font=("Arial", 11, "bold"),
                                     command=self.run_reading, bg="#e67e22", fg="white", padx=15, pady=5)
        self.draw_button.pack(pady=10)

    def setup_slots(self, count):
        for label in self.card_labels:
            label.destroy()
        self.card_labels = []
        self.current_photos = []

        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        back_path = os.path.join(script_dir, "tarot_cards_images", "card_back.png")

        for i in range(count):
            lbl = tk.Label(self.cards_frame, bg="#34495e", relief="sunken", bd=2)
            lbl.grid(row=0, column=i, padx=5)
            self.card_labels.append(lbl)

            try:
                img = Image.open(back_path).resize((180, 300), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.current_photos.append(photo)
                lbl.config(image=photo)
            except:
                lbl.config(text="Tarot", fg="white", width=20, height=15)

    def run_reading(self):
        user_count = int(self.count_selection.get())
        self.setup_slots(user_count)

        tarot_reader = TarotReader()
        reading_results = tarot_reader.get_interpretations(tarot_reader.draw_multiple_cards(user_count))

        final_display_text = ""
        for i, item in enumerate(reading_results):
            final_display_text += f"{item['name']} ({item['orientation']})\n"
            self.update_card_image(i, item['name'], item['is_upright'])

        self.output_text.config(text=final_display_text.strip())

    def update_card_image(self, index, card_name, is_upright):
        import os
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filename = f"{card_name.lower().replace(' ', '_')}.png"
            image_path = os.path.join(script_dir, "tarot_cards_images", filename)

            loaded_img = Image.open(image_path)
            if not is_upright:
                loaded_img = loaded_img.rotate(180)

            loaded_img = loaded_img.resize((180, 300), Image.LANCZOS)
            photo = ImageTk.PhotoImage(loaded_img)

            self.current_photos[index] = photo
            self.card_labels[index].config(image=photo, text="")
        except:
            self.card_labels[index].config(text=f"Missing:\n{card_name}", fg="white", width=20, height=15)
            
if __name__ == "__main__":
    app_root = tk.Tk()
    tarot_instance = TarotApp(app_root)
    app_root.mainloop()
