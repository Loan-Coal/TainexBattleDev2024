#NE PAS TOUCHER
flux = ['V1A:1617', 'V1B:2096', 'V1C:1555']
network = ['V1A:V2A,V2C,V2D', 'V1B:V2B,V2C,V2A', 'V1C:V2D,V2A,V2C', 'V2A:V3B,V3D,V3G,V3E,V3F', 'V2B:V3G,V3A,V3E,V3F,V3B', 'V2C:V3C,V3D,V3F,V3G', 'V2D:V3F,V3G,V3E', 'V3A:V4J,V4G,V4I,V4E,V4D,V4K', 'V3B:V4F,V4E,V4G,V4H', 'V3C:V4L,V4D,V4G,V4B', 'V3D:V4J,V4H,V4F,V4D,V4E', 'V3E:V4J,V4B,V4D,V4K,V4A', 'V3F:V4K,V4J,V4D,V4E,V4H', 'V3G:V4E,V4D,V4L,V4C']
#NE PAS TOUCHER


#Dictionnaires pour les flux
flux_dict = {}
vanne_dict = {}

for f in flux:
    vanne, flow = f.split(':')
    flux_dict[vanne] = int(flow)

#Repartition dans differents niveaux
def repartition(network, flux_dict, vanne_dict):
    for connection in network:
        parent_vanne, children = connection.split(':')
        children_vannes = children.split(',')

        flux_par_child = flux_dict[parent_vanne] // len(children_vannes)

        for child in children_vannes:
            if child in vanne_dict:
                vanne_dict[child] += flux_par_child
            else:
                vanne_dict[child] = flux_par_child

    return vanne_dict

#Traiter les connexions du niveau 1 à 3

vanne_dict = repartition(network[:3], flux_dict, vanne_dict)  # Niveau 1
flux_dict = vanne_dict.copy()

vanne_dict = repartition(network[3:7], flux_dict, vanne_dict)  # Niveau 2
flux_dict = vanne_dict.copy()

vanne_dict = repartition(network[7:13], flux_dict, vanne_dict)  # Niveau 3
flux_dict = vanne_dict.copy()

vanne_dict = repartition(network[13:], flux_dict, vanne_dict)  # Niveau 4



vannes_niveau_4 = {v: flux for v, flux in vanne_dict.items() if v.startswith('V4')}

max_flux = max(vannes_niveau_4.values())
vannes_max_flux = [v for v, flux in vannes_niveau_4.items() if flux == max_flux]

result = f"{max_flux}_{''.join(sorted(vannes_max_flux))}"

print(result)