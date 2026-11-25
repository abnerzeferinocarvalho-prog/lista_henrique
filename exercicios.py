# Criando a lista de listas inicial (ID, Nome, Preço)
produtos = [
    [1, "Teclado", 120.00],
    [2, "Mouse", 65.50],
    [3, "Monitor", 850.00]
]

# 1. Imprimir os produtos
print("--- LISTA INICIAL DE PRODUTOS ---")
for produto in produtos:
    print(f"ID: {produto[0]} | Produto: {produto[1]} | Preço: R$ {produto[2]:.2f}")

# 2. Localizar um produto pelo ID
print("\n--- BUSCA DE PRODUTO ---")
id_procurado = 2
encontrado = False

for produto in produtos:
    if produto[0] == id_procurado:
        print("Produto encontrado:", produto)
        encontrado = True
        break

if not encontrado:
    print("Produto não encontrado.")

# 3. Remover um produto pelo ID
print("\n--- REMOÇÃO DE PRODUTO ---")
id_remover = 1

for indice, produto in enumerate(produtos):
    if produto[0] == id_remover:
        removido = produtos.pop(indice)
        print("Produto removido:", removido)
        break

# 4. Imprimir novamente a lista depois da remoção
print("\n--- LISTA APÓS A REMOÇÃO ---")
for produto in produtos:
    print(f"ID: {produto[0]} | Produto: {produto[1]} | Preço: R$ {produto[2]:.2f}")


# ==========================================
# DESAFIOS EXTRAS
# ==========================================

# Desafio A: Cadastrar um novo produto usando append()
print("\n--- CADASTRANDO NOVO PRODUTO ---")
novo_produto = [4, "Headset", 199.90]
produtos.append(novo_produto)
print("Novo produto adicionado com sucesso!")

# Desafio B: Alterar o preço de um produto pelo ID
print("\n--- ALTERANDO PREÇO DE UM PRODUTO ---")
id_alterar = 3
novo_preco = 799.00

for produto in produtos:
    if produto[0] == id_alterar:
        produto[2] = novo_preco  # O índice 2 corresponde à coluna do preço
        print(f"Preço do produto '{produto[1]}' atualizado para R$ {produto[2]:.2f}")
        break

# Exibição final para conferir todas as alterações
print("\n--- LISTA FINAL ATUALIZADA ---")
for produto in produtos:
    print(f"ID: {produto[0]} | Produto: {produto[1]} | Preço: R$ {produto[2]:.2f}")
