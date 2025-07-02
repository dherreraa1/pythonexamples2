from collections import Counter
import re
from tkinter.filedialog import askopenfilename
import pathlib
from pypdf import PdfReader
import docx

def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common() # n = number of words to show

def main() -> None:
    # original version
    # text: str = input("Enter your text: ").strip()

    # new version
    filename = askopenfilename()
    with open(filename, "r") as file:
        file_suffix = pathlib.Path(filename).suffix
        if file_suffix == '.pdf':
            reader = PdfReader(filename)
            page = reader.pages[0]
            text = page.extract_text()
        elif file_suffix == '.doc' or file_suffix == '.docx':
            doc = docx.Document(filename)
            fulltext = []
            for paragraph in doc.paragraphs:
                fulltext.append(paragraph.text)
            text = '\n'.join(fulltext)
        else:    
            text = file.read()

    word_frequencies: list[tuple[str, int]] = get_frequency(text)
    
    for word, count in word_frequencies:
        print(f"{word}: {count}")

if __name__ == '__main__':
    main()
