import random
import string


def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    gerar_senha = ''.join(random.choice(caracteres)
                          for i in range(comprimento))
    return gerar_senha


try:

    comprimento_senha = int(input('Digite o comprimento da senha desejada: '))
    nova_senha = gerar_senha(comprimento_senha)
    print(f'Sua Nova senha é: {nova_senha}')
except ValueError:
    print('Error: O comprimento da senha deve ser um número inteiro.')
