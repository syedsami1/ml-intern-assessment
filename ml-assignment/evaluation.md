# **evaluation.md**

## **Trigram Language Model – Design Choices**
For this assignment, I built a trigram language model from scratch to predict the next word based on the previous two words. I tried to keep the design simple and clear while still following the assignment requirements.

### **How I Stored N-Gram Counts**

I decided to use a nested dictionary for storing trigrams. Each bigram `(w1, w2)` is a key in the outer dictionary, and it maps to another dictionary that counts the next word `w3`. This structure felt intuitive because it’s easy to update during training and look up possible next words during generation. I also kept a `vocab` set with all unique words seen in the text, mainly to keep track of what words the model knows.

### **Text Cleaning, Padding, and Unknown Words**

Before training, I converted all text to lowercase and removed punctuation. This way, words like “Alice” and “alice” are treated the same, and punctuation doesn’t interfere with tokenization. I split the text into words by whitespace. To make sure the model could start and stop sentences properly, I padded the text with two `<START>` tokens at the beginning and a single `<END>` token at the end. I didn’t implement special handling for unknown words since the assignment didn’t require it, but the `vocab` set could be used for that in the future.

### **How I Implemented the Generate Function**

For generating text, I start with the bigram `("<START>", "<START>")`. Then, I look up all possible next words for that context and randomly pick one using the counts as weights. I used `random.choices()` to turn the counts into a probability distribution so the model samples words probabilistically instead of just picking the most likely one. After selecting a word, I slide the context window forward and repeat until either `<END>` is generated or the maximum length is reached. If the model has no data (like when the input text is empty), `generate()` just returns an empty string.

### **Other Design Decisions**

I tried to keep the model simple and readable. I didn’t add smoothing or more advanced features because the goal was to understand trigram modeling and probabilistic generation. I made sure the code handled edge cases like empty input gracefully and kept the nested dictionary approach because it’s both efficient and easy to understand.
=======

For this assignment, I built a trigram language model from scratch to predict the next word based on the previous two words. I tried to keep the design simple and clear while still following the assignment requirements.

### **How I Stored N-Gram Counts**

I decided to use a nested dictionary for storing trigrams. Each bigram `(w1, w2)` is a key in the outer dictionary, and it maps to another dictionary that counts the next word `w3`. This structure felt intuitive because it’s easy to update during training and look up possible next words during generation. I also kept a `vocab` set with all unique words seen in the text, mainly to keep track of what words the model knows.

### **Text Cleaning, Padding, and Unknown Words**

Before training, I converted all text to lowercase and removed punctuation. This way, words like “Alice” and “alice” are treated the same, and punctuation doesn’t interfere with tokenization. I split the text into words by whitespace. To make sure the model could start and stop sentences properly, I padded the text with two `<START>` tokens at the beginning and a single `<END>` token at the end. I didn’t implement special handling for unknown words since the assignment didn’t require it, but the `vocab` set could be used for that in the future.

### **How I Implemented the Generate Function**

For generating text, I start with the bigram `("<START>", "<START>")`. Then, I look up all possible next words for that context and randomly pick one using the counts as weights. I used `random.choices()` to turn the counts into a probability distribution so the model samples words probabilistically instead of just picking the most likely one. After selecting a word, I slide the context window forward and repeat until either `<END>` is generated or the maximum length is reached. If the model has no data (like when the input text is empty), `generate()` just returns an empty string.

### **Other Design Decisions**

I tried to keep the model simple and readable. I didn’t add smoothing or more advanced features because the goal was to understand trigram modeling and probabilistic generation. I made sure the code handled edge cases like empty input gracefully and kept the nested dictionary approach because it’s both efficient and easy to understand.


