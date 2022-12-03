class Kubus :
    def __init__ (self,lebar,tinggi,panjang):
        self.__lebar = (lebar) 
        self.__panjang = (panjang )
        self.__tinggi = (tinggi)
        
    def set_lebar (self, x) :
        self.__lebar = x
        return self.__lebar
    def set_panjang (self, x) :
        self.__panjang = x
        return self.__panjang
    def set_tinggi (self, x) :
        self.__tinggi = x
        return self.__tinggi
    def set_massa (self, x) :
        self.__massa = x
        return self.__massa
    def get_massa(self):
        return (self.__massa)
    def get_massa_jenis (self) :
        self.__massajenis = self.__massa/(self.__lebar*self.__panjang*self.__tinggi)
        return (self.__massajenis)
lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())
kubus = Kubus(lebar, tinggi, panjang)
kubus.set_massa(massa)
print("Massa Jenis =", kubus.get_massa_jenis())
kubus.set_massa(massa*2)
print("Massa Jenis =", kubus.get_massa_jenis())




