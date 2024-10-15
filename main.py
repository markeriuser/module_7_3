import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:

                    all_text = file.read().lower()


                    translator = str.maketrans('', '', string.punctuation.replace('-', ''))
                    all_text = all_text.translate(translator)


                    words = all_text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        results = {}
        all_words = self.get_all_words()
        word = word.lower()
        for file_name, words in all_words.items():
            if word in words:
                results[file_name] = words.index(word) + 1
        return results

    def count(self, word):
        results = {}
        all_words = self.get_all_words()
        word = word.lower()
        for file_name, words in all_words.items():
            results[file_name] = words.count(word)
        return results


# Пример выполнения программы

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
