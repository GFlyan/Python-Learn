#Faça um programa que leia um valor em metros e o exiba convertido em km, hm, dam, dm, cm e mm.

print('Este é o software de conversão de metros para centímetros e milímetros!')
m = float(input('Digite um valor em metros para a conversão: '))

km = (m/1000)
hm = (m/100)
dam = (m/10)
dm = int(m*10)
cm = int(m*100)
mm= int(m*1000)

print(f'O valor de {m} metros em quilômetros é: \n{km} km \nEm hectômetros é: \n{hm} hm \nEm decâmetros é: \n{dam} dam \nEm decimetros é: \n{dm} dm')
print(f'Em centímetros é: \n{cm} cm \nEm milímetros é: \n{mm} mm')