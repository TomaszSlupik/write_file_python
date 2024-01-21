# Wygeneruj wszystkie liczby parzyste od 2 do 18 włącznie. 
# Następnie zapisz każdą liczbę w osobnej linii do pliku o nazwie num.txt.

myNum = []
for num in range(2, 19):
    if num % 2 == 0:
        myNum.append(num)

    with open ('num.txt', "w") as file:
        for num in myNum:
            file.write(str(num) + '\n')

try:
    with open ('num.txt', "r") as file:
        for line in file:
            print(line.strip())
except:
    print('Plik nie istnieje')

print('---')

# Zapisz powyższe dane do pliku 
headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open ('users.csv', "w") as file:
    for i,head in enumerate(headers):
        file.write(head)
        if i < len(headers) - 1:
            file.write(',')
    file.write('\n')

    for user in users:
        file.write(','.join(user))
        file.write('\n')

with open('users.csv', "r") as file:
    for line in file:
        print(line.strip())

print('---')

# Zapisz listę do pliku txt
listLang = ['python', 'java', 'sql', 'sas']

with open ('techs.txt', "w") as file:
    for line in listLang:
        file.write(line + '\n')

print('---')

# Zapisz listę produktów do pliku tekstowego o nazwie products.txt. 
# Każdy produkt zapisz jako wiersz, który składa się z nazwy produktu i ceny, 
# oddzielonych przecinkiem. Każdy wiersz zakończ znakiem nowej linii \n.

products = [
    {'name': 'T-shirt', 'price': 29.99},
    {'name': 'Shoes', 'price': 99.99},
    {'name': 'Pants', 'price': 49.99},
]
    
with open ('products.txt', "w") as file:
    for prod in products:
        myProd = f"{prod['name']}, {prod['price']}"
        file.write(myProd + '\n')


with open  ('products.txt', "r") as file:
    for line in file:
        print(line.strip())

print('---')



