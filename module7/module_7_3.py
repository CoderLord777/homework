import re


class WordsFinder:
    def __init__(self, *file_name: str):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        for w in self.file_name:
            with open(w, encoding='utf-8') as file:
                words = []
                for i in file:
                    i = i.lower()
                    i = re.sub(r'[,.\=!\?;:\-]', '', i)
                    words.extend(i.split())
                    all_words[w] = words
        return all_words

    def find(self, word):
        find_dict = self.get_all_words()
        result_dict = {}
        word = word.lower()
        for name, words in find_dict.items():
            result_dict[name] = words.index(word) + 1
        return result_dict

    def count(self, word):
        find_dict = self.get_all_words()
        result_dict = {}
        word = word.lower()
        for name, words in find_dict.items():
            result_dict[name] = words.count(word)
        return result_dict


if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
