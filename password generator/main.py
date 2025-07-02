import secrets, string

class Password:
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols
        self.base_characters: str = string.ascii_lowercase + string.digits
        
        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation

    def generate(self) -> str:
        password: list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))

        return ''.join(password)

    def strength_checker(self) -> bool:
        if self.use_symbols and self.use_uppercase and self.length > 16:
            print("Strong password.")
            return True
        if not self.use_symbols:
            print("Password does not contain any symbols.")
        if not self.use_uppercase:
            print("Password does not contain uppercase characters.")
        if self.length <= 16:    
            print("Password length is too short.")
        return False

def main() -> None:
    password: Password = Password(length=17, uppercase = False, symbols = False)
    for i in range(5):
        generated: str = password.generate()
        print(f'{generated} ({len(generated)} chars)')
        print(password.strength_checker())

if __name__ == '__main__':
    main()