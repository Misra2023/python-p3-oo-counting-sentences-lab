import re

class MyString:
    def __init__(self, value=''):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        delimiters = ['.', '!', '?']
        sentences = [s for s in re.split('|'.join(map(re.escape, delimiters)), self._value) if s]
        return len(sentences)