from deep_translator import GoogleTranslator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
en_sentense = {}

for word in french_words:
    en_sentense[word] = GoogleTranslator(source='auto', target='en').translate(word)
print(en_sentense)