# your code goes here!
class Anagram :
    def __init__(self,word):
        self.word = word
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        matches = []

        for candidate in word_list:

          if sorted(candidate.lower()) == self.sorted_word and candidate.lower() != self.word:
            # Check if the sorted letters of the lowercase candidate match the original sorted word
            # Also ensure it's not exactly the same word as the original (case-insensitive)
              matches.append(candidate) # If both conditions are true, add to matches
        return matches
# match method       
#iterates over the list of candidate words.
#Sorts each candidate and compares it with the original word’s sorted version.
#Ensures it's not the exact same word (ignoring case).
#Collects valid anagrams into a result list.

