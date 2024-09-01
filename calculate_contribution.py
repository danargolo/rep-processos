def calculate_contribution(invoice_by_state):
  values = list(invoice_by_state.values())
  
  total_invoice = sum(values)
  
  percentage_contribution = {
    state: (value / total_invoice) * 100
    for state, value in invoice_by_state.items()
  }
  # print(percentage_contribution)
  
  return {
      "percentage_contribution": percentage_contribution
  }

def main():
  invoice_by_state = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
  }
  
  stats = calculate_contribution(invoice_by_state)
  print(stats["percentage_contribution"].items())
  
  print("O percentual de representação que cada estado:")
  for state, percentage in stats["percentage_contribution"].items():
      print(f"{state}: {percentage:.2f}%")

if __name__ == "__main__":
  main()
