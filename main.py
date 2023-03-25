import tkinter as tk
from pathlib import Path
from tkinter import filedialog

import pdfplumber
from art import tprint
from gtts import gTTS


def text_to_audio(file_path, language="en"):
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        print(f"Выбран файл {Path(file_path).name}.")
        print("Начат процесс обработки.")
        with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = "".join(pages)               # Объединение страниц в один файл
        text = text.replace("\n", "")       # Удаляем переносы строк, чтобы при чтении файла небыло длительных пауз
        audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        audio.save(f"{file_name}.mp3")
        return f"Файл {file_name}.mp3 сохранен."

    else:
        return "Ошибка, не выбран файл или неверный тип файла."


def taking_file_path():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()


def main():
    tprint("PDF_to_MP3", font="buldhead")
    file_path = taking_file_path()
    language = input("Введите язык текста en или ru: ")
    print(text_to_audio(file_path, language))


if __name__ == "__main__":
    main()
