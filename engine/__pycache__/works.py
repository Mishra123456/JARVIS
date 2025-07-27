import speech_recognition as sr

for mic_index in [1, 5, 9]:
    print(f"\nTrying mic index: {mic_index}")
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=mic_index) as source:
            print("Calibrating...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            text = r.recognize_google(audio)
            print(f"Mic {mic_index} heard: {text}")
    except Exception as e:
        print(f"Mic {mic_index} failed: {e}")
