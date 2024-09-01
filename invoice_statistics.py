import json

def load_data(file_path):
  try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
  
  except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Erro ao carregar arquivo: {e}")
    return None

def invoice_statistics(data):

  invoice_list = data["daily_invoice"]

  valid_invoice = [day["value"] for day in invoice_list if day["value"] > 0]

  min_invoice = min(valid_invoice)
  max_invoice = max(valid_invoice)

  average_invoice = sum(valid_invoice) / len(valid_invoice)

  above_average = len([value for value in valid_invoice if value > average_invoice])

  return {
      "min_invoice": min_invoice,
      "max_invoice": max_invoice,
      "above_average": above_average
  }

def main():
  file_path = 'invoices.json'
  
  data = load_data(file_path)
  if data is None:
      return
  
  result = invoice_statistics(data)
    
  print(f"O menor faturamento ocorrido em um dia do mês: R${result['min_invoice']:.2f}")
  print(f"O maior faturamento ocorrido em um dia do mês: R${result['max_invoice']:.2f}")
  print(f"Dias no qual o valor de faturamento diário foi superior à média mensal: {result['above_average']} dias")

if __name__ == "__main__":
  main()
