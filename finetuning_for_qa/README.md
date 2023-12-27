# Fine-tuning for QA
We adopt the official training code from [!huggingface](https://github.com/huggingface/transformers/tree/main/examples/pytorch/question-answering).

## Setup
```bash
pip install -r requirements.txt
```

## Run
We include two demo scripts for fine-tuning in which you can modify the model and data sources. 
The training parameters can be found in the paper.

To reproduce the main results:
```bash
bash ft.sh
```
To reproduce the results for varying the amount of data:
```bash
bash ft_num.sh
```








