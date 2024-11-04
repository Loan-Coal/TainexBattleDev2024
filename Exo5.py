#NE PAS TOUCHER
sequences = ['PCCCPHDCDC', 'CCHDHCCCPP', 'PPDCHDCPHC', 'HCHCHCCDDDP', 'PHCPHCCPHPC', 'CCDDPDCCHH', 'HCPDDDPCDDHD', 'HDHHPHPDDP', 'CDCHPPPPCH', 'PPHHDHHHCHCD']
storages = ['DHPC', 'CPDCC', 'DCPHH', 'CPCCP', 'HCPP']
#NE PAS TOUCHER


time_ref = {'P':1, 'H':2, 'C':3, 'D':4};

time_sequences = []
time_storages = []

for i in range(len(sequences)):

    c = 0

    for k in range(len(sequences[i])):

        c+=time_ref[sequences[i][k]]

    time_sequences.append(c)

for j in range(len(storages)):

    c = 0

    for m in range(len(storages[j])):

        c+=time_ref[storages[j][m]]

    time_storages.append(c)

sq = max(time_sequences)
st = max(time_storages)

for p in range(len(time_sequences)):

    if time_sequences[p] == sq:

        sq_pattern = sequences[p]

for q in range(len(time_storages)):

    if time_storages[q] == st:

        st_pattern = storages[q]

print(str(sq_pattern) + str(st_pattern) + "_" + str(sq + st))