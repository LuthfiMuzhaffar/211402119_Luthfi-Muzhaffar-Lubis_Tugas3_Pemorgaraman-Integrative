class BMI:
    def __init__(self, weight, height):
        self._weight = weight  # Simpan berat dalam kilogram
        self._height = height  # Simpan tinggi dalam meter

    @property
    def Weight(self):
        return self._weight

    @property
    def Height(self):
        return self._height

    def BMI_Value(self):
        # Hitung BMI menggunakan rumus yang diberikan
        return self._weight / (self._height ** 2)

    def __eq__(self, other):
        # Override metode __eq__ untuk membandingkan dua objek BMI
        if isinstance(other, BMI):
            return self._weight == other.Weight and self._height == other.Height
        return False

# Contoh penggunaan:
bmi1 = BMI(80, 1.80)  # Berat: 80 kg, Tinggi: 1.80 m
bmi2 = BMI(60, 1.70)  # Berat: 60 kg, Tinggi: 1.70 m

print("BMI 1:", bmi1.BMI_Value())
print("BMI 2:", bmi2.BMI_Value())

# Bandingkan dua objek BMI
if bmi1 == bmi2:
    print("BMI 1 sama dengan BMI 2")
else:
    print("BMI 1 tidak sama dengan BMI 2")
