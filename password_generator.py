import string
import random
class Password:
    def __init__(self, min_length, number=True, symbols = True)->str:
        self.min_length = min_length
        self.number = number
        self.symbol = symbols
        self.letters = string.ascii_letters
        self.numbers = string.digits
        self.symbols = string.punctuation
    
    def __str__(self) -> str:
        return self.__generate_password()
    
    def __len__(self)-> int:
        return len(self.__generate_password())
    
    def __getCharacter(self):
        character = self.letters
        if self.number:
            character += self.numbers
        if self.symbol:
            character += self.symbols
        return character
        
    def __generate_password(self):
        pwd = ""
        meet_criteria = False
        has_number = False
        has_special = False
        
        while not meet_criteria or len(pwd) < self.min_length:
            new_char = random.choice(self.__getCharacter())
            pwd += new_char
            
            if new_char in self.numbers:
                has_number = True
            if new_char in self.symbols:
                has_special = True
                
            if self.number:
                meet_criteria = has_number
            if self.symbol:
                meet_criteria = meet_criteria and has_special
        return pwd
        