class TermFinder():

    def __init__(self, docs=[], term=''):
        self.docs = docs
        self.term = term
        self.wordCounts = []
        self.termCounts = []
        self.results = {}

    def printTermFreq(self):
        # getCounts runs for each document in the array.
        # getCounts fills in all the data we need for the class variables above.
        # Once we have the needed data, we run printSummary for the user.
        for doc in self.docs:
            self.getCounts(doc)
        self.printSummary()

    def getCounts(self, doc):
        count = 0
        path = 'texts/' + doc
        punctArr = ['!','?','.',',',';',':','"','-']
        try:
            with open(path, encoding="utf-8") as f_obj:
                contents = f_obj.read()
        except FileNotFoundError:
            print('file not found')
            pass
        else:
            # Punctuation must be removed from the text before splitting:
            # If punctuation remains, it will throw off the word matching.
            for punct in punctArr:
                contents = contents.replace(punct, '')
            # With the punctuation now removed during the above loop,
            # it is safe to split the text string into an array of words.
            # for futher accuracy, all words will be transformed into lowercase.
            words = contents.lower().split()
            totalWords = len(words)
            self.wordCounts.append(totalWords)
            # Now we check to see if any of the words in the text
            # match the user's input. If they do, we increase the count.
            # Next, we append the count to the termsCount array for later.
            for word in words:
                if word == self.term:
                    count += 1
            self.termCounts.append(count)

    def printSummary(self):
        match = 0
        print(f"\nResults for '{self.term}':")
        print("---------------------------------------")
        print("Filename | Term Frequency (high to low)")
        print("---------------------------------------")
        for i, count in enumerate(self.wordCounts):
            # Only prints the doc and frequency if the termCount isn't zero.
            # if the termCount isn't zero, we increment the match counter.
            if self.termCounts[i] != 0:
                match += 1
                # For readability, we round the frequency to four decimal points.
                termFreq = round(self.termCounts[i]/count, 4)
                self.results[self.docs[i]] = float(termFreq)
                # Now that we have captured the results in the result dictionary,
                # we print it with sortResults().
        self.sortResults()
        print("---------------------------------------")
        # if no matches were found, the match counter will still be at zero.
        if match == 0:
            print("No matches found.\n")

    def sortResults(self):
        dict = self.results
        # Here we sort the dictionary from highest to lowest.
        srtRes = {key: val for key, val in sorted(dict.items(), key = lambda ele: ele[1], reverse = True)}
        for key in srtRes:
            # including the .txt is redundant in the file name, so it is sliced from the printout.
            print(f"{key[:- 4]} -->   {srtRes[key]}")

