import os
import re

# Get the full path of the directory where the current file is located
dir_path = os.path.dirname(os.path.abspath(__file__))
dir_path = dir_path.replace('\\','/')


def createScript(filepath, author, year, genre, source):
    text = ""

    with open(filepath, "r", encoding="latin-1") as infile:
        for line in infile:
            if line.strip():
                text += line.strip("\n") + " "

        text = re.sub(";", ",", text)

    sentences = text.split(".")

    with open(f"{dir_path}/Lyrisch.csv", "w", encoding="latin-1") as outfile:
        for i in range(len(sentences)):
            outfile.write(f"{i};{sentences[i].strip()};{author};{year};{genre};{source}\n") 

data_text = f"{dir_path}/Lyrisch.txt"
createScript(data_text, "Heinrich Heine", "n.n.", "lyrical", "n.n.")