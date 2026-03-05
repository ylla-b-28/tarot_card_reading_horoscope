import random
import tkinter as tk
import os
from datetime import date
from PIL import Image, ImageTk

tarot_meanings = {
    "The Fool": {
        "upright": "A fresh chapter is unfolding. Trust your instincts and take a leap of faith. The universe is guiding you toward an unexpected adventure where innocence and optimism are your greatest strengths. Embrace the unknown with an open heart.",
        "reversed": "You may be acting without thinking, leading to unnecessary risks. Stop and breathe before you jump. Are you running away from something, or toward something meaningful? Reassess your path before you lose your footing."
    },
    "The Magician": {
        "upright": "You possess all the tools required for success. It is time to manifest your desires into reality. Align your willpower with your actions, and you will find that the elements of life bend to your favor. Focus is your magic wand.",
        "reversed": "Your energy is being scattered or manipulated. You have the potential, but a lack of focus or dishonest intentions is blocking your progress. Look inward to find where your power is leaking and fix the drain."
    },
    "The High Priestess": {
        "upright": "Silence the noise of the world and listen to your inner voice. Secrets are being revealed through dreams and intuition. This is a time for deep reflection and spiritual growth rather than outward action. Trust the silence.",
        "reversed": "You are ignoring your gut feelings and relying too much on others' opinions. Hidden motives may be at play. Take time to reconnect with your subconscious before making a major decision. The truth is within, not without."
    },
    "The Empress": {
        "upright": "Abundance, creativity, and nurturing energy surround you. This is a fertile time for new ideas or relationships. Nature and beauty will provide the healing you need to move forward with grace and confidence.",
        "reversed": "You may be feeling a creative block or experiencing a lack of self-worth. Are you giving too much of yourself to others? It is time to stop and nurture your own soul. You cannot pour from an empty cup."
    },
    "The Emperor": {
        "upright": "Structure, discipline, and authority are your allies today. You are in a position to lead and create order out of chaos. Firm boundaries will protect your progress and command the respect you truly deserve.",
        "reversed": "Power is being misused, or a lack of self-control is leading to instability. Avoid being overly rigid or dominating. True leadership comes from wisdom and compassion, not just from barking orders at those around you."
    },
    "The Hierophant": {
        "upright": "Wisdom today comes from tradition and established structures. You may find comfort in a mentor or a community that shares your values. It is a day to honor the rules and seek knowledge from those who have walked the path before you.",
        "reversed": "You are feeling restricted by outdated rules or expectations. It is time to question the status quo and find your own personal truth. Don't be afraid to break away from tradition if it no longer aligns with your soul's growth."
    },
    "The Lovers": {
        "upright": "Harmony and alignment are entering your life. Whether in a relationship or a personal choice, your heart and mind are finally in sync. Trust in the power of connection and the beauty of making choices from a place of love.",
        "reversed": "An imbalance is causing friction in your connections. You may be struggling with a difficult choice or feeling disconnected from your values. Realign with your inner self before trying to fix the external disharmony."
    },
    "The Chariot": {
        "upright": "Victory is within reach, but it requires fierce focus and self-discipline. You are successfully balancing opposing forces to move forward. Stay the course; your determination is the engine that will drive you to your goal.",
        "reversed": "You feel like you’ve lost control of the reins. External pressures or internal conflicts are pulling you in too many directions. Stop and find your center before the momentum leads you off course into chaos."
    },
    "Strength": {
        "upright": "True power today comes from a quiet, inner resilience rather than force. You have the grace to handle difficult situations with patience and compassion. Tame your fears with kindness, and you will find you are unbreakable.",
        "reversed": "You may be struggling with self-doubt or a sudden burst of temper. You are stronger than you feel right now, but your inner lion is acting out because it feels unheard. Practice self-forgiveness to regain your footing."
    },
    "The Hermit": {
        "upright": "The world is too loud right now; the answers you seek are in the silence. Retreat into your own inner sanctuary. This period of soul-searching will provide the clarity that no one else can give you. Trust your inner light.",
        "reversed": "You may be isolating yourself too much or, conversely, fearing being alone. Withdrawal has turned into loneliness. It is time to come back to the light and share the wisdom you’ve found with the world again."
    },
    "Wheel of Fortune": {
        "upright": "The wheel is turning in your favor. Destiny is at work, bringing a stroke of luck or a fated encounter. Change is the only constant, so embrace this upward swing with gratitude and an open mind.",
        "reversed": "A cycle is ending, and things may feel out of your control. You might be experiencing a streak of bad luck, but remember that the wheel never stops turning. This dip is only temporary; hold on tight."
    },
    "Justice": {
        "upright": "Truth and fairness are the themes of the day. Every action has a consequence, and the scales are balancing out. If you have been honest, expect a favorable resolution. Clarity and logic will serve you better than emotion.",
        "reversed": "You may be facing unfairness or a situation where the truth is being hidden. Perhaps you are being too hard on yourself or others. Avoid dishonesty, as the karmic debt will eventually need to be paid."
    },
    "The Hanged Man": {
        "upright": "Progress requires a temporary pause. By letting go of control and looking at your situation from a different angle, you will find a breakthrough. Sacrifice the now for a better later. Surrender is your strength.",
        "reversed": "You are stalling or resisting a necessary change. You may feel like you're in limbo, but you're the one holding yourself there. Stop the indecision and make a move, even if it feels uncomfortable at first."
    },
    "Death": {
        "upright": "A major cycle is ending to make way for a profound transformation. Do not fear the clearing of the old; it is necessary for the new to bloom. Embrace the change and let go of what no longer serves you.",
        "reversed": "You are resisting a necessary ending, which is only causing more pain. The transition is inevitable. Holding on to the past will prevent you from seeing the beautiful new beginning waiting for you."
    },
    "Temperance": {
        "upright": "Balance and moderation are your keys to peace. You are blending different areas of your life into a beautiful harmony. Practice patience and avoid extremes; the middle path is where your healing and growth reside.",
        "reversed": "You are out of sync. Perhaps you are overindulging or rushing a process that needs time. This lack of balance is draining your energy. Re-evaluate your habits and find where you can bring back a sense of calm."
    },
    "The Devil": {
        "upright": "You are becoming aware of a habit or belief that is holding you captive. Recognize that the chains are loose and you have the power to walk away. Freedom starts with acknowledging what binds you.",
        "reversed": "A breakthrough is happening. You are finally breaking free from an old pattern or an unhealthy attachment. The darkness is lifting, and you are reclaiming your independence and your light. Freedom is yours."
    },
    "The Tower": {
        "upright": "A sudden, shocking change is clearing away a foundation built on illusions. While it feels chaotic, this earthquake is necessary to make room for something much more honest and stable. Let the old structures fall.",
        "reversed": "You can feel a disaster coming and are desperately trying to delay it. Or, you have just survived a crisis and are picking up the pieces. Don't rebuild the old version; build something new and stronger."
    },
    "The Star": {
        "upright": "Hope and healing are pouring into your life. The Star brings a sense of renewed purpose and serenity. Trust that you are being protected and that your dreams are truly within reach. The universe is being kind to you.",
        "reversed": "You are feeling discouraged and disconnected from your inspiration. It feels like your light has dimmed. This is a temporary dark night of the soul. The Star is still there; you just need to look up through the clouds."
    },
    "The Moon": {
        "upright": "Things are not as they seem. You are moving through a fog of mystery and hidden emotions. Trust your intuition over your logic today, as your subconscious is trying to communicate through symbols and dreams.",
        "reversed": "The confusion is starting to clear. Secrets are being revealed, and the anxiety of the unknown is fading away. You are learning to distinguish between your true intuition and your irrational fears."
    },
    "The Sun": {
        "upright": "Success, joy, and vitality are radiating through you! Everything you touch turns to gold today. This is a time of peak clarity, warmth, and celebration. Share your light; your happiness is infectious.",
        "reversed": "The clouds are temporarily blocking the sun. You may be feeling less energetic or struggling to see the bright side. The success is still there, but your perspective is a bit gloomy. Focus on the small wins."
    },
    "Judgement": {
        "upright": "A calling is reaching out to you. It is time for deep self-evaluation and a fresh start. You are being washed clean of the past and invited to step into a higher version of yourself. Listen to the call.",
        "reversed": "You are ignoring a wake-up call or judging yourself too harshly. You are stuck in a loop of past mistakes. Stop looking backward; the universe is trying to give you a clean slate, but you have to accept it."
    },
    "The World": {
        "upright": "A major journey has come to a successful conclusion. You feel a sense of wholeness and completion. You have learned your lessons and are ready to step into a whole new level of existence. The world is yours.",
        "reversed": "You are close to the finish line but are struggling to complete the final steps. You might feel a lack of closure. Don't give up now; tie up the loose ends so you can move forward without any heavy baggage."
    }
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
        self.main_window.title("Mystical Tarot Horoscope")
        self.main_window.geometry("900x850")
        self.main_window.configure(bg="#1a1a2e")

        self.user_name = tk.StringVar(value="Seeker")
        self.user_dob = tk.StringVar(value="MM/DD/YYYY")

        profile_frame = tk.Frame(main_window, bg="#16213e", bd=2, relief="ridge")
        profile_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(profile_frame, text="Name:", font=("Arial", 10, "bold"), fg="#e94560", bg="#16213e").grid(row=0, column=0, padx=5, pady=10)
        tk.Entry(profile_frame, textvariable=self.user_name, width=20).grid(row=0, column=1, padx=5)
        tk.Label(profile_frame, text="Birthday (MM/DD/YYYY):", font=("Arial", 10, "bold"), fg="#e94560", bg="#16213e").grid(row=0, column=2, padx=5)
        tk.Entry(profile_frame, textvariable=self.user_dob, width=20).grid(row=0, column=3, padx=5)

        self.title_label = tk.Label(main_window, text="✧ YOUR DESTINY AWAITS ✧", font=("Georgia", 22, "bold"), fg="#e94560", bg="#1a1a2e")
        self.title_label.pack(pady=10)

        self.layout_frame = tk.Frame(main_window, bg="#1a1a2e")
        self.layout_frame.pack(pady=5)

        self.soul_side = tk.Frame(self.layout_frame, bg="#1a1a2e", padx=10)
        self.soul_side.pack(side="left")
        tk.Label(self.soul_side, text="SOUL CARD", font=("Arial", 11, "bold"), fg="#f1c40f", bg="#1a1a2e").pack()
        self.soul_card_label = tk.Label(self.soul_side, bg="#16213e", relief="ridge", bd=3)
        self.soul_card_label.pack(pady=5)

        self.reading_side = tk.Frame(self.layout_frame, bg="#1a1a2e", padx=10)
        self.reading_side.pack(side="left")
        self.reading_title = tk.Label(self.reading_side, text="CURRENT READING", font=("Arial", 11, "bold"), fg="#e94560", bg="#1a1a2e")
        self.reading_title.pack()
        self.cards_frame = tk.Frame(self.reading_side, bg="#1a1a2e")
        self.cards_frame.pack(pady=5)

        self.card_labels = []
        self.current_photos = []
        self.setup_slots(1)

        self.text_frame = tk.Frame(main_window, bg="#16213e")
        self.text_frame.pack(pady=10, padx=20)
        self.scrollbar = tk.Scrollbar(self.text_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.output_text = tk.Text(self.text_frame, font=("Arial", 11, "italic"), fg="#ecf0f1", bg="#16213e", height=8, width=100, wrap="word", bd=0, yscrollcommand=self.scrollbar.set)
        self.output_text.pack(side="left")
        self.scrollbar.config(command=self.output_text.yview)

        self.controls_frame = tk.Frame(main_window, bg="#1a1a2e")
        self.controls_frame.pack(pady=10)
        self.count_selection = tk.StringVar(main_window)
        self.count_selection.set("1")
        tk.OptionMenu(self.controls_frame, self.count_selection, "1", "2", "3").pack(side="left", padx=10)
        self.draw_button = tk.Button(self.controls_frame, text="REVEAL CARDS", font=("Arial", 12, "bold"), command=self.run_reading, bg="#e94560", fg="white", padx=30, pady=10)
        self.draw_button.pack(side="left", padx=10)

    def calculate_soul_card(self, dob_string):
        try:
            total_sum = sum(int(digit) for digit in dob_string if digit.isdigit())
            while total_sum > 22:
                total_sum = sum(int(single_digit) for single_digit in str(total_sum))
            all_card_names = list(tarot_meanings.keys())
            return all_card_names[total_sum - 1] if 0 < total_sum <= 22 else "The Fool"
        except:
            return "The Fool"

    def setup_slots(self, requested_count):
        for existing_label in self.card_labels:
            existing_label.destroy()
        self.card_labels, self.current_photos = [], []
        script_directory = os.path.dirname(os.path.abspath(__file__))
        back_image_path = os.path.join(script_directory, "tarot_cards_images", "card_back.png")

        try:
            back_image_file = Image.open(back_image_path).resize((130, 210), Image.Resampling.LANCZOS)
            self.soul_photo = ImageTk.PhotoImage(back_image_file)
            self.soul_card_label.config(image=self.soul_photo)
        except:
            self.soul_card_label.config(text="Soul", fg="white", width=12, height=10)

        for column_index in range(requested_count):
            card_slot_label = tk.Label(self.cards_frame, bg="#16213e", relief="ridge", bd=3)
            card_slot_label.grid(row=0, column=column_index, padx=5)
            self.card_labels.append(card_slot_label)
            try:
                placeholder_image = Image.open(back_image_path).resize((130, 210), Image.Resampling.LANCZOS)
                placeholder_photo = ImageTk.PhotoImage(placeholder_image)
                self.current_photos.append(placeholder_photo)
                card_slot_label.config(image=placeholder_photo)
            except:
                card_slot_label.config(text="???", fg="white", width=12, height=10)

    def run_reading(self):
        user_selection_count = int(self.count_selection.get())
        self.setup_slots(user_selection_count)

        full_name = self.user_name.get()
        birthday_entry = self.user_dob.get()
        calculated_soul_card = self.calculate_soul_card(birthday_entry)
        soul_card_description = tarot_meanings.get(calculated_soul_card, {}).get("upright", "A mystery.")

        current_date_string = date.today().strftime("%B %d, %Y")
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)

        intro_text = f"Greetings, {full_name}.\nToday is {current_date_string}.\n\n✧ YOUR SOUL CARD: {calculated_soul_card.upper()} ✧\n{soul_card_description}\n"
        intro_text += "--------------------------------------------------\n\n"
        self.output_text.insert(tk.END, intro_text)

        self.update_single_image(self.soul_card_label, calculated_soul_card, True, (130, 210))

        tarot_reader_engine = TarotReader()
        reading_results = tarot_reader_engine.get_interpretations(
            tarot_reader_engine.draw_multiple_cards(user_selection_count))

        for result_index, result_item in enumerate(reading_results):
            result_header = f"--- {result_item['name'].upper()} ({result_item['orientation']}) ---\n"
            self.output_text.insert(tk.END, result_header)
            self.output_text.insert(tk.END, f"{result_item['meaning']}\n\n")
            self.update_reading_image(result_index, result_item['name'], result_item['is_upright'])

        self.output_text.config(state="disabled")

    def update_single_image(self, target_label, card_name, is_upright, dimensions):
        try:
            script_directory = os.path.dirname(os.path.abspath(__file__))
            file_name = f"{card_name.lower().replace(' ', '_')}.png"
            image_full_path = os.path.join(script_directory, "tarot_cards_images", file_name)
            card_image_file = Image.open(image_full_path)
            if not is_upright:
                card_image_file = card_image_file.rotate(180)
            card_image_file = card_image_file.resize(dimensions, Image.Resampling.LANCZOS)
            final_photo_object = ImageTk.PhotoImage(card_image_file)
            target_label.config(image=final_photo_object)
            target_label.image = final_photo_object
        except:
            target_label.config(text="Missing")

    def update_reading_image(self, photo_index, card_name, is_upright):
        try:
            script_directory = os.path.dirname(os.path.abspath(__file__))
            file_name = f"{card_name.lower().replace(' ', '_')}.png"
            image_full_path = os.path.join(script_directory, "tarot_cards_images", file_name)
            card_image_file = Image.open(image_full_path)
            if not is_upright:
                card_image_file = card_image_file.rotate(180)
            card_image_file = card_image_file.resize((130, 210), Image.Resampling.LANCZOS)
            final_photo_object = ImageTk.PhotoImage(card_image_file)
            self.current_photos[photo_index] = final_photo_object
            self.card_labels[photo_index].config(image=final_photo_object)
        except:
            self.card_labels[photo_index].config(text="Missing")

if __name__ == "__main__":
    app_root = tk.Tk()
    tarot_instance = TarotApp(app_root)
    app_root.mainloop()
