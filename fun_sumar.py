def sumar(a: int = 5, b: int = 1) -> int:
  try:
    return print(f'Resultado: ',a+b)
  except TypeError:
    print('Erroe de valor')
  except Exception as e:
    print('Error:',e)
    
sumar(4,5)