class Character:
    def __init__(self, character: str, bold: bool=False, italic: bool=False, underline: bool=False) -> None:
        assert len(character) == 1, "Character length must be equal to 1"
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self) -> str:
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character

class Document:
    def __init__(self) -> None:
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character: Character or str) -> None:
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self) -> None:
        del self.characters[self.cursor.position]

    def save(self) -> None:
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()
    
    @property
    def string(self) -> str:
        return "".join((str(c) for c in self.characters))
    
class Cursor:
    def __init__(self, document: Document) -> None:
        self.document = document
        self.position = 0

    def forward(self) -> None:
        self.position += 1
    
    def back(self) -> None:
        self.position -= 1
    
    def home(self) -> None:
        while self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break
    
    def end(self) -> None:
        while self.position < len(self.document.characters) and self.document.characters[self.position].character != '\n':
            self.position += 1

if __name__ == '__main__':
    doc = Document()
    doc.filename = "test_document"
    doc.insert('h')
    doc.insert('e')
    doc.insert(Character('l', bold=True))
    doc.insert(Character('l', bold=True))
    doc.insert('o')
    doc.insert('\n')
    doc.insert(Character('w', italic=True))
    doc.insert(Character('o', italic=True))
    doc.insert(Character('r', underline=True))
    doc.insert('l')
    doc.insert('d')
    print(doc.string)
    doc.cursor.home()
    doc.delete()
    doc.insert('W')
    print(doc.string)
    doc.characters[0].underline = True
    print(doc.string)