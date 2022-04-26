import numpy as np
import OUTfile_reader

Pr = 1e-1
# R0s = np.array([1.45, 3.0, 5.0, 7.0, 9.0])
R0s = np.array([1.5, 3.0, 5.0, 7.0, 9.0])
HB = 0.1
Pm = 0.1

names = ["R0", "urms", "TEMPrms", "CHEMrms", "Brms", "flux_Temp", "flux_Chem", "u_max(3)",
         "uxrms", "uyrms", "uzrms", "Bxrms", "Byrms", "Bzrms", "diss_Temp", "diss_Chem"]

data_array = np.zeros((len(R0s), len(names)), dtype=np.float64)
for ri, r0 in enumerate(R0s):
    data_array[ri, 0] = r0
    for ni, name in enumerate(names[1:]):
        data_array[ri, ni+1] = OUTfile_reader.get_avg_from_DNS(Pr, r0, HB, Pm, name)

fname = 'extracted_data/Pr{}_HB{}_Pm{}_R0scan_data.txt'.format(Pr, HB, Pm)

np.savetxt(fname, data_array, header=' '.join(names))

print('done')
