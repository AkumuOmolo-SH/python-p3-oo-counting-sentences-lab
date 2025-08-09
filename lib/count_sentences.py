#!/usr/bin/env python3

import re  # for counting sentences

class MyString:
    def __init__(self, value=""):
        self.value = value  # calls the setter

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")  # or raise an error

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        # Use regex to split on '.', '!', or '?'
        sentences = re.split(r'[.!?]', self.value)
        # Remove empty strings and whitespace-only strings
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

      
    
        

      
        
   


