#!/usr/bin/env python3

# class MyString:
  
#   pass

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        import re
        # Use regex to count the number of sentences based on punctuation
        sentences = re.split(r'[.!?]+', self.value)
        # Filter out empty strings
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)


