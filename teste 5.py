def inverter_string(s):
    resultado = ""
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

# String pode ser definida diretamente
# string_original = "exemplo"

# Ou pode ser recebida do usuário
string_original = input("Digite a string que deseja inverter: ")

string_invertida = inverter_string(string_original)

print("String original:", string_original)
print("String invertida:", string_invertida)
