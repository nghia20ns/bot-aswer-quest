import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound

# Khởi tạo trình nhận diện giọng nói
recognizer = sr.Recognizer()

# Danh sách các câu hỏi (từ vựng)
vocab_list = [
    "Khí quyễn",  # atmosphere
    "khoãng",     # almost
    "Phần lớn",   # mostly
    "Giải thích", # explanation
    "Áp lực",     # pressure
    "Có sẵn",     # available
    "Bốc hơi",    # evaporating
    "Tan ra trong", # dissolved in
    "Kết tủa",    # precipitation
    "Thành phần", # composition
    "Mất",        # disappearance
    "Nhiệt độ",   # temperature
    "Phổ biến",   # prevalent
    "Kết quả là", # result in
    "Tích tụ",    # accumulation
    "Mở rộng",    # expansion
    "Hút vào",    # absorb into
    "Giải phóng", # release
    "Kết hợp",    # combine with
    "Thay thế"    # replace
]

# Hàm để phát giọng nói tiếng Việt
def speak(text):
    tts = gTTS(text=text, lang='vi')
    tts.save("speak.mp3")
    playsound("speak.mp3")
    os.remove("speak.mp3")

# Hàm lắng nghe giọng nói từ micro
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            # Chuyển giọng nói thành văn bản
            text = recognizer.recognize_google(audio, language="vi-VN")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection")
            return ""

# Vòng lặp hỏi lần lượt từng từ vựng
for word in vocab_list:
    speak(word)  # Máy phát từ vựng
    user_input = listen()  # Người dùng trả lời
    print(f"User response: {user_input}")
    # Tiếp tục hỏi từ tiếp theo
