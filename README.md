# Heine or not-Heine? That’s the question! - A text classifier

## Table of Contents
1. [General Info](#general-info)
2. [Requirements](#requirements)
3. [Download](#download)
4. [Usage](#usage)
5. [Technologies/Sources](#technologiessources)
6. [Licence](#licence)

## General Info
In this project done in the *Using transformers for CL tasks* class at *Heinrich Heine Univerität Düseldorf*, we (Philipp Bauer, Jefferson Fonseca, Tim Ostrolucký and Velizar Petrov) fine-tuned the BERT language model to recognize texts from the famous German poet and author Heinrich Heine (written in German). We trained BERT to distinguish between texts written by Heine and:
1) modern texts (newspapers, Wikipedia articles, etc.)
2) other German poets and authors from the 19th century (J.W. von Goethe, E.T.A. Hoffmann and Theodor Storm)

In the next step, we asked ChatGPT to write texts in the style of Heinrich Heine to check whether our fine-tuned models recognize these "fakes".

The models that distinguish between Heine texts and modern or contemporary texts can be found in the Jupyter notebooks with the corresponding names (`HeinrichT_modern/historisch.ipynb`). The `CorpusScript.py` program is used to generate the corpus on which these two models are trained as well as the ChatGPT test data by combining the information in the `TextInfo.csv`-file with the texts in the `Textdaten` folder and the modern Leipzig Corpus (`deu_mixed-typical_2011_10K-sentences.txt`).

For further information, please see the paper.

## Requirements
In order to run the `CorpusScript.py` program please make sure you have installed Python Version **3.11.8.** As the other programs are Jupyter notebooks, you do not need to install anything else.

## Download
To be able to run the project on your computer, please clone this GitHub repository by running the following command in your terminal; you have to run the terminal as administrator:
<pre>git clone https://github.com/tiost100/Heinrich_Heine</pre>

## Usage
### CorpusScript.py
To run the `CorpusScript.py` program please do as followed:
* Open your Command Prompt or Windows Terminal.
* Navigate to the directory into where you have stored this repository using the `cd` command.
* Type `python` followed by the name of the Python file, including the `.py` extension.
* Press Enter to run the Python file.

### HeinrichT_modern/historisch.ipynb
To run the Jupyter notebooks please do as followed: 
* Open Google Colab: https://colab.research.google.com/
* Click *Upload Notebook* in the Open Notebook window and select the desired notebook.
* Change runtime type to ***T4 GPU***.
* It is necessary that you run the code cells in the correct order as the individual program parts build on each other. 

## Technologies/Sources
* ChatGPT. (n.d.). Retrieved February 27, 2024, from https://chat.openai.com/
* Code in Action. (2021, July 26). Mastering Transformers | 5. Fine-Tuning Language models for text Classification [Video]. YouTube. Retrieved February 27, 2024, from https://www.youtube.com/watch?v=rR0vHaEOV_k
* German BERT | State of the art language model for German NLP. (n.d.). deepset.ai. Retrieved February 27, 2024, from https://www.deepset.ai/german-bert
* Google Colaboratory. (n.d.). Retrieved February 27, 2024, from https://colab.research.google.com/
* Jin, D., Jin, Z., Hu, Z., Vechtomova, O., & Mihalcea, R. (2020). Deep Learning for text Style Transfer: A survey. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2011.00416
* Project Gutenberg. (n.d.). Project Gutenberg. Retrieved February 27, 2024, from https://www.gutenberg.org/ebooks/results/
* Rothman, D. (2022). Transformers for natural language processing: Build, train, and fine-tune deep neural network architectures for NLP with Python, Hugging Face, and OpenAI’s GPT-3, ChatGPT, and GPT-4. Packt Publishing Ltd.
* Universität Leipzig. (n.d.). Leipzig Corpus. Retrieved February 27, 2024, from https://wortschatz.uni-leipzig.de/de/download/German#mixed-typical
* Yıldırım, S., & Chenaghlu, M. A. (2021). Mastering transformers: Build state-of-the-art models from scratch with advanced natural language processing techniques. Packt Publishing Ltd.

## Licence
We are not aware of any copyright restrictions of the material.
