class Sentence(list):
    def __init__(self, plain_text):
        for word in plain_text.split():
            self.append(self.FormatedWord(word))
        
    def __str__(self):
        l = []
        for i in self:
            l.append(i.word if i.capitalize==False else i.word.upper())
        return " ".join(l)

    class FormatedWord:
        def __init__(self, word, capitalize=False):
            self.word = word
            self.capitalize = capitalize


if __name__ == "__main__":
    sentence = Sentence("hellow man")
    sentence[1].capitalize = True
    print(sentence)