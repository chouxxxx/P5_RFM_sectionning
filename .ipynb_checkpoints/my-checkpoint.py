import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def desc(seris):
    display("                                 %missings:", seris.isna().mean())
    display("                                  describe:", seris.describe())
    
def desc2(seris):
    display("                                 %missings:", seris.isna().mean())
    plt.figure(figsize=(20, 12)) #(16, 9)
    sns.histplot(seris, kde=True, bins=int(seris.max()-seris.min()))
    plt.title(seris.columns,fontsize=16)
    plt.xlabel('values',fontsize=16)
    plt.xticks(fontsize=14)
    plt.ylabel('occurences',fontsize=16)
    plt.yticks(fontsize=14)
    plt.figure(figsize=(4, 6))
    sns.boxplot(x=seris)
    plt.show()
    
def desc_FULL(seris):
    display("                                 %missings:", seris.isna().mean())
    display("                                  missings:", seris.isna().sum())
    display("                                      mode:", seris.mode())
    display("                                  describe:", seris.describe())
    display("                      value_counts.head(7):", seris.value_counts().head(7))
    plt.figure(figsize=(20, 12))
    sns.histplot(seris, kde=True, bins=int(seris.max()-seris.min()))
    plt.title(seris.columns,fontsize=16)
    plt.xlabel('values',fontsize=16)
    plt.xticks(fontsize=14)
    plt.ylabel('occurences',fontsize=16)
    plt.yticks(fontsize=14)
    print("                      skew (>0 <=> exp(-)):", seris.skew())
    print("             kurtosis (>0 <=> spike>gauss):", seris.kurtosis())
    plt.figure(figsize=(20, 12))
    #df.boxplot(column='additives_n')
    #sns.boxplot(x='energy_100g',y='carbohydrates_100g',data=df,hue='nutrition_grade_fr',palette='BrBG')
    sns.boxplot(x=seris)
    plt.show()

def read_csv(dfstr):
    daf = pd.read_csv(dfstr)
    try:
        daf["Unnamed: 0"]
    except KeyError:
        print("Y'avait pas de colonne 'Unnamed: 0'")
    else:
        daf = daf.drop('Unnamed: 0', axis=1)
    return daf

def resindx(daf):
    daf = daf.reset_index()
    try:
        daf = daf.drop(columns='level_0')
        print("Une colonne 'level_0' indésirable a été supprimée.")
    except:
        print("Il n'y avait pas de colonne 'level_0' indésirable à supprimer.")
    try:
        daf = daf.drop(columns='index')
        print("Une colonne 'index' indésirable a été supprimée.")
    except:
        print("Il n'y avait pas de colonne 'index' indésirable à supprimer.")
    print(daf.shape)
    return daf

def hstplot(seris, strlog='log de ', hstsize=20):
    hst = seris.copy()
    hst.replace([np.inf, -np.inf], np.nan, inplace=True)
    hst.dropna(inplace=True)
    hst_val, hst_bin = np.histogram(hst, bins=50)
    hst = pd.DataFrame()
    hst.loc[:,'hst_bin'] = hst_bin[:-1] # Ou alors décaler d'un demi bin avec bins_mean = [0.5 * (bins[i] + bins[i+1]) for i in range(len(n))].
    hst.loc[:,'hst_val'] = hst_val
    hst = hst[hst['hst_val'] != 0]
    with sns.axes_style("whitegrid"):
        sns.scatterplot(hst['hst_bin'], hst['hst_val'], legend=None, s=hstsize)
    plt.title(('Hist de ' + strlog + seris.name),fontsize=16)
    plt.xlabel((strlog + seris.name),fontsize=16)
    plt.xticks(fontsize=14)
    plt.ylabel('Nb de clients',fontsize=16)
#    plt.ylabel('Nb de bâtiments',fontsize=16)
    plt.yticks(fontsize=14)
    plt.legend