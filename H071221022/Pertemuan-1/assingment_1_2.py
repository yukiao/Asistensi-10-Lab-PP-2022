waktu= int(input("maasukan detik : "))

jam   = (waktu//3600)
menit = (waktu%3600)//(60)
detik = (waktu%3600)%(60)

print (f'{jam} : {menit} : {detik}')
