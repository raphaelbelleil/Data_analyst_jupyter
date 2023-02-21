import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st


def stat_var(var): 

    var_IQR = var[var<(np.quantile(var, 0.75)+(1.5*(st.iqr(var))))]
    var_zscore = var[abs(st.zscore(var))<3]

    echantillon = [var, var_IQR, var_zscore, np.log(var), np.log(var_IQR), np.log(var_zscore)]

    colonne = ['echantillon_base', 'echantillon_base_IQR', 'echantillon_base_zscore', 
                        'echantillon_base_log', 'log_IQR', 'log_zscore']

    indicateur = ['moyenne', 'moyenne_min', 'moyenne_max', 'test_moyenne_10_%', 'mediane', 'mode', 'moyenne_tronquee',
                  'ecart_type', 'CV', 'IQR', 'skewness', 'skewness_pvalue', 'kurtosis', 'kurtosis_pvalue', 'ks_pvalue', 'shapiro_pvalue']


    liste = []

    for x in echantillon :
        moyenne = round(x.mean(),2)
        moyenne_min = round(x.mean()*0.9,2)
        moyenne_max = round(x.mean()*1.1,2)
        mediane = round(x.median(),2)
        mode = round(x.mode()[0],2)
        moyenne_tronquee = round(st.trim_mean(x, 0.05),2)
        if (moyenne_min<mediane<moyenne_max) & (moyenne_min<moyenne_tronquee<moyenne_max) : test_moyenne_10_pourcents = True
        else : test_moyenne_10_pourcents = False
        ecart_type = round(x.std(),2)
        CV = round(x.std()/x.mean(),2)
        IQR = round(np.quantile(x, 0.75) - (np.quantile(x, 0.25)),2)
        skewness = round(x.skew(),2)
        skewness_pvalue = st.skewtest(x)[1]
        kurtosis = round(x.kurtosis(),2)
        kurtosis_pvalue = st.kurtosistest(x)[1]
        ks_pvalue = round(st.kstest(x, 'norm')[1],2)
        shapiro_pvalue = round(st.shapiro(x)[1],2)
        liste1 = [moyenne, moyenne_min, moyenne_max, test_moyenne_10_pourcents, mediane, mode, moyenne_tronquee, 
                  ecart_type, CV, IQR, skewness, skewness_pvalue, kurtosis, kurtosis_pvalue, ks_pvalue, shapiro_pvalue]
        liste.append(liste1) 

    dictionnaire = {colonne : liste for colonne, liste in zip(colonne, liste)}
    df = pd.DataFrame(dictionnaire, index=indicateur)
    
    return df