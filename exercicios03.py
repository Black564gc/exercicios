def verificar_idade(nome, idade):

  if idade >= 18:
    return f"{nome}! Você é maior de idade."
  else:
    return f"{nome}! Você é menor de idade."

nome = "Richard"
idade = 16
print(verificar_idade(nome, idade))

