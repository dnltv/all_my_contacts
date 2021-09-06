import hashlib


def create_code(id):
    c1 = (int(id[0]) + int(id[-1]) + 1) % 10
    c2 = (int(id[1]) + int(id[-2]) + 4) % 10
    c3 = (int(id[2]) + int(id[-3]) + 9) % 10
    c4 = (int(id[3]) + int(id[-4])) % 10
    code = str(c1) + str(c2) + str(c3) + str(c4)
    return code

# Открываем файл для записи ID, кода и хэш
f = open('codes.txt', 'a')

# Проходимся в цикле по первым 5000 значений и записываем построчно в файл
for i in range(1, 5001):
    id = str(i).zfill(8)
    code = create_code(id)
    pre_hash = f'{code}id{id}'
    #hash_object = hashlib.sha1(pre_hash.encode())
    #hex_dig = hash_object.hexdigest()
    hex_dig = hashlib.sha1(pre_hash.encode()).hexdigest()
    info = f'{id} {code} {hex_dig}'
    f.write(info + '\n')

# Закрываем файл
f.close()
