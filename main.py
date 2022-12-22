
class Characters:
    def Properties(self, name, phrase1, phrase2):
        self.name=name
        self.phrase1=phrase1
        self.phrase2=phrase2
        self.level=0
    
    def speak(self, PhraseNumber):
        if PhraseNumber==1:
            print(self.phrase1)
        elif PhraseNumber==2:
            print(self.phrase2)

    def setLevel(self, newLevel):
        self.level=newLevel
        print(self.level)   

kungfupanda=Characters("Kung Fu Panda", "Skadoosh", "You have been blinded by pure awesomeness!")
spiderman=Characters("Spiderman", "Your friendly neighbourhood spiderman.", "Kachow!")

kungfupanda.speak(1)
spiderman.setLevel(2)
spiderman.speak(2)