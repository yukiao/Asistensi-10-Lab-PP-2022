
nilai = int(input('masukkan nilai: '))

if nilai >100:
    print('nilai tidak valid')
elif nilai>=90:
    print('nilai',nilai,"='A'")
elif nilai >=80:
    print("nilai",nilai,"='B'")
elif nilai>=70:
    print("nilai",nilai,"='C'")
elif nilai >=60:
    print('nilai',nilai,"='D")
elif nilai >=40:
    print('nilai',nilai,"='E'")
elif nilai <40:
    print("nilai",nilai,"='F'")