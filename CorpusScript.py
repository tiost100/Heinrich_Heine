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

                # split the text into sentences
                sentences = text.split(".")
                sentences = sentences[:-1]
                sentences_nr = len(sentences)

                # write the sentence ID (text ID & number of sentence), text, author, year, genre, source into the corpus
                with open(f"{dir_path}/Corpus.csv", "a", encoding="latin-1") as outfile:
                    for i in range(sentences_nr):
                        outfile.write(f"{text_nr}-{i};{sentences[i].strip()};{row[1]};{row[2]};{row[3]};{row[4]}\n")
            row_nr += 1

createCorpus(dir_path)