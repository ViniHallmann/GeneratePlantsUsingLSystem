import random
from rules   import AXIOM, RULES
from globals import GENERATIONS

class LSystem:
    def __init__(self):
        self.current = AXIOM


    def set_values(self, current_string: bool = None) -> None:
        if current_string is not None:
            self.current = AXIOM

    def generate(self) -> str:
        for _ in range(GENERATIONS):
            next_string = ""
            for char in self.current:
                if char in RULES:
                    next_string += self.choose_rule(RULES[char])
                else:
                    next_string += char
            self.current = next_string
        return self.current
    
    def generate_next(self) -> str:
        next_string = ""
        for char in self.current:
            if char in RULES:
                next_string += self.choose_rule(RULES[char])
            else:
                next_string += char
        self.current = next_string
        return self.current

    def choose_rule(self, rules: list) -> str:
        n = random.random()
        t = 0
        for rule in rules:
            t += rule["prob"]
            if n < t:
                return rule["rule"]
        return ""
