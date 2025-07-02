from collections import Counter

def open_file(path: str) -> str:
    with open(path,'r') as file:
        text: str = file.read()
        return text

def analyse(text: str) -> dict[str, tuple]:

    print('Extracted text:')
    print(f'"{text}"')

    result: dict[str, tuple] = {
        'total_chars_incl_spaces': (len(text), 'Total characters including spaces'),
        'total_chars_excl_spaces': (len(text.replace(' ','')), 'Total characters excluding spaces'),
        'total_spaces': (text.count(' '), 'Total spaces'),
        'total_words': (len(text.split()), 'Total words'),
        'top_5_most_common_words': (Counter(text.split()).most_common(5), '5 most common words')
    }

    return result

def main() -> None:
    text: str = open_file('note.txt')
    analysis: dict[str, tuple] = analyse(text)
    print("This file contains:")
    for key, value in analysis.items():
        if key != 'top_5_most_common_words':
            print(f'{value[1]}: {value[0]}')
        else:
            print(f'{value[1]}:')
            for i in value[0]:
                print(f'{i[0]}: {i[1]}')    

if __name__ == '__main__':
    main()