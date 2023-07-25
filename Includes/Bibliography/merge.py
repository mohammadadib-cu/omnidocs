import os

data_all = "";
for file in os.listdir():
    if file[-3:] == "bib" and (not file == "all.bib"):
        with open(file, "r", encoding="utf8") as fp:
            data = fp.read();
        data_all += "\n";
        data_all += data;
    
    with open("all.bib", "w", encoding="utf8") as fp:
        fp.write(data_all);