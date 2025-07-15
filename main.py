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
# indexing dan slicing
