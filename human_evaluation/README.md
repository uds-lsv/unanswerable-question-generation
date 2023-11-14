# Human evaluation

The file [results.tsv](/human_evaluation/results.tsv) contains all the data needed to replicate our human evaluation.

![Spreadsheet with columns for paragraph, question, ID, and annotations for unanswerability, relatedness and readability for 3 annotators. Each paragraph extends over 4 rows since it is paired with 4 questions.](/img/human_evaluation_results.png "Results from 3 annotators in a spreadsheet")

Each of the 100 paragraphs in this sheet is paired with 4 questions in randomized order - one written by crowdworkers, one generated with UNANSQ, one generated with CRQDA, and one generated with our methods (a 50-50 mix of antonym-augmented and entity-augmented questions).

## Replicating the annotation

Annotators received a copy of this spreadsheet on Google Sheets, but without the ID column (which indicates how each question was generated). The paragraphs and questions were in exactly the same order as in the results.tsv file. Annotators also received a copy of the annotation guidelines (provided in Appendix C of our paper). We used the built-in data validation feature to help us ensure the annotations were clean and to help guide the annotators by including short text descriptions of each of the possible annotations for a certain category. In other words, rather than simply indicating numbers like 0, 1, 2, 3, the dropdown also indicated whether this meant "unanswerable" or "related" or "fluent" as shown below.

![Columns for unanswerability relatedness and readability showing annotations like "0 (answerable)" and "1 (related)." A dropdown on the readability column shows that the options for that cell are: 1 (incomprehensible), 2 (minor errors), and 3 (fluent).](/img/data_validation.png "Data validataion")

## Replicating final numbers

Our paper reports averages of the unanswerability, relatedness and readability scores across these 3 annotators, along with Krippendorf's alpha as a measure of inter-annotator agreement for each of these categories individually.
