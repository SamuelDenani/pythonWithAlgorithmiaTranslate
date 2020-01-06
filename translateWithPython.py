# Import Algorithmia module to use Google Translate algorithm
import Algorithmia
# Import JSON built-in module to get credentials from credential.json
import json

# Read credentials.json
with open('credentials.json', 'r') as readFile:
	credentials = json.load(readFile)

# Save api key from credentials file
apiKey = credentials['apiKey']

# List with all possible actions
actions = ['translate', 'detect_language']

# Ask user to enter wanted action with an integer, then we can get the respective action from "actions" list
action = int(input('Welcome to the Python Algorithm with Google Translator, please select the action you want to use:\n1- Translate 2- Detect Language\n'))

# Ask for the text to translate or detect language
userText = input('Ok! Tell me what is your text\n')

# Dictionary for user input following the Algorithmia Google Translate algorithm model.
# This way, if user wants to detect the language, the dictionary is already setted, so if
# the user wants to translate the dictionary can be updated later
userInput = {
  'action': actions[action-1],
  'text': userText,
}

# If the user wants to translate then ask for the source language and the target language.
# And update "userInput" dictionary to send all informations in the request.
if action == 1:
	sourceLang = input('Now please let me know from what language you want to translate\n')
	targetLang = input('Right! And what language do you want to translate to?\n')
	userInput.update({'source_language': sourceLang,'target_language': targetLang})

# Log in Algorithmia
client = Algorithmia.client(apiKey)
# Set the Google Translate algorithm
algo = client.algo('translation/GoogleTranslate/0.1.1')
# Set variable to hold the result. If user want to translate search for translation, otherwise
# search for language.
result = 'This is your result: ' + algo.pipe(userInput).result['translation' if action == 1 else 'language'] 

print(result)
