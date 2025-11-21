import random
import string

class TrigramModel:
    def __init__(self):
        """
        Initializes the TrigramModel.
        """
        self.trigram_counts = {}
        self.vocab = set()

    def clean_text(self, text):
        """
        Cleans the input text by converting to lowercase, removing punctuation,
        and splitting into words.
        """
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        return text.split()

    def fit(self, text):
        """
        Trains the trigram model on the given text.

        Args:
            text (str): The text to train the model on.
        """
        words = self.clean_text(text)

        # If empty text, just store empty model
        if len(words) == 0:
            self.trigram_counts = {}
            return

        # Add padding
        words = ["<START>", "<START>"] + words + ["<END>"]

        # Count trigrams
        for i in range(len(words) - 2):
            w1, w2, w3 = words[i], words[i+1], words[i+2]

            self.vocab.update([w1, w2, w3])

            if (w1, w2) not in self.trigram_counts:
                self.trigram_counts[(w1, w2)] = {}

            if w3 not in self.trigram_counts[(w1, w2)]:
                self.trigram_counts[(w1, w2)][w3] = 0

            self.trigram_counts[(w1, w2)][w3] += 1

    def generate(self, max_length=50):
        """
        Generates new text using the trained trigram model.
        """
        # If no training was done (empty text)
        if not self.trigram_counts:
            return ""

        current_bigram = ("<START>", "<START>")
        generated_words = []

        for _ in range(max_length):

            # If no continuation exists
            if current_bigram not in self.trigram_counts:
                break

            next_word_counts = self.trigram_counts[current_bigram]
            next_words = list(next_word_counts.keys())
            weights = list(next_word_counts.values())

            # Sample next word using probability distribution
            next_word = random.choices(next_words, weights)[0]

            # Stop if END is generated
            if next_word == "<END>":
                break

            generated_words.append(next_word)

            # Slide the window
            current_bigram = (current_bigram[1], next_word)

        return " ".join(generated_words)
