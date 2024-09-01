text = input("Digite um texto ou palavra que deseja inverter:\n")

def reverse_string(str):
  reversed_string = ""
  for char in str:
      reversed_string = char + reversed_string
  print(reversed_string)

reverse_string(text)