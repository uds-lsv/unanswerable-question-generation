# A Lightweight Method to Generate Unanswerable Questions in English

This repository contains code and data for our paper.

## Code

Code for generating unanswerable questions using entity and antonym swaps, and for filtering them (random filtering as well as GPT2-perplexity-based filtering) are located in the [generating swaps](generating_swaps/) folder. The [finetuning for QA](finetuning_for_qa) folder contains the code we used to train BERT, RoBERTa and ALBERT models for question answering. As input and output, this code uses JSON files in the SQuAD 2.0 format.

## Data

For reproducibility, we provide all of our generated and filtered unanswerable questions in the [augmented data](augmented_data/) folder. Along with our finetuning for QA code, this data can be used to reproduce our reported numbers for our methods as seen in the body of the paper.

## Human evaluation

We also release the data and annotations (from 3 annotators) from our human evaluation. The annotator instructions are available in Appendix C of the paper.
