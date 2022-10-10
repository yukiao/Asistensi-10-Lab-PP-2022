def urutan_data(data):
    urut = True
    while len(data) - 1 > 0 and urut:
        urut = False
        for i in range(len(data)- 1):
            if data[i] > data[i + 1]:
                urut = True
                tukar = data[i]
                data[i] = data[i + 1]
                data[i + 1] = tukar

data = []
bilangan = input('Masukkan data: ').split(' ')
bilangan_int = list(map(int, bilangan))

urutan_data(bilangan_int)
bilangan_str = list(map(str, bilangan_int))
hasil = ' '.join(bilangan_str)
print(hasil)