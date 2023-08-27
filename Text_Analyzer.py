class TextAnalyzer:
    def __init__(self, text):
        # Initialize the TextAnalyzer object with the provided text.
        text = text.lower()
        text = text.replace(',','').replace('.','').replace('!','').replace('?','')
        self.fmtText = text  # Store the formatted text in the object.

    def freqAll(self):
        # Calculate the frequency of each word in the formatted text.
        words = self.fmtText.split(' ')
        dict1 = {}
        for word in words:
            frequency = words.count(word)
            dict1[word] = frequency
        return dict1

    def freqOf(self, word):
        # Get the frequency of a specific word in the formatted text.
        dict = self.freqAll()
        if word in dict:
            return dict[word]
        else:
            return 0

comment = "Ugh, this mixer is a mess! It totally breaked after one use. " \
    "Plus, the long delivery was a nightmare. " \
    "The breaked parts, the hassle, the disappointment. " \
    "Would have preferred anything else. Waste of time and money, seriously."

analyzed = TextAnalyzer(comment)
print("Formated text: ", analyzed.fmtText)

dict1 = analyzed.freqAll()
print(dict1)

word = "breaked"
frequency = analyzed.freqOf(word)
print("The word", word,"appears", frequency,"times.")