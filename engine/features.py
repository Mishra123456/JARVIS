from playsound import playsound
import os

def playassistantSound():
    # Correct relative path
    music_dir = os.path.join('frontend', 'assets', 'audio', 'jarvis-147563.mp3')
    
    # Verify path exists
    if not os.path.exists(music_dir):
        print(f"Error: File not found at {os.path.abspath(music_dir)}")
        return
    
    try:
        playsound(music_dir)
    except Exception as e:
        print(f"Error playing sound: {e}")