from utils import morse_dict, punctuation_marks


def translate_to_morse(sentence: str) -> str:
    """ Returns a morse translation of the inputted sentence.

    Args:
        sentence (string): A sentence provided from the user.
        
    returns:
        morse_translation (string): The corresponding morse
        representation of the inputted sentence.
    """

    morse_translation = ''

    for letter in sentence.replace(' ', '').lower():
        if letter in punctuation_marks:
            pass
        else:
            morse_translation += (morse_dict[letter] + ' ')

    return morse_translation


if __name__ == "__main__":
    user_sentence = input('Please insert the text you would like to convert: ')
    translation = translate_to_morse(user_sentence)
    print(f'The morse translation of your message is: {translation}')
