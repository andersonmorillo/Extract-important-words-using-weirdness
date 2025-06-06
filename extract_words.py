import csv
from typing import Dict, List, Tuple
import re
from collections import Counter


def extract_important_words_by_weirdness(
    specialist_corpus_freqs: Dict[str, int],
    general_corpus_file: str,
    top_n: int = 50,
    min_weirdness: float = 1.0,
) -> List[Tuple[str, float]]:
    """
    Extract important words from a specialist corpus using the weirdness index.
    Args:
        specialist_corpus_freqs: dict of {word: frequency} for the specialist corpus
        general_corpus_file: path to Eng_GoogleUnigrams.csv (general corpus)
        top_n: number of top words to return
        min_weirdness: minimum weirdness value to include a word
    Returns:
        List of (word, weirdness_score) tuples, sorted by weirdness descending
    """
    # Load general corpus frequencies
    general_freqs = {}
    tg = 0
    with open(general_corpus_file, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            if len(row) != 2:
                continue
            word, freq = row
            try:
                freq = float(freq)
            except ValueError:
                continue
            general_freqs[word] = freq
            tg += freq

    # Calculate total words in specialist corpus
    ts = sum(specialist_corpus_freqs.values())

    # Calculate weirdness for each word in specialist corpus
    weirdness_scores = []
    for word, ws in specialist_corpus_freqs.items():
        wg = general_freqs.get(word, 1.0)  # Avoid division by zero
        weirdness = (ws / ts) / (wg / tg)
        if weirdness >= min_weirdness:
            weirdness_scores.append((word, weirdness))

    # Sort by weirdness descending
    weirdness_scores.sort(key=lambda x: x[1], reverse=True)
    return weirdness_scores[:top_n]


def calculate_word_frequencies_from_text(text):
    """
    Calculates the frequency of each word in the given text.

    Args:
        text (str): The input text string.

    Returns:
        dict: A dictionary where keys are words and values are their frequencies.
    """
    text = text.lower()
    words = re.findall(r"\b\w+\b", text)
    word_frequencies = Counter(words)

    return dict(word_frequencies)


if __name__ == "__main__":
    # Example specialist corpus text (e.g., from a finance article)
    specialist_text = """
    The investors were excited about the supercritical fluid technology. 
    Dollars and cents were discussed, and the pressurization of the fluid was achieved. 
    Supercritical fluids are important in modern finance and chemistry. 
    The investors agreed that the dollars invested in supercritical fluid research would yield returns.
    """

    specialist_corpus_freqs = calculate_word_frequencies_from_text(specialist_text)

    general_corpus_file = "Eng_GoogleUnigrams.csv"

    top_words = extract_important_words_by_weirdness(
        specialist_corpus_freqs, general_corpus_file, top_n=10, min_weirdness=1.0
    )

    print("Top important words by weirdness:")
    for word, score in top_words:
        print(f"{word}: {score:.2f}")
