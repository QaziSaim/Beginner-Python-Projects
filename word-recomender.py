import speech_recognition as sr
import requests

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Function to get a random word from the Random Word API
def get_random_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None

# Function to find similar words in the vocabulary
def recommend_words(recognized_text, vocabulary):
    recognized_words = recognized_text.lower().split()
    recommendations = set()

    for word in recognized_words:
        for vocab_word in vocabulary:
            if vocab_word.startswith(word[:3]):  # Suggest words with similar prefixes
                recommendations.add(vocab_word)

    return recommendations

# Function to capture audio from the microphone and recognize speech
def recognize_speech_from_mic():
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        # Listen for 5 seconds and create the ambient noise energy level
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("Microphone calibrated")

        print("Say something!")
        # Capture the audio data
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print("You said: " + text)

            # Get a random word
            random_word = get_random_word()
            if random_word:
                print("Random word: " + random_word)

                # Add the random word to the vocabulary
                vocabulary.append(random_word)

            # Get vocabulary recommendations
            recommendations = recommend_words(text, vocabulary)
            print("Recommended words: ", ", ".join(recommendations))

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Vocabulary list for recommendations
vocabulary = [
    "hello", "world", "python", "programming", "recognition", "speech",
    "microphone", "ambient", "noise", "audio", "google", "request", "results",
    "service", "understand", "calibrate", "listen", "capture", "text", "engine"
]

# Call the function to start recognizing speech and recommending vocabulary
recognize_speech_from_mic()
