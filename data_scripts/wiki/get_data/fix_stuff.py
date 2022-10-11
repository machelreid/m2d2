from bs4 import BeautifulSoup
import sys
import os


filename = sys.argv[1]
write_path = sys.argv[2]

with open(filename, "r") as f:
    soup = BeautifulSoup(f.read(), "lxml")
docs = soup.find_all("doc")

for doc in docs:
    if len([i for i in doc.text.split("\n") if i != ""]) >= 1:
        doc_title = doc["title"].replace(" ", "_").split("/")[-1]
        d = os.path.join(write_path, doc_title[:2].upper())
        os.makedirs(d, exist_ok=True)
        with open(
            os.path.join(d, doc_title + ".txt"),
            "w",
        ) as f:
            f.write(doc.text)
