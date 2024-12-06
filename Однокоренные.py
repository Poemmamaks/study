def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if str.lower(root_word) in str.lower(other_words[i]) or str.lower(other_words[i]) in str.lower(root_word):
            same_words.append(other_words[i])
    print(same_words)



single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

