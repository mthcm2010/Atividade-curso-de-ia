1) ele devolve uma String (C)

2) API tem que ser armazenada no arquivo .env pra proteger as informações privadas e evitar que fique direto no código. Desse jeito, diminui o risco de vazar a chave quando compartilhar o projeto ou publicar ele no github
se ninguém tiver acesso, vai poder fazer alguma solicidação usando sua conta e causar gastos não autorizados

3) Uma lista de dicionários (B)

4) 

total = 0
while True:
 n = int(input("Número (0 para sair): "))
 if n == 0:
 break
 total += n
print(f"Soma: {total}")