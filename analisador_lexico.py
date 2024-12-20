"""
Código de um Analisador Lexico com objetico de categorizar o texto enviado

"""

import re

# Definição de padrões para as categorias
TOKEN_PATTERNS = [
    (r'\b(if|else|while|for|return|int|float|string|void)\b', 'Palavra-chave'),
    (r'[a-zA-Z_]\w*', 'Letra'), #letras
    (r'\b\d+\b', 'Int'), # NUmeros
    (r'\b\d+\.\d+\b', 'Float'), # Float
    (r'[*=+-;{}()\[\],.]', 'Operador'),  # Operadores
    (r'[!@#$%^&*()-_\\{};:"\\|,.<>\/?]', 'Símbolo'),  # símbolos especiais
    (r'[a-zA-Z0-9._%+-]+@(gmail.com|hotmail.com)', 'Endereço de Email'),  # Endereço de email
    (r'\s+', None),  # Ignorar espaços em branco
]

# Função do analizador léxico
def analisar_lexico(codigo):
    tokens = []
    while codigo:
        for padrao, categoria in TOKEN_PATTERNS:
            match = re.match(padrao, codigo)
            if match:
                if categoria:  # Ignorar categorias None
                    tokens.append({
                        'Token': match.group(),
                        'Categoria': categoria
                    })
                codigo = codigo[match.end():]  # Avançar no código
                break
        else:
            raise ValueError(f"Token inválido: {codigo[0]}")
    return tokens


# Função para categorizar a entrada do usuário
def categorizar_entrada():
    codigo_fonte = input("\n Digite o texto para ser analisado: ")
    resultado = analisar_lexico(codigo_fonte)

    for token in resultado:
        print(f"<Token: '{token['Token']}', Categoria: {token['Categoria']}>")

# Loop do print
while True:
  categorizar_entrada()

  # Condição de saída do loop
  if input("Digite 'sair' para encerrar ou qualquer tecla para continuar: ") == "sair":
      break

