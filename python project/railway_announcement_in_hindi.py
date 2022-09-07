import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton():
    audio = AudioSegment.from_mp3(r'railway.mp3')
    # 1 - kripya dhyan dijiye
    start = 500
    finish = 4000
    audioProcessed = audio[start:finish]
    audioProcessed.export(r"1_hindi.mp3", format="mp3")

    # 2 - train number

    # 3 from train station

    # 4 - generate se chalkar
    start = 8100
    finish = 8900
    audioProcessed = audio[start:finish]
    audioProcessed.export(r"4_hindi.mp3", format="mp3")

    # 5 - via train station

    # 6 generate ke rastein
    start = 10200
    finish = 11000
    audioProcessed = audio[start:finish]
    audioProcessed.export(r"6_hindi.mp3", format="mp3")

    # 7 - to train station

    # 8 - ko jane wali
    start = 11700
    finish = 12800
    audioProcessed = audio[start:finish]
    audioProcessed.export(r"8_hindi.mp3", format="mp3")

    # 9 - train name

    # 10 - generating platform number
    start = 19800
    finish = 20700
    audioProcessed = audio[start:finish]
    audioProcessed.export(r"10_hindi.mp3", format="mp3")

    # 11 - platform number

    # 12 - generate se jayegi
    start = 21250
    finish = 22300
    audioProcessed = audio[start:finish]
    audioProcessed.export(r"12_hindi.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - train number
        textToSpeech(item['train_number'], r"2_hindi.mp3")

        # 3 from train station
        textToSpeech(item['from'], r"3_hindi.mp3")

        # 5 - via train station
        textToSpeech(item['via'], r"5_hindi.mp3")

        textToSpeech(item['to'], r"7_hindi.mp3")

        # 9 - train name
        textToSpeech(item['train_name'], r"9_hindi.mp3")

        # 11 - platform number
        textToSpeech(item['platform'], r"11_hindi.mp3")

        audios = [f"{i}_hindi.mp3" for i in range(1, 13)]
        announcement = mergeAudios(audios)
        announcement.export(
            f"announcement_{item['train_number']}_{index+1}.mp3", format="mp3")


if __name__ == '__main__':
    print('generating skeleton')
    generateSkeleton()
    print('now generating announcement')
    generateAnnouncement(r'announce_hindi.xlsx')
