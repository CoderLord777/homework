def single_root_words(root_word, *other_words):
    same_words = []
    root_word_reg = root_word.lower()
    for word in other_words:
        word_reg = word.lower()
        if root_word_reg in word_reg or word_reg in root_word_reg:
            same_words.append(word)
    return same_words

test1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(test1)
test2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print (test2)