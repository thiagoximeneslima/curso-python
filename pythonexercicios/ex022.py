nomecompleto = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...\n')
print('Seu nome em maiúsculo é:',nomecompleto.upper())
print('Seu nome em minúsculo é: ',nomecompleto.lower())
print('O seu nome completo tem {} letras'.format(len(nomecompleto) - nomecompleto.count(' ')))
print('O seu  primeiro nome tem {} letras'.format(nomecompleto.find(' ')))
