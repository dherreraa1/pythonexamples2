morse_code_dict: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/', '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.',
    '!': '-.-.--', '(': '-.--.', ')': '-.--.-', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', '&': '.-...'
}

def convert_to_morse(text: str) -> str:
    return ' '.join(morse_code_dict.get(char.upper(),'') for char in text)

def invert_dict_values_keys(dictionary: dict[str, str]) -> dict[str, str]:
    return dict(zip(dictionary.values(),dictionary.keys()))

def morse_to_text(morse_text: str) -> str:
    morse_to_text_dict = invert_dict_values_keys(morse_code_dict)
    return ''.join(morse_to_text_dict.get(word,'') for word in morse_text.split())

def main() -> None:
    user_input: str  = input('Enter text: ')
    output: str = convert_to_morse(user_input)
    print(output)
    morse_text: str = morse_to_text(output)
    print(morse_text)

if __name__ == '__main__':
    main()