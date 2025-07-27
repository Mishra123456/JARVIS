# #ab bolega jarvis
# import pyttsx3
# import speech_recognition as sr
# import eel
# import time
# import traceback # <--- Keep this import for debugging

# @eel.expose
# def speak(text):
#     engine = pyttsx3.init('sapi5')# by default voice 1 use hoga
#     voices = engine.getProperty('voices') # to get all the voices
#     #to get another voice
#     engine.setProperty('voice', voices[2].id)
#     engine.setProperty('rate', 170)
#     eel.DisplayMessage(text)
#     print(f"Speaking: {text}") # Improved debug print
#     engine.say(text)
#     engine.runAndWait()

# #we say ,jarvis recognizes
# @eel.expose
# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print('listening....')
#         eel.DisplayMessage('listening....')
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source, 10, 6)

#     try:
#         print('recognizing')
#         eel.DisplayMessage('recognizing....')
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}") # Corrected to f-string
#         eel.DisplayMessage(query)
#         # REMOVED: speak(query) # <--- Removed this to prevent double-speak
#         return query.lower()

#     except sr.UnknownValueError:
#         print("Speech Recognition could not understand audio.")
#         eel.DisplayMessage("Speech Recognition could not understand audio.")
#         return ""
#     except sr.RequestError as e:
#         print(f"Could not request results from Google Speech Recognition service; {e}")
#         eel.DisplayMessage(f"Could not request results from Google Speech Recognition service; {e}")
#         return ""
#     except Exception as e: # <--- Added 'as e' for proper exception handling
#         print(f"An unexpected error occurred during speech recognition in takecommand: {e}")
#         traceback.print_exc() # <--- Show full traceback
#         return ""


# def allcommands(message=1):
#     if message == 1:
#         query = takecommand()
#         print(query)
#         eel.senderText(query)
#     else:
#         query = message
#         eel.senderText(query)

#     try:
#         print(f"Command received by allcommands: {query}") # Improved debug print

#         if "open" in query:
#             from engine.features import openCommand
#             openCommand(query)
#         elif "on youtube" in query: 
#             from engine.features import PlayYoutube
#             PlayYoutube(query)
#         elif "send message" in query or "phone call" in query or "video call" in query:
#             from engine.features import findContact, whatsApp
#             message = ""
#             contact_no, name = findContact(query)
#             if(contact_no != 0):

#                 if "send message" in query:
#                     message = 'message'
#                     speak("what message to send")
#                     query = takecommand()
                    
#                 elif "phone call" in query:
#                     message = 'call'
#                 else:
#                     message = 'video call'
                    
#                 whatsApp(contact_no, query, message, name)

#             else:
#                 speak("did not run")
        
#     except Exception as e: 
#         print("error")
#     eel.ShowHood() 

# # #ab bolega jarvis
# # import pyttsx3
# # import speech_recognition as sr
# # import eel
# # import time
# # import traceback

# # @eel.expose
# # def speak(text):
# #     engine = pyttsx3.init('sapi5')
# #     voices = engine.getProperty('voices')
# #     engine.setProperty('voice', voices[2].id)
# #     engine.setProperty('rate', 170)
# #     eel.DisplayMessage(text)
# #     print(f"Speaking: {text}")
# #     engine.say(text)
# #     engine.runAndWait()

# # @eel.expose
# # def takecommand():
# #     r = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print('listening....')
# #         eel.DisplayMessage('listening....')
# #         r.pause_threshold = 1
# #         r.adjust_for_ambient_noise(source)
# #         audio = r.listen(source, 10, 6)

# #     try:
# #         print('recognizing')
# #         eel.DisplayMessage('recognizing....')
# #         query = r.recognize_google(audio, language='en-in')
# #         print(f"User said: {query}")
# #         eel.DisplayMessage(query)
# #         return query.lower()

# #     except sr.UnknownValueError:
# #         print("Speech Recognition could not understand audio.")
# #         eel.DisplayMessage("Speech Recognition could not understand audio.")
# #         return ""
# #     except sr.RequestError as e:
# #         print(f"Could not request results from Google Speech Recognition service; {e}")
# #         eel.DisplayMessage(f"Could not request results from Google Speech Recognition service; {e}")
# #         return ""
# #     except Exception as e:
# #         print(f"An unexpected error occurred during speech recognition in takecommand: {e}")
# #         traceback.print_exc()
# #         return ""

# # @eel.expose
# # def allcommands(command_input=""): # Renamed parameter for absolute clarity
# #     query = "" # Initialize query

# #     # --- THIS IS THE CRITICAL LOGIC BLOCK (for determining input source) ---
# #     if command_input: # If command_input is NOT empty (meaning text was passed)
# #         query = command_input.lower()
# #         print(f"Command from chatbox: {query}")
# #     else: # If command_input IS empty (meaning mic button/hotkey was used)
# #         query = takecommand() # Then, and ONLY then, get command via voice
# #         print(f"Command from voice: {query}")
# #     # --- END CRITICAL LOGIC BLOCK ---

# #     # Display the determined query on the frontend immediately
# #     eel.DisplayMessage(query)

# #     try:
# #         # --- REMOVE THIS LINE: query=takecommand() ---
# #         # print(f"Command received by allcommands: {query}") # This print statement is good, but use the 'query' determined above

# #         # Check if the query is empty after potential voice recognition failure
# #         if not query.strip(): # Handles cases where query might be just whitespace or empty string
# #             speak("I didn't receive a clear command. Please try again.")
# #             return # Exit the function early if no command to process

# #         if "open" in query:
# #             from engine.features import openCommand # Assuming engine.features exists
# #             openCommand(query)
# #             speak("Opening " + query.replace("open", "").strip() + ".") # Added more specific confirmation
# #         elif "on youtube" in query:
# #             from engine.features import PlayYoutube
# #             PlayYoutube(query)
# #             speak("Playing content on YouTube.")
# #         elif "send message" in query or "phone call" in query or "video call" in query:
# #             from engine.features import findContact, whatsApp
# #             # Removed the 'message = ""' here, as it conflicts with 'query' later
# #             contact_no, name = findContact(query)
# #             if(contact_no != 0):
# #                 if "send message" in query:
# #                     msg_type = 'message'
# #                     speak("What message to send?")
# #                     # This call to takecommand() is correct if you expect voice input for the message content
# #                     message_content = takecommand() # Renamed to avoid confusion with outer 'query'
# #                     whatsApp(contact_no, message_content, msg_type, name)
# #                 elif "phone call" in query:
# #                     msg_type = 'call'
# #                     whatsApp(contact_no, "", msg_type, name)
# #                 else: # video call
# #                     msg_type = 'video call'
# #                     whatsApp(contact_no, "", msg_type, name)
# #             else:
# #                 speak("I did not find that contact.")

# #         # Add more commands here as needed!
# #         elif "hello jarvis" in query:
# #             speak("Hello there! How can I help you today?")
# #         elif "time" in query:
# #             # Current location is Kothri Kalan, Madhya Pradesh, India (IST)
# #             current_time = time.strftime("%I:%M %p")
# #             speak(f"The current time is {current_time} in Kothri Kalan.")
# #         elif "date" in query:
# #             from datetime import date
# #             today = date.today().strftime("%B %d, %Y")
# #             speak(f"Today is {today}.")
# #         elif "system stop" in query or "stop" in query or "exit" in query:
# #              speak("Goodbye!")
# #              eel.closeApp()
# #         else:
# #             speak("I didn't quite catch that. Can you please repeat?")

# #     except Exception as e:
# #         print(f"An error occurred during command processing: {e}")
# #         traceback.print_exc()
# #         speak("I encountered an error trying to process that command.")
# #     finally:
# #         # Call your JavaScript function to reset the UI
# #         eel.ShowHideButton("") # Pass empty string to show mic button

import pyttsx3
import speech_recognition as sr
import eel
import time
import traceback

@eel.expose
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 170)
    eel.DisplayMessage(text)
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        return query.lower()

    except sr.UnknownValueError:
        print("Speech not understood.")
        eel.DisplayMessage("Speech not understood.")
        return ""
    except sr.RequestError as e:
        print(f"Google Speech API error: {e}")
        eel.DisplayMessage(f"Google Speech API error: {e}")
        return ""
    except Exception as e:
        print(f"Speech recognition failed: {e}")
        traceback.print_exc()
        return ""

@eel.expose
def allcommands(message=""):
    try:
        # ✅ Use mic only if no message passed
        if message and message != "1":
            query = message.strip().lower()
            print(f"[Text Input] Query: {query}")
        else:
            query = takecommand()
            print(f"[Voice Input] Query: {query}")

        if not query.strip():
            speak("I didn't catch that. Please try again.")
            return

        eel.DisplayMessage(query)

        # ✅ COMMAND LOGIC
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            contact_no, name = findContact(query)
            if contact_no != 0:
                if "send message" in query:
                    speak("What message to send?")
                    msg = takecommand()
                    whatsApp(contact_no, msg, "message", name)
                elif "phone call" in query:
                    whatsApp(contact_no, "", "call", name)
                else:
                    whatsApp(contact_no, "", "video call", name)
            else:
                speak("Contact not found.")

        elif "hello jarvis" in query:
            speak("Hello there! How can I help you today?")

        elif "time" in query:
            current_time = time.strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")

        elif "date" in query:
            from datetime import date
            today = date.today().strftime("%B %d, %Y")
            speak(f"Today is {today}.")

        elif "stop" in query or "exit" in query:
            speak("Goodbye!")
            eel.closeApp()

        else:
            speak("I didn't quite get that. Please try again.")

    except Exception as e:
        print(f"[ERROR] {e}")
        traceback.print_exc()
        speak("Something went wrong. Please try again.")

    finally:
        eel.ShowHood()
