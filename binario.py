# Exemplo: Aqui está uma maneira prática de representar strings ASCII como sequências de bits em Python. Cada caractere da string ASCII é pseudocodificado em 8 bits, com espaços entre as sequências de 8 bits, cada uma representando um único caractere.
#
def make_bitseq(s: str) -> str:
     if not s.isascii():
         raise ValueError("ASCII only allowed")
     return " ".join(f"{ord(i):08b}" for i in s)

texto = input('\nDigite uma sequência qualquer: ')
binario = make_bitseq(texto)
print(f'\nA sequência de bits de {texto} é: {binario}')