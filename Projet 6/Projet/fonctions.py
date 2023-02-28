import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st


def stat_var(var): 

    # variable échantillon de base + méthode IQR + méthode zscore
    
    var_IQR = var[var<(np.quantile(var, 0.75)+(1.5*(st.iqr(var))))]
    var_zscore = var[abs(st.zscore(var))<3]

    # transformations au logarithme 
    var_log = np.log(var)
    log_IQR = var_log[var_log<(np.quantile(var_log, 0.75)+(1.5*(st.iqr(var_log))))]
    log_zscore = var_log[abs(st.zscore(var_log))<3]

    # transformations à la racine
    var_sqrt = np.sqrt(var)
    sqrt_IQR = var_sqrt[var_sqrt<(np.quantile(var_sqrt, 0.75)+(1.5*(st.iqr(var_sqrt))))]
    sqrt_zscore = var_sqrt[abs(st.zscore(var_sqrt))<3]

    # mes 9 échantillons
    echantillon = [var, var_IQR, var_zscore, var_log, log_IQR, log_zscore, var_sqrt, sqrt_IQR, sqrt_zscore]

    # les colonnes du dataframe correspondant aux 9 échantillons
    colonne = ['echantillon_base', 'echantillon_base_IQR', 'echantillon_base_zscore', 
               'echantillon_base_log', 'log_IQR', 'log_zscore',
               'echantillon_base_sqrt', 'sqrt_IQR', 'sqrt_zscore']

    # les indicateurs qu'on va calculer pour chaque échantillon
    indicateur = ['moyenne', 'moyenne_min', 'moyenne_max', 'test_moyenne_10_pourcents','mediane', 'mode', 'moyenne_tronquee', 
                  'ecart_type', 'CV', 'IQR', 'outlier_max_iqr', 'outlier_min_iqr', 'nb_outlier_iqr', 'outlier_max_zscore',
                  'outlier_min_zscore', 'nb_outlier_zscore', 'skewness', 'skewness_pvalue', 'kurtosis', 'kurtosis_pvalue',
                  'ks_pvalue', 'shapiro_pvalue']
    
    
    # création du dataframe

    liste = []

    for x in echantillon :
        moyenne = round(x.mean(),4)
        moyenne_min = round(x.mean()*0.9,4)
        moyenne_max = round(x.mean()*1.1,4)
        mediane = round(x.median(),4)
        mode = round(x.mode()[0],4)
        moyenne_tronquee = round(st.trim_mean(x, 0.05),4)
        if (moyenne_min<mediane<moyenne_max) & (moyenne_min<moyenne_tronquee<moyenne_max) : test_moyenne_10_pourcents = True
        else : test_moyenne_10_pourcents = False
        ecart_type = round(x.std(),4)
        CV = round(x.std()/x.mean(),4)
        IQR = round(np.quantile(x, 0.75) - (np.quantile(x, 0.25)),4)
        outlier_max_iqr = np.quantile(x, 0.75) + 1.5*IQR
        outlier_min_iqr = max(np.quantile(x, 0.25) - 1.5*IQR,0)
        nb_outlier_iqr = x[(x>outlier_max_iqr)|(x<outlier_min_iqr)].count()
        outlier_max_zscore = x[abs(st.zscore(x))<3].max()
        outlier_min_zscore = max(np.mean(x)-3*np.std(x),0)
        nb_outlier_zscore = x[abs(st.zscore(x))>3].count()
        skewness = round(x.skew(),4)
        skewness_pvalue = round(st.skewtest(x)[1],4)
        kurtosis = round(x.kurtosis(),4)
        kurtosis_pvalue = round(st.kurtosistest(x)[1],4)
        ks_pvalue = round(st.kstest(x, 'norm')[1],4)
        shapiro_pvalue = round(st.shapiro(x)[1],4)
        liste1 = [moyenne, moyenne_min, moyenne_max, test_moyenne_10_pourcents, mediane, mode, moyenne_tronquee, 
                  ecart_type, CV, IQR, outlier_max_iqr, outlier_min_iqr, nb_outlier_iqr, outlier_max_zscore,
                  outlier_min_zscore, nb_outlier_zscore, skewness, skewness_pvalue, 
                  kurtosis, kurtosis_pvalue, ks_pvalue, shapiro_pvalue]
        liste.append(liste1) 

    dictionnaire = {colonne : liste for colonne, liste in zip(colonne, liste)}
    df = pd.DataFrame(dictionnaire, index=indicateur)

    df
    
    return df





def hist_var(var) : 

    # variable échantillon de base + méthode IQR + méthode zscore
    
    var_IQR = var[var<(np.quantile(var, 0.75)+(1.5*(st.iqr(var))))]
    var_zscore = var[abs(st.zscore(var))<3]

    # transformations au logarithme 
    var_log = np.log(var)
    log_IQR = var_log[var_log<(np.quantile(var_log, 0.75)+(1.5*(st.iqr(var_log))))]
    log_zscore = var_log[abs(st.zscore(var_log))<3]

    # transformations à la racine
    var_sqrt = np.sqrt(var)
    sqrt_IQR = var_sqrt[var_sqrt<(np.quantile(var_sqrt, 0.75)+(1.5*(st.iqr(var_sqrt))))]
    sqrt_zscore = var_sqrt[abs(st.zscore(var_sqrt))<3]

    # mes 9 échantillons
    echantillon = [var, var_IQR, var_zscore, var_log, log_IQR, log_zscore, var_sqrt, sqrt_IQR, sqrt_zscore]

    # les colonnes du dataframe correspondant aux 9 échantillons
    colonne = ['echantillon_base', 'echantillon_base_IQR', 'echantillon_base_zscore', 
               'echantillon_base_log', 'log_IQR', 'log_zscore',
               'echantillon_base_sqrt', 'sqrt_IQR', 'sqrt_zscore']

    # les indicateurs qu'on va calculer pour chaque échantillon
    indicateur = ['moyenne', 'moyenne_min', 'moyenne_max', 'test_moyenne_10_pourcents','mediane', 'mode', 'moyenne_tronquee', 
                  'ecart_type', 'CV', 'IQR', 'outlier_max_iqr', 'outlier_min_iqr', 'nb_outlier_iqr', 'outlier_max_zscore',
                  'outlier_min_zscore', 'nb_outlier_zscore', 'skewness', 'skewness_pvalue', 'kurtosis', 'kurtosis_pvalue',
                  'ks_pvalue', 'shapiro_pvalue']
    
    plt.figure(figsize=(30,15))

    for x, i, titre in zip(echantillon, range(len(echantillon)), colonne):
        plt.subplot((len(echantillon))//3, (len(echantillon))//3,i+1)
        plt.title(titre, size=16)
        plt.xlabel(' ')
        sns.histplot(x)
    
    
    return(plt.show())







def boxplot_var(var):
    
    # variable échantillon de base + méthode IQR + méthode zscore
    
    var_IQR = var[var<(np.quantile(var, 0.75)+(1.5*(st.iqr(var))))]
    var_zscore = var[abs(st.zscore(var))<3]

    # transformations au logarithme 
    var_log = np.log(var)
    log_IQR = var_log[var_log<(np.quantile(var_log, 0.75)+(1.5*(st.iqr(var_log))))]
    log_zscore = var_log[abs(st.zscore(var_log))<3]

    # transformations à la racine
    var_sqrt = np.sqrt(var)
    sqrt_IQR = var_sqrt[var_sqrt<(np.quantile(var_sqrt, 0.75)+(1.5*(st.iqr(var_sqrt))))]
    sqrt_zscore = var_sqrt[abs(st.zscore(var_sqrt))<3]

    # mes 9 échantillons
    echantillon = [var, var_IQR, var_zscore, var_log, log_IQR, log_zscore, var_sqrt, sqrt_IQR, sqrt_zscore]

    # les colonnes du dataframe correspondant aux 9 échantillons
    colonne = ['echantillon_base', 'echantillon_base_IQR', 'echantillon_base_zscore', 
               'echantillon_base_log', 'log_IQR', 'log_zscore',
               'echantillon_base_sqrt', 'sqrt_IQR', 'sqrt_zscore']

    # les indicateurs qu'on va calculer pour chaque échantillon
    indicateur = ['moyenne', 'moyenne_min', 'moyenne_max', 'test_moyenne_10_pourcents','mediane', 'mode', 'moyenne_tronquee', 
                  'ecart_type', 'CV', 'IQR', 'outlier_max_iqr', 'outlier_min_iqr', 'nb_outlier_iqr', 'outlier_max_zscore',
                  'outlier_min_zscore', 'nb_outlier_zscore', 'skewness', 'skewness_pvalue', 'kurtosis', 'kurtosis_pvalue',
                  'ks_pvalue', 'shapiro_pvalue']
    
    
    plt.figure(figsize=(15,10))

    plt.subplot(3,1,1)
    plt.boxplot(echantillon[0:3], showfliers=False)
    plt.xticks(range(1, 1+len(echantillon)//3), colonne[0:3], size=8)

    plt.title('Boites à moustaches des prix échantillons de base')

    plt.subplot(3,1,2)
    plt.boxplot(echantillon[3:6], showfliers=False)
    plt.xticks(range(1, 1+len(echantillon)//3), colonne[3:6], size=8)

    plt.title('Boites à moustaches des prix échantillons passés au logarithme')


    plt.subplot(3,1,3)
    plt.boxplot(echantillon[6:9], showfliers=False)
    plt.xticks(range(1, 1+len(echantillon)//3), colonne[6:9], size=8)

    plt.title('Boites à moustaches des prix échantillons passés à la racine')
    


    return(plt.show())