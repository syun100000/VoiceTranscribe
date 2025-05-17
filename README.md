# VoiceTranscribe

## 概要
VoiceTranscribeは、音声ファイル（wav, mp3, m4a, mp4）を日本語テキストに変換するデスクトップアプリケーションです。TkinterによるGUIを備え、ファイルのインポート・文字起こし・テキストのエクスポート・コピーが簡単に行えます。

## 特徴
- 音声ファイルの自動文字起こし（Google Speech Recognition API使用）
- wav以外の音声/動画ファイルも自動変換対応
- 文字起こし結果のテキストファイル保存・クリップボードコピー
- シンプルなGUI
- DDD（ドメイン駆動設計）に基づく構成

## 使い方
1. 必要なライブラリをインストール
   ```sh
   pip install -r requirements.txt
   ```
2. アプリを起動
   ```sh
   python app.py
   ```
3. 「ファイルをインポート」ボタンから音声ファイルを選択
4. 解析が完了するとテキストが表示されます
5. 必要に応じて「テキストをエクスポート」や「テキストをコピー」を利用

## ディレクトリ構成
```
VoiceTranscribe/
├── app.py                  # プレゼンテーション層（GUI）
├── transcription_service.py # ドメイン層（文字起こしロジック）
└── ...
```

## 必要なライブラリ
- tkinter
- speechrecognition
- pydub

## ライセンス
MIT License
