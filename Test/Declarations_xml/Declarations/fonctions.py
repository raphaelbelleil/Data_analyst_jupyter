# creation des listes de stockage
uuids = []
chemins = []
champss = []
valeurs = []
niveaux = []


# fonction scan xml et creation du tableau clé valeur
def scan_xml(root):
    # script de scan du xml
    for element, i in zip(root, range(len(root))):

        for enfant in element:
            chemin_complet_niv1 = element.tag + '/' + enfant.tag
            champs_niv1 = enfant.tag
            valeur_niv1 = enfant.text
            niveau = 1
            #print(chemin_complet_niv1, champs_niv1, valeur_niv1)

            uuid = root[i].findall('uuid')[0].text

            if valeur_niv1 : 

                uuids.append(uuid)
                chemins.append(chemin_complet_niv1)
                champss.append(champs_niv1)
                valeurs.append(valeur_niv1)
                niveaux.append(niveau)


            for enfant_niv2 in enfant:
                chemin_complet_niv2 = chemin_complet_niv1 + '/' + enfant_niv2.tag
                champs_niv2 = enfant_niv2.tag
                valeur_niv2 = enfant_niv2.text
                niveau = 2
                #print(chemin_complet_niv2, champs_niv2, valeur_niv2)

                if valeur_niv2 : 

                    uuids.append(uuid)
                    chemins.append(chemin_complet_niv2)
                    champss.append(champs_niv2)
                    valeurs.append(valeur_niv2)
                    niveaux.append(niveau)


                for enfant_niv3 in enfant_niv2:
                    chemin_complet_niv3 = chemin_complet_niv2 + '/' + enfant_niv3.tag
                    champs_niv3 = enfant_niv3.tag
                    valeur_niv3 = enfant_niv3.text
                    niveau = 3
                    #print(chemin_complet_niv3, champs_niv3, valeur_niv3)

                    if valeur_niv3 : 

                        uuids.append(uuid)
                        chemins.append(chemin_complet_niv3)
                        champss.append(champs_niv3)
                        valeurs.append(valeur_niv3)
                        niveaux.append(niveau)

                    for enfant_niv4 in enfant_niv3:
                        chemin_complet_niv4 = chemin_complet_niv3 + '/' + enfant_niv4.tag
                        champs_niv4 = enfant_niv4.tag
                        valeur_niv4 = enfant_niv4.text
                        niveau = 4
                        #print(chemin_complet_niv4, champs_niv4, valeur_niv4)      

                        if valeur_niv4 : 

                            uuids.append(uuid)
                            chemins.append(chemin_complet_niv4)
                            champss.append(champs_niv4)
                            valeurs.append(valeur_niv4)
                            niveaux.append(niveau)


                        for enfant_niv5 in enfant_niv4:
                            chemin_complet_niv5 = chemin_complet_niv4 + '/' + enfant_niv5.tag
                            champs_niv5 = enfant_niv5.tag
                            valeur_niv5 = enfant_niv5.text
                            niveau = 5
                            #print(chemin_complet_niv5, champs_niv5, valeur_niv5)   

                            if valeur_niv5 : 

                                uuids.append(uuid)
                                chemins.append(chemin_complet_niv5)
                                champss.append(champs_niv5)
                                valeurs.append(valeur_niv5)
                                niveaux.append(niveau)

                            for enfant_niv6 in enfant_niv5:
                                chemin_complet_niv6 = chemin_complet_niv5 + '/' + enfant_niv6.tag
                                champs_niv6 = enfant_niv6.tag
                                valeur_niv6 = enfant_niv6.text
                                niveau = 6
                                #print(chemin_complet_niv6, champs_niv6, valeur_niv6)   

                                if valeur_niv6 : 

                                    uuids.append(uuid)
                                    chemins.append(chemin_complet_niv6)
                                    champss.append(champs_niv6)
                                    valeurs.append(valeur_niv6)    
                                    niveaux.append(niveau)


                                for enfant_niv7 in enfant_niv6:
                                    chemin_complet_niv7 = chemin_complet_niv6 + '/' + enfant_niv7.tag
                                    champs_niv7 = enfant_niv7.tag
                                    valeur_niv7 = enfant_niv7.text
                                    niveau = 7
                                    #print(chemin_complet_niv7, champs_niv7, valeur_niv7) 

                                    if valeur_niv7 : 

                                        uuids.append(uuid)
                                        chemins.append(chemin_complet_niv7)
                                        champss.append(champs_niv7)
                                        valeurs.append(valeur_niv7)  
                                        niveaux.append(niveau)

                                    for enfant_niv8 in enfant_niv7:
                                        chemin_complet_niv8 = chemin_complet_niv7 + '/' + enfant_niv8.tag
                                        champs_niv8 = enfant_niv8.tag
                                        valeur_niv8 = enfant_niv8.text
                                        niveau = 8
                                        #print(chemin_complet_niv8, champs_niv8, valeur_niv8) 

                                        if valeur_niv8 : 

                                            uuids.append(uuid)
                                            chemins.append(chemin_complet_niv8)
                                            champss.append(champs_niv8)
                                            valeurs.append(valeur_niv8)  
                                            niveaux.append(niveau)


#########################################################################################################################

import re

def modif_chemins_declaration(valeur):
    ''' Fonction qui modifie les chemins pour pouvoir les utiliser comme champs de base de données sans avoir d'erreurs.
    - retire 'general/',
    - remplace les "/" par des "_", 
    - ajoute un "_" avant les majuscules,
    - transforme le tout en minuscule.'''
    
    valeur = valeur.replace('general/','')
    valeur = valeur.replace('/','_')
    valeur = re.sub(r'([A-Z])', r'_\1', valeur)
    valeur = valeur.lower()
    
    return valeur


#########################################################################################################################

from tqdm import tqdm

def id_table(nom_table, champs_levier):
    '''Création de l'id de la table'''
    # ajout de l'id de la table
    ids_table = []
    champs_table = []

    # creation de l'id de la table, qui s'incrémente à chaque nouvel élément, c'est à dire à chaque 'champs_repere_nouvelle_ligne'
    for element in nom_table['champs'].values:
        champs_table.append(element)
        i = champs_table.count(champs_levier) - 1
        ids_table.append(i)

    nom_table['id_table'] = ids_table

    return nom_table   

#########################################################################################################################

import pandas as pd
from sklearn.preprocessing import LabelEncoder

folder = 'D:/Fichiers_dev/test_xml/tables/'

# id_declarations = pd.read_csv(folder + 'data_nettoyees.csv')['id_declaration']

# encoder_id_declaration2 = LabelEncoder()

# encoder_id_declaration2.fit(id_declarations)

# encoder_id_declaration = encoder_id_declaration2


#########################################################################################################################


data3 = pd.read_csv(folder + 'data_nettoyees.csv')


def creation_table_avec_ressources(chemins, champs_levier, encoder_id_declaration):
    '''Création de la table à partir du chemin et du champs levier.'''

    # création de l'encoder
    # id_declarations = pd.read_csv(folder + 'data_nettoyees.csv')['id_declaration'].unique()
    # encoder_id_declaration = LabelEncoder()
    # encoder_id_declaration.fit(id_declarations)

    # chemins de la table
    mask_champs_table = (data3['chemins'].str.contains(chemins, na=False)) & ~(data3['chemins'].str.contains('montant/', na=False))
    
    # champs associés au chemin
    champs_table = data3[mask_champs_table]['chemins'].unique()
    print(champs_table)
    
    # creation de la table
    table = data3[data3['chemins'].isin(champs_table)][['id_declaration', 'champs', 'valeurs']]
    print(f"Table {chemins.replace('/items/', '')} créée")
    
    # encodage id_declaration
    table['id_declaration'] = encoder_id_declaration.transform(table['id_declaration'])
    

    # créer l'id de la table, qui s'incremente par rapport à un champs levier
    table = id_table(nom_table=table, champs_levier=champs_levier)
    
    
    # supression des doublons
    table = table.drop(table[table.duplicated(subset=['id_declaration','champs', 'id_table'], keep='last')].index)

    # pivot table
    table = table.pivot(index=['id_declaration', 'id_table'], columns='champs', values='valeurs').reset_index()
    
    # renommage id_table
    table = table.rename(columns={'id_table': f"id{chemins.replace('/items/', '')}"})
    print(f"Table {chemins.replace('/items/', '')} créée, avec {table.shape[0]} lignes et {table.shape[0]} colonnes.")
    print(f"Les colonnes : {table.columns}")

    # export en csv
    table.to_csv(folder + f'{table}.csv', index=False)
    print('Fichier exporté')

    return table