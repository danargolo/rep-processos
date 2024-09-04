value = int(input('Digite um número e verifique se pertence à sequencia Fibonacci: \n'))

def fibonacci_check(num):
  seq = []
  a, b = 0, 1

  while a <= num:
    seq.append(a)

    if a == num:
      return print(f'{num} pertence à sequencia Fibonacci')
    
    a, b = b, a + b
  
  return print(f'{num} não pertence à sequencia Fibonacci')
  
fibonacci_check(value)
