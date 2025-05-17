# Instalar a biblioteca OpenAI
!pip install --upgrade openai --quiet

# Importar a biblioteca OpenAI
from openai import OpenAI

# Instanciar o cliente com sua chave de API
client = OpenAI(api_key="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")  # Substitua pela sua chave de API

# Função para interagir com o modelo GPT-4.1-mini
def chat_with_gpt(messages):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.7,
        max_tokens=150
    )

    return response.choices[0].message.content

# Início da conversa
conversation = [
    {"role": "system", "content": "Você é um assistente de pedidos de pizza."},
    {"role": "user", "content": "Olá!"}
]

# Interação com o usuário
print(chat_with_gpt(conversation))

# Coletar nome do cliente
name = input("Por favor, informe seu nome: ")
conversation.append({"role": "user", "content": f"meu nome é: (name)"})
print(chat_with_gpt(conversation))

# prompt: Solicitar o sabor, e tamanho da pizza para o cliente. (grande, média, pequena).

flavor = input("Qual sabor de pizza você gostaria? ")
size = input("Qual tamanho (grande, média, pequena)? ")

conversation.append({"role": "user", "content": f"Gostaria de uma pizza de {flavor} no tamanho {size}."})
print(conversation)

# prompt: Solicitar o sabor, e tamanho da pizza para o cliente. (grande, média, pequena).

flavor = input("Qual sabor de pizza você gostaria? ")
size = input("Qual tamanho (grande, média, pequena)? ")

conversation.append({"role": "user", "content": f"Gostaria de uma pizza de {flavor} no tamanho {size}."})
print(chat_with_gpt(conversation))

# prompt: Solicitar endereço de entrega para o cliente. Pedindo Rua, Bairro, e número da casa

print("\nPara entrega, por favor, informe seu endereço:")
street = input("Rua: ")
neighborhood = input("Bairro: ")
number = input("Número da casa: ")

conversation.append({"role": "user", "content": f"Meu endereço para entrega é: Rua {street}, Bairro {neighborhood}, número {number}."})
print(chat_with_gpt(conversation))

# prompt: Confirmar pedido do cliente. Verificando todas as informações solicitadas para confirmar

# Confirmar pedido com o cliente
confirm_order_message = f"""Por favor, confirme os detalhes do seu pedido:
Nome: {name}
Pedido: Pizza de {flavor}, tamanho {size}
Endereço de entrega: Rua {street}, Bairro {neighborhood}, número {number}

Está correto? (sim/não)
"""
print(confirm_order_message)
confirmation = input().lower()

if confirmation == 'sim':
    conversation.append({"role": "user", "content": "Sim, o pedido e o endereço estão corretos."})
    print(chat_with_gpt(conversation))
    print("\nPedido confirmado! Obrigado.")
else:
    conversation.append({"role": "user", "content": "Não, há um erro no meu pedido ou endereço."})
    print(chat_with_gpt(conversation))
    print("\nOk, vamos revisar seu pedido.")
    # Aqui você pode adicionar lógica para permitir que o usuário corrija as informações.

