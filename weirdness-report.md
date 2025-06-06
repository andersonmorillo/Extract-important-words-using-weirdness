# Weirdness in “Weirdness Indexing for Logical Document Extrapolation and Retrieval (WILDER)”  
**University of Surrey Participation in TREC 8**  

## 1. What is “Weirdness” in This Context?  
- The authors introduce **“weirdness”** as a technical measure:  
  - Comparing word frequencies in a *specialist* corpus (like TREC, composed of newswire, financial, and government texts) versus a *general language* corpus (the British National Corpus, BNC).
  - The **“weirdness coefficient”** is defined as the ratio (normalized for corpus size) of word frequency in specialist texts vs. general texts.
  - Words highly overrepresented in the specialist corpus have high “weirdness.”
- The term apparently draws inspiration from anthropologist Bronisław Malinowski, who referred to “weird” language among shamans (lots of names, spirits, objects).

## 2. Why Did They Use “Weirdness”?  
- The reasoning:  
  - General texts (e.g., BNC) have very few *open-class* (content/topic) words among their most frequent terms, whereas specialist corpora (like TREC-8) have many more open-class words.
  - Words “weird” to general English (much more frequent in specialist texts) probably signify topical relevance.

## 3. How is “Weirdness” Calculated?  
**Formula:**  
```
Weirdness = (ws/ts) / (wg/tg)
```
Where:  
- ws = frequency of the word in the specialist corpus  
- ts = total words in specialist corpus  
- wg = frequency in general corpus  
- tg = total words in general corpus  

If the result is much greater than 1, it’s “weird” (i.e., distinctive for the specialist domain).  
- Example (from their table):  
  - “dollars” has a weirdness of 42.5  
  - “supercritical” (topic word) has a weirdness of 236,000!

## 4. “Weirdness” as a Retrieval Heuristic  
- The system strips off the “most common” words, focusing on those with high “weirdness.”
- Queries are similarly broken into frequency lists, and their “weirdness” measured.
- Documents and queries are matched by overlapping lists of highly “weird” words.

## 5. Examples of Detected “Weirdness”  
- Topic: “supercritical fluids”
  - Words like “supercritical” (236,000), “pressurization” (50,500), “fluid” (4,780), “achieved” (276) — these exceedingly high weirdness values suggest that such words are “alien” in general English, but common in the TREC specialist collection.
- For the Financial Times subcorpus:
  - After filtering out the 2000 most common general words, residual vocabulary is all *finance speak*: “cent, FT, dollars, investors, trading, equity, currency, bond...” (all high-weirdness items).

## 6. System Implementation Quirkiness  
- The prototype (WILDER) was a mash-up of Java, Perl, C, and Unix shell scripts.
- Initial indexing took 4 days on a Sparc Ultra 1.
- Each query took 8 hours to produce results (!), suggesting a lack of optimization—and perhaps a “weird” (by modern standards) tolerance for inefficiency.

## 7. Reflections on “Weirdness”  
- The term is tongue-in-cheek but points to a real linguistic effect: specialist jargon stands out statistically.
- The authors note the technique is theoretically language-independent, since it just looks for “statistical aliens.”
- Potential issues: no synonym handling, no phrase-level context, simple word filtering (no LSI/semantic analysis).
- The method may misinterpret out-of-vocabulary (OOV) words or miss topical context (e.g., “dollar” could be ambiguous without qualifiers).

## 8. Final Thoughts — The Actual Weirdness  
- “Weirdness” as a label and metric is unusual and humorous for an academic information retrieval system.
- Their “remove commonly used words and focus on what is left” approach goes further than standard stoplist approaches—it leverages global statistical contrast in a formal way.
- The approach acknowledges its own limits: synonymy, morphology, technical expressions, and not modern in terms of NLP sophistication.

---

## Summary  
The Surrey team’s use of “weirdness” is both conceptually literal and a playful technical construct. While the approach is simplistic compared to modern NLP strategies, it leverages a genuinely useful statistical effect: words “weird” to the general public tend to be highly relevant in specialist literature. The method is charmingly unorthodox in both naming and execution, reflecting early IR experimentation with corpus statistics.

---

Let me know if you want a more visual report (with tables, figures, or diagrams), or a deeper technical breakdown of their retrieval model or “weirdness” math!
