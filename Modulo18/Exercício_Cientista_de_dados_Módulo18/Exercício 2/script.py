import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import statsmodels.formula.api as smf

def Qualitativa (df, y, x):
    # Criando bivariada para 'age' através do pd.crosstab().
    # Nº de saudáveis
    # Nº de doentes
    # Total
    tab = pd.crosstab(df[x], df[y], margins=True, margins_name='Total', dropna=True)

    # Quantidade média de doentes.
    tab['media_doentes'] = tab['Doente']/tab['Total']

    # Odds
    tab['Chance_Odds_Doentes'] = tab['Doente']/tab['Saudavel']

    # Odds ratio
    tab['RC_vs_total_OddsRatio'] = tab['Chance_Odds_Doentes']/tab.loc['Total', 'Chance_Odds_Doentes']

    # Logito (LOG(Odds))
    tab['Logito'] = np.log(tab['Chance_Odds_Doentes'])

    # Log do Odds ratio - Weight of Evidence (WOE)
    tab['WOE'] = np.log(tab['RC_vs_total_OddsRatio'])

    return tab