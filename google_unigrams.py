import os
import csv
import string
import concurrent.futures
from google_ngram_downloader import readline_google_store
from tqdm import tqdm


def process_letter(letter):
    """Process a single letter from the Google ngram dataset."""
    letter_dict = {}
    fnames, urls, records = next(
        readline_google_store(ngram_len=1, indices=letter, lang="eng")
    )
    for i in records.__iter__():
        ngram = str(i.ngram).lower()
        if ngram.find("_") == -1:
            if ngram in letter_dict:
                temp = letter_dict.get(ngram)
                freq = temp["freq"] + i.match_count
                count = temp["count"] + 1
                letter_dict[ngram] = {"freq": freq, "count": count}
            else:
                freq = i.match_count
                count = 1
                letter_dict[ngram] = {"freq": freq, "count": count}
    return letter_dict


def calculate_relative_freq(ngram_dict):
    """Calculate relative frequency for each ngram."""
    result = {}
    for k, v in ngram_dict.items():
        relative_freq = round(float(v["freq"] / v["count"]), 2)
        result[k] = relative_freq
    return result


def merge_dicts(dict_list):
    """Merge multiple dictionaries."""
    merged = {}
    for d in dict_list:
        for k, v in d.items():
            if k in merged:
                merged[k]["freq"] += v["freq"]
                merged[k]["count"] += v["count"]
            else:
                merged[k] = v
    return merged


def write_to_csv(result_dict, output_file):
    """Write results to CSV file."""
    with open(output_file, "w", newline="\n", encoding="utf-8") as output:
        writer = csv.writer(output, delimiter=";")
        for k, v in result_dict.items():
            value = str(v).lower()
            value = value.rstrip(string.whitespace)
            writer.writerow([str(k).lower(), value])
    print(f"CSV file successfully exported to {output_file}!")


if __name__ == "__main__":
    # Get alphabet
    alphabet = list(string.ascii_lowercase)
    print(f"Processing letters: {alphabet}")

    # Set up the process pool (adjust max_workers based on your CPU)
    max_workers = min(len(alphabet), os.cpu_count() or 4)
    print(f"Using {max_workers} workers for parallel processing")

    # Process letters in parallel
    results = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks and create a future-to-letter mapping
        future_to_letter = {
            executor.submit(process_letter, letter): letter for letter in alphabet
        }

        # Process results as they complete
        for future in tqdm(
            concurrent.futures.as_completed(future_to_letter),
            total=len(alphabet),
            desc="Processing alphabet",
        ):
            letter = future_to_letter[future]
            try:
                letter_results = future.result()
                results.append(letter_results)
                print(
                    f"Completed processing letter '{letter}' with {len(letter_results)} entries"
                )
            except Exception as e:
                print(f"Error processing letter '{letter}': {e}")

    # Merge all dictionaries
    print("Merging results...")
    dict_ngram = merge_dicts(results)
    print(f"Total unique ngrams: {len(dict_ngram)}")

    # Calculate relative frequencies
    print("Calculating relative frequencies...")
    result = calculate_relative_freq(dict_ngram)

    # Export to CSV
    ROOT_OUTPUT = "ENG1"
    file_output = ROOT_OUTPUT + "_GoogleUnigrams.csv"
    write_to_csv(result, file_output)
