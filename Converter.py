class Converter:
    def __init__(self):
        self.ver_en = "livros/3_musk_en.txt"
        self.ver_fr = "livros/3_musk_fr.txt"

    """função que transforma os ficheiros todos para UPPERCASE"""
    def small2big(self):
        with open(self.ver_en, "r", encoding="utf-8") as en:
            with open("livros/3_MUSK_EN.txt", "w", encoding="utf-8") as EN:
                for line in en:
                    EN.write(line.upper())

        with open(self.ver_fr, "r", encoding="utf-8") as fr:
            with open("livros/3_MUSK_FR.txt", "w", encoding="utf-8") as FR:
                for line in fr:
                    FR.write(line.upper())
