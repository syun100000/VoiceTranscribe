import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr
from pydub import AudioSegment
import os

# GUIアプリの作成
def create_gui():
    window = tk.Tk()
    window.title("文字起こしアプリ")

    status_var = tk.StringVar()
    status_var.set("準備完了")
    status_label = tk.Label(window, textvariable=status_var)
    status_label.pack()

    # ファイルのインポート
    def import_file():
        file_path = filedialog.askopenfilename(filetypes=[("音声ファイル", "*.wav"), ("音声ファイル", "*.mp3"), ("音声ファイル", "*.m4a"), ("動画ファイル", "*.mp4")])
        if file_path:
            status_var.set("ファイルを解析中...")
            window.update()
            analyze_audio(file_path)
    
    # 音声ファイルの解析
    def analyze_audio(file_path):
        if not file_path.endswith('.wav'):
            # mp3, mp4, m4aファイルをwavに変換
            audio = AudioSegment.from_file(file_path)
            file_path = "temp.wav"
            audio.export(file_path, format="wav")

        r = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            audio = r.record(source)
        text = r.recognize_google(audio, language="ja-JP")
        text_prompt.configure(state=tk.NORMAL)
        text_prompt.delete("1.0", tk.END)
        text_prompt.insert(tk.END, text)
        text_prompt.configure(state=tk.DISABLED)

        # temp.wavを削除
        if os.path.exists("temp.wav"):
            os.remove("temp.wav")

        status_var.set("解析完了")

    # テキストのエクスポート
    def export_text():
        text = text_prompt.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("テキストファイル", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)

    # テキストのコピー
    def copy_text():
        text = text_prompt.get("1.0", tk.END)
        window.clipboard_clear()
        window.clipboard_append(text)

    # インポートボタンの作成
    import_button = tk.Button(window, text="ファイルをインポート", command=import_file)
    import_button.pack()
    
    # テキストプロンプトの作成
    text_prompt = tk.Text(window, height=10, state=tk.DISABLED)
    text_prompt.pack()
    
    # エクスポートボタンの作成
    export_button = tk.Button(window, text="テキストをエクスポート", command=export_text)
    export_button.pack()

    # コピー機能のボタンの作成
    copy_button = tk.Button(window, text="テキストをコピー", command=copy_text)
    copy_button.pack()
    
    window.mainloop()

# GUIアプリの実行
create_gui()
