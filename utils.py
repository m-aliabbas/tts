import inflect

def convert_to_words(text):
    p = inflect.engine()
    words = text.split()
    print(words)
    for i, word in enumerate(words):
        if word.isdigit():
            num_word = p.number_to_words(word)
            if i == 0:
                num_word = num_word.capitalize()
            else:
                num_word = num_word.lower()
            words[i] = p.ordinal(num_word)
        else:
            if word[0].isdigit():
                num_word = p.number_to_words(word[:-2]) # 1st ===> 1 etc
                words[i] = p.ordinal(num_word)
    return ' '.join(words)

# text = "Class 7th is bad class. The students are 15 years old"
# converted_text = convert_to_words(text)
# print(converted_text)