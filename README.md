# Google Unigrams Frequency Corpus

This project processes Google's n-gram dataset to create a frequency corpus of English unigrams (single words). It downloads, processes, and calculates relative frequencies for words from the Google Books corpus, making it available in a CSV format.

## Features

- Downloads and processes Google's n-gram dataset for English unigrams
- Parallel processing of data using multiple CPU cores
- Calculates relative frequencies for each word
- Exports results to a CSV file
- Progress tracking with tqdm
- Handles large datasets efficiently

## Requirements

- Python 3.x
- Required Python packages:
  - google-ngram-downloader
  - tqdm

## Installation

1. Clone this repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Install the required dependencies:
```bash
pip install google-ngram-downloader tqdm
```

## Usage

Simply run the script:
```bash
python google_unigrams.py
```

The script will:
1. Process all letters of the alphabet in parallel
2. Download and process the Google n-gram data
3. Calculate relative frequencies
4. Export the results to a CSV file named `ENG1_GoogleUnigrams.csv`

## Output Format

The output CSV file contains two columns:
- Word: The lowercase unigram
- Frequency: The calculated relative frequency

The file is delimited by semicolons (;) and uses UTF-8 encoding.

# Weirdness Index for Important Word Extraction

This project also provides a function to extract important words from a specialist corpus using the "weirdness" index, as described in Ahmad et al. (1999). The weirdness index measures how much more frequent a word is in a specialist corpus compared to general English, highlighting domain-specific vocabulary.

### How Weirdness is Calculated

For each word:

    Weirdness = (ws/ts) / (wg/tg)

Where:
- ws = frequency of the word in the specialist corpus
- ts = total words in the specialist corpus
- wg = frequency in the general corpus (Google Unigrams)
- tg = total words in the general corpus

Words with high weirdness are considered important or distinctive for the specialist domain.

### Usage Example

You can use the provided Python function to extract important words from your own text:

```python
from extract_words import calculate_word_frequencies_from_text, extract_important_words_by_weirdness

specialist_text = """
The investors were excited about the supercritical fluid technology. 
Dollars and cents were discussed, and the pressurization of the fluid was achieved. 
Supercritical fluids are important in modern finance and chemistry. 
The investors agreed that the dollars invested in supercritical fluid research would yield returns.
"""

specialist_corpus_freqs = calculate_word_frequencies_from_text(specialist_text)
general_corpus_file = "Eng_GoogleUnigrams.csv"

important_words = extract_important_words_by_weirdness(
    specialist_corpus_freqs, general_corpus_file, top_n=10, min_weirdness=1.0
)

for word, score in important_words:
    print(f"{word}: {score:.2f}")
```

## References

Ahmad, K., Gillam, L., & Tostevin, L. (1999). University of Surrey Participation in TREC8: Weirdness Indexing for Logical Document Extrapolation and Retrieval (WILDER). In E. M. Voorhees & D. K. Harman (Eds.), Proceedings of The Eighth Text REtrieval Conference, TREC 1999, Gaithersburg, Maryland, USA, November 17-19, 1999 (NIST Special Publication, Vol. 500-246). National Institute of Standards and Technology (NIST). [PDF](http://trec.nist.gov/pubs/trec8/papers/surrey2.pdf)

BibTeX:

```bibtex
@inproceedings{weirdness_org,
  author    = {Khurshid Ahmad and
               Lee Gillam and
               Lena Tostevin},
  editor    = {Ellen M. Voorhees and
               Donna K. Harman},
  title     = {University of Surrey Participation in {TREC8:} Weirdness Indexing
               for Logical Document Extrapolation and Retrieval {(WILDER)}},
  booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999,
               Gaithersburg, Maryland, USA, November 17-19, 1999},
  series    = {{NIST} Special Publication},
  volume    = {500-246},
  publisher = {National Institute of Standards and Technology {(NIST)}},
  year      = {1999},
  url       = {http://trec.nist.gov/pubs/trec8/papers/surrey2.pdf},
  timestamp = {Tue, 30 Jun 2020 17:23:13 +0200},
  biburl    = {https://dblp.org/rec/conf/trec/AhmadGT99.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

## Performance

- The script uses parallel processing to handle multiple letters simultaneously
- The number of workers is automatically set based on your CPU cores
- Progress is displayed using tqdm progress bars

## Notes

- The script processes only English unigrams (single words)
- Words containing underscores are filtered out
- All words are converted to lowercase
- The relative frequency is calculated as the total frequency divided by the number of occurrences

## License

[Add your license information here]

## Contributing

[Add contribution guidelines if applicable] 