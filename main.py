# %% 
# import numpy  yang sudah terinstall
import numpy as np
# %%
#membuat aray numpy 1 dimensi

arei = np.array([1,2,3,4,5])
aree = np.array([[1,2,3],[4,5,6]])
arazero = np.zeros((2,3))
araone = np.ones((3,2), dtype=int)
ararange = np.arange(6)
aralin = np.linspace(0,1, num=5)

print(f"{arei} < adalah array/vektor 1 demsi \n")
print(f"{aree} < adalah array/matriks 2 dimensi\n")
print(f"{arazero} < ini adalah matriks 2X3 berisi 0\n")
print(f"{araone} < ini adalalh matriks 3x2 berisi 1\n {araone.dtype}\n")
print(f"{ararange} < ini adalah array np.arrange\n")
print(f"{ararange.reshape(2,3)} < ini adalah hasil dari .reshape(). kalo ini dari berapa samme berapa stepnya berapa\n")
print(f"{aralin} < ini adalah .linspace yaitu dari angaka berapa sampe berapa dibagi jadi berapa\n")
#caranya tu dengan bikin aja objek np yanng langsung ada listnya
#________________________________________________________________

# %%
# indexing
a = np.array([1,2,3,4,5,6])
b = np.arange(6).reshape(2,3)

print(f"{a} adalah vektor 1 dimensi\n")
print(f"{a[2]} indexing di urutan index ke 2\n")
print(f"{b} > matriks 2 dimensi\n")
print(f"{b[0,2]} = hasil dari baris ke 0 dan  kolom ke 2")
print(f"{b[1,1]} = hasil dari baris ke 1 dan  kolom ke 1")
# %%
#slicing
a = np.array([10,20,30,40,50,60,70])

print(a)
print(a[0:7:2])
print(a[1:7:2])
print(a[::4])
print(a[-1:])
print(a[:-1])
print(a[::-1])
print("\n")

b = np.arange(6).reshape(2,3)

print(f"{b}\n")
print(f"{b[0,1]}\n")
print(f"{b[0:,1]}\n")
print(f"{b[0:,0:2]}\n")


# %%
