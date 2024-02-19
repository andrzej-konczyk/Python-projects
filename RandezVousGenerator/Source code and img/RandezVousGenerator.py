import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import random
import os
import sys

class IdeaGeneratorApp:
    def __init__(self, csv_file, images_folder):
        self.df = pd.read_csv(csv_file)
        self.columns = list(self.df.columns)
        self.images_folder = images_folder

    def generate_idea(self):
        idea = [random.choice(self.df[column].tolist()) for column in self.columns]
        return idea

    def display_images(self, idea):
        # Usunięcie poprzednich dzieci z images_frame
        for child in images_frame.winfo_children():
            child.destroy()
            
        for i, column in enumerate(self.columns):
            image_path = os.path.join(self.images_folder, f"{idea[i]}.jpg")
            image = Image.open(image_path)
            image = image.resize((300, 300), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            image_label = ttk.Label(images_frame, image=photo)
            image_label.image = photo
            image_label.grid(row=0, column=i, padx=10, pady=10)
            idea_label = ttk.Label(images_frame, text=f"{self.columns[i]}: {idea[i]}", wraplength=300)
            idea_label.grid(row=1, column=i, padx=10, pady=5, sticky="n")

def generate_and_display_idea():
    idea = app.generate_idea()
    app.display_images(idea)

# Pobranie ścieżki do katalogu, w którym znajduje się uruchamiany skrypt
script_directory = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Sprawdzenie, czy plik CSV istnieje w bieżącym katalogu lub w katalogu nadrzędnym
csv_file_path = os.path.join(script_directory, "RandezVous.csv")
if not os.path.exists(csv_file_path):
    parent_directory = os.path.abspath(os.path.join(script_directory, os.pardir))
    csv_file_path = os.path.join(parent_directory, "RandezVous.csv")

# Zbudowanie ścieżki do folderu z obrazami
images_folder_path = script_directory

app = IdeaGeneratorApp(csv_file_path, images_folder_path)

root = tk.Tk()
root.title("Generator pomysłu na randkę")

# Zmiana koloru tła na odcień różu
root.configure(bg="#FFCCCC")

# Zmiana koloru przycisku na odcień czerwieni
style = ttk.Style()
style.configure("TButton", background="#FF3333", font=("Arial", 12))

generate_button = ttk.Button(root, text="Generuj pomysł", command=generate_and_display_idea)
generate_button.pack(pady=10)

idea_label = ttk.Label(root, text="Wygenerowany pomysł na randkę:", font=("Arial", 12, "bold"))
idea_label.pack()

# Ustawienie stylu ramki, aby zmienić kolor tła
style.configure("TFrame", background="#FFCCCC")

images_frame = ttk.Frame(root)
images_frame.pack()

root.mainloop()
