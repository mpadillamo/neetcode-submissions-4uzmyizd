class WordDictionary:

    def __init__(self):
        self.words = set() #.add

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        else:
            for el in self.words:
                if len(el) == len(word):
                    c = 0
                    for i in range(len(word)):
                        if el[i] == word[i] or word[i] == ".":
                            c += 1
                    
                    if len(word)== c:
                        return True
            return False
            