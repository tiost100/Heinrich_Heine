import os
import re
import csv

# Get the full path of the directory where the current file is located
dir_path = os.path.dirname(os.path.abspath(__file__))
dir_path = dir_path.replace('\\','/')


def createCorpus(filepath):
    """Create a corpus from the .txt-files

    args: filepath (string, full path of the location of the files)

    return: none

    note: the file path depends on the storage location of the file on the 
    computer, and can vary from computer to computer
    """

    text_nr = 0

    # open the textinfo.csv-file with all the information about every text
    with open(filepath + "/textinfo.csv") as csvfile:
        csv_reader_object = csv.reader(csvfile, delimiter=";")
        row_nr = 0

        # go through each row in the .csv-file
        for row in csv_reader_object:
            # skip the first line as there are only the column names
            if row_nr != 0:
                text_nr = row[0]
                text = ""
                
                # open current .txt-file and store all the text data into variable text
                with open(filepath+ "/Textdaten/" + text_nr + ".txt", "r", encoding="latin-1") as infile:
                    for line in infile:
                        if line.strip():
                            text += line.strip("\n") + " "

                    text = re.sub(";", ",", text)
                    text = re.sub("=", "", text)
                    text = re.sub("_", "", text)

                # split the text into sentences
                sentences = re.split(r'[.!?]', text)
                sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
                sentences_nr = len(sentences)

                # write the sentence ID (text ID & number of sentence), text, author, year, genre, source into the corpus
                with open(f"{dir_path}/Corpus.csv", "a", encoding="latin-1") as outfile:
                    for i in range(sentences_nr):
                        outfile.write(f"{text_nr}-{i};{sentences[i].strip()};{row[1]};{row[2]};{row[3]};{row[4]}\n")
            row_nr += 1

    # open the deu_mixed-typical_2011_10K-sentences.txt-file containing the mixed type Leipzig Corpus from 2011
    with open(filepath + "/deu_mixed-typical_2011_10K-sentences.txt") as infile:
        # go through each row in the .txt-file
        for line in infile:
            # split every line in id and text
            id_sentence = line.split("\t")
            id = int(id_sentence[0]) - 1
            sentence = id_sentence[1].strip()

            # write the sentence ID (text ID & number of sentence), text, author, year, genre, source into the corpus
            with open(f"{dir_path}/Corpus.csv", "a", encoding="utf-8") as outfile:
                outfile.write(f"{int(text_nr) + 1}-{id};{sentence};{'verschieden'};{2011};{'verschieden'};{'Leipzig Corpus'}\n")


def createTestData(filepath):
    """Create test data from the ChatGPT.txt-file

    args: filepath (string, full path of the location of the files)

    return: none

    note: the file path depends on the storage location of the file on the 
    computer, and can vary from computer to computer
    """

    # open the ChatGPT.txt-file with all the information about every text
    with open(filepath + "/ChatGPT.txt", encoding = "utf-8") as infile:
        data = infile.read()

    texts = data.split("----------------------------------------------------------------------------------------------------------------------")
    text_nr = 0

    for t in texts:
        titel_text = t.split(":")

        titel = titel_text[0].strip()
        text = titel_text[1]
        sentences = re.split(r'[.!?]', text)

        sentence_nr = 0

        with open(f"{dir_path}/TestData.csv", "a", encoding="utf-8") as outfile:
            for s in sentences:
                if s.strip():
                    s = re.sub("\n", " ", s)
                    genre = ""

                    if "Gedicht" in titel:
                        genre = "Lyrik"
                    else:
                        genre = "Prosa"
                    
                    outfile.write(f"{text_nr}-{sentence_nr};{s.strip()};{'ChatGPT'};{'2023'};{genre};{titel}\n")
                
                sentence_nr += 1

            text_nr += 1

createCorpus(dir_path)
createTestData(dir_path)