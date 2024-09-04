text = input("Digite uma frase ou palavra:")

def vowel_counter(string):
  formated_string = string.lower()
  vowel = {
    "a": 0,
  }

  for char in formated_string:
    if char in vowel:
      vowel[char] += 1
      return print(f'A vogal "a" ocorre {vogal["a"]}x em {string}.')

  return print(f'Não há ocorrência de "a" em {string}.')
  

vowel_counter(text)