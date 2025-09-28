# lib/anagram.py
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, word_list):
        matches = []
        # Sort the letters of the original word once
        sorted_word = sorted(self.word)
        
        for candidate in word_list:
            candidate_lower = candidate.lower()
            # Skip if it's the same word (case-insensitive)
            if candidate_lower == self.word:
                continue
            # Check if sorted letters match
            if sorted(candidate_lower) == sorted_word:
                matches.append(candidate)
        
        return matches