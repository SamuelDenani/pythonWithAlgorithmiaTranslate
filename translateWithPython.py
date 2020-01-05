import Algorithmia
import json

with open('credentials.json', 'r') as readFile:
	credentials = json.load(readFile)

apiKey = credentials['apiKey']

actions = ['translate', 'detect_language']

action = int(input('Welcome to the Python Algorithm with Google Translator, please select the action you want to use:\n1- Translate 2- Detect Language\n'))
userText = input('Ok! Tell me what is your text\n')

userInput = {
  'action': actions[action-1],
  'text': userText,
}

if action == 1:
	sourceLang = input('Now please let me know from what language you want to translate\n')
	targetLang = input('Right! And what language do you want to translate to?\n')
	userInput.update({'source_language': sourceLang,'target_language': targetLang})

client = Algorithmia.client(apiKey)
algo = client.algo('translation/GoogleTranslate/0.1.1')
result = 'This is your result: ' + algo.pipe(userInput).result['translation' if action == 1 else 'language'] 

print(result)
