# ドメイン層：音声ファイルの文字起こしサービス
import os
from pydub import AudioSegment
import speech_recognition as sr

class TranscriptionService:
    """
    音声ファイルの文字起こしを行うサービスクラス
    """
    def transcribe(self, file_path: str) -> str:
        # wav以外は一時的にwavへ変換
        temp_file = None
        if not file_path.endswith('.wav'):
            audio = AudioSegment.from_file(file_path)
            temp_file = "temp.wav"
            audio.export(temp_file, format="wav")
            file_path = temp_file
        recognizer = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="ja-JP")
        # 一時ファイルの削除
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)
        return text
