class AnagramChecker():
    def __init__(self):
        self.word_list = None
        with open('words.txt', mode='r') as file:
            content = file.readlines()
            self.word_list = [word.lower().strip() for word in content]

    def is_valid_word(self, word):
        return True if word.lower() in self.word_list else False

    def get_anagrams(self, user_word):
        anagrams = []
        for word in self.word_list:
            if self.is_anagram(word, user_word.lower()) and word != user_word.lower():
                anagrams.append(word)
        if len(anagrams) > 0:
            return anagrams
        else:
            None

    @staticmethod
    def is_anagram(word1, word2):
        if len(word1) == len(word2):
            for letter in word1.lower():
                if letter not in word2.lower():
                    return False

                for let in word2.lower():
                    if let not in word1.lower():
                        return False
            else:
                return True
        else:
            return False
