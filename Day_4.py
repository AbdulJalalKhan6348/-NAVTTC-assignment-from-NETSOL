import re
from collections import Counter


# ==========================================
# 1. Load Dataset
# ==========================================

try:
    with open("input.txt", "r", encoding="utf-8") as file:
        text = file.read()

except FileNotFoundError:
    print("Error: input.txt file not found.")
    exit()


# ==========================================
# 2. Tokenization
# ==========================================

words = re.findall(r"\b\w+\b", text.lower())

if not words:
    print("Error: input.txt is empty.")
    exit()

print("Total words:", len(words))


# ==========================================
# 3. Unigram Model
# ==========================================

word_counts = Counter(words)
total_words = len(words)


def unigram_probability(word):
    """
    Calculate the probability of a word
    using the Unigram Model.
    """

    word = word.lower()

    if total_words == 0:
        return 0

    return word_counts[word] / total_words


# ==========================================
# 4. Bigram Model
# ==========================================

bigram_counts = Counter(
    (words[i], words[i + 1])
    for i in range(len(words) - 1)
)


def bigram_probability(previous_word, current_word):
    """
    Calculate P(current_word | previous_word)
    using the Bigram Model.
    """

    previous_word = previous_word.lower()
    current_word = current_word.lower()

    bigram = (previous_word, current_word)

    numerator = bigram_counts[bigram]
    denominator = word_counts[previous_word]

    if denominator == 0:
        return 0

    return numerator / denominator


# ==========================================
# 5. Trigram Model
# ==========================================

trigram_counts = Counter(
    (words[i], words[i + 1], words[i + 2])
    for i in range(len(words) - 2)
)


def trigram_probability(word1, word2, word3):
    """
    Calculate P(word3 | word1, word2)
    using the Trigram Model.
    """

    word1 = word1.lower()
    word2 = word2.lower()
    word3 = word3.lower()

    trigram = (word1, word2, word3)
    bigram = (word1, word2)

    numerator = trigram_counts[trigram]
    denominator = bigram_counts[bigram]

    if denominator == 0:
        return 0

    return numerator / denominator


# ==========================================
# 6. Next-Word Prediction
# ==========================================

def predict_next_word(sentence, top_n=5):
    """
    Predict the next word based on the
    last two words of the given sentence.
    """

    sentence_words = re.findall(
        r"\b\w+\b",
        sentence.lower()
    )

    # Trigram model requires at least 2 words
    if len(sentence_words) < 2:
        return []

    word1 = sentence_words[-2]
    word2 = sentence_words[-1]

    predictions = []

    # Search all trigrams
    for (w1, w2, w3), count in trigram_counts.items():

        if w1 == word1 and w2 == word2:

            denominator = bigram_counts[(w1, w2)]

            if denominator > 0:
                probability = count / denominator

                predictions.append(
                    (w3, probability)
                )

    # Sort by highest probability
    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    # Return top N predictions
    return predictions[:top_n]


# ==========================================
# 7. Display Model Information
# ==========================================

print("\n========== MODEL INFORMATION ==========")

print("Unique words:", len(word_counts))
print("Total bigrams:", len(bigram_counts))
print("Total trigrams:", len(trigram_counts))


# ==========================================
# 8. Interactive Predictor
# ==========================================

while True:

    sentence = input(
        "\nEnter a sentence (or type 'quit'): "
    )

    # Exit program
    if sentence.lower().strip() == "quit":
        print("Program ended.")
        break

    # Check empty input
    if not sentence.strip():
        print("Please enter a sentence.")
        continue

    # Get predictions
    predictions = predict_next_word(sentence, top_n=5)

    # Display predictions
    if not predictions:

        print("No prediction found.")

    else:

        print("\nNext-word predictions:")

        for word, probability in predictions:

            print(
                f"{word}: "
                f"{probability * 100:.2f}%"
            )