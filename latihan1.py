#mendefikinisikan kelas
class KelilingLingkaran(object):
	def __init__(self, phi, r):
		self.phi = phi
		self.jarijari = r
	def hitungKeliling(self):
		return 2 * self.phi * self.jarijari

def main():
	# membuat objek pertama
	lingkaran1 = KelilingLingkaran(3.14, 5)

	#menggunaan objek ertama
	print("Objek keliling lingkaran1")
	print("phi\t: ", lingkaran1.phi)
	print("jarijari\t: ", lingkaran1.jarijari)
	print("Keliling\t= ", lingkaran1.hitungKeliling())

	lingkaran2 = KelilingLingkaran(3.14, 10)

	#menggunaan objek ertama
	print("\nObjek keliling lingkaran2")
	print("phi\t: ", lingkaran2.phi)
	print("jarijari\t: ", lingkaran2.jarijari)
	print("Keliling\t= ", lingkaran2.hitungKeliling())

if __name__ == "__main__":
	main()

class LuasLingkaran(object):

	def __init__(self, phi, r):
		self.phi = phi
		self.jarijari = r
	def hitungLuas(self):
		return self.phi * self.jarijari * self.jarijari

def main():
	# membuat objek pertama
	lingkaran1 = LuasLingkaran(3.14, 6)

	#menggunaan objek ertama
	print("Objek luas lingkaran1")
	print("phi\t: ", lingkaran1.phi)
	print("jarijari\t: ", lingkaran1.jarijari)
	print("Luas\t= ", lingkaran1.hitungLuas())

	lingkaran2 = LuasLingkaran(3.14, 8)

	#menggunaan objek pertama
	print("\nObjek luas lingkaran2")
	print("phi\t: ", lingkaran2.phi)
	print("jarijari\t: ", lingkaran2.jarijari)
	print("Luas\t= ", lingkaran2.hitungLuas())

if __name__ == "__main__":
	main()
