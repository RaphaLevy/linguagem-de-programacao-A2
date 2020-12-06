import Conexao as con
import pandas as pd
from datetime import datetime

"""

INFO DO DATAFRAME, PODE APAGAR DEPOIS


<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5936 entries, 0 to 5935
Data columns (total 11 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   AggregationMethod  5936 non-null   object 
 1   Date               5936 non-null   object 
 2   Version            5936 non-null   float64
 3   AirportName        5936 non-null   object 
 4   PercentOfBaseline  5936 non-null   int64  
 5   Centroid           5936 non-null   object 
 6   City               5936 non-null   object 
 7   State              5936 non-null   object 
 8   ISO_3166_2         5936 non-null   object 
 9   Country            5936 non-null   object 
 10  Geography          5936 non-null   object 
dtypes: float64(1), int64(1), object(9)
memory usage: 510.2+ KB
"""


class CovidAeroporto():
    # Cada função é referente à uma pergunta
    
    def __init__(self):
        self.conexao = con.Conexao()
        self.df = self.conexao.getCovidImpactDataFrame()
        self.conexao.fecharConexao()    
        
    def voosPorBaseline(self):
        return pd.DataFrame(self.df[["Country", "PercentOfBaseline"]].groupby("Country").mean())
    
    # # Em que cidades dos EUA o número de voos aumentou?  
    # # Em que cidades dos EUA o número de voos diminuiu?
    def baselinePorCidade(self):
        return pd.DataFrame(self.df[["City", "PercentOfBaseline"]].groupby("City").mean())
    
    # # Qual dia teve o maior número de voos internacionalmente?
    def maiorNumeroVoos(self):
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["QtdVoos"]
        aux_df["Weekday"] = [date.weekday() for date in aux_df.index.values]
        return aux_df.sort_values(by = aux_df["QtdVoos"], ascending = False)
    
    # # Qual dia teve o menor número de voos internacionalmente?
    def menorNumeroVoos(self):
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["QtdVoos"]
        aux_df["Weekday"] = [date.weekday() for date in aux_df.index.values]
        return aux_df.sort_values(by = aux_df["QtdVoos"], ascending = True)
    
    # # Comparando o dia com mais voos com o mesmo dia da semana no período de baseline, o número de voos aumentou ou abaixou?
    # # Comparando o dia com menos voos com o mesmo dia da semana no período de baseline, o número de voos aumentou ou abaixou?
    def baselinePorDia(self):
        return pd.DataFrame(self.df[["Date", "PercentOfBaseline"]].groupby("Date").mean())
    

# -----------Já tava aqui antes

# print(data1.keys())

# print(data1.head())
# print(data1.describe())

# df = pd.DataFrame(data1)
# print(df)

# ##############PLOT COMPARACAO DE VOOS POR AEROPORTO###############
# print(data1.groupby("Date").mean())
# print(data1.groupby("AirportName").mean())
# print(data1.groupby(["Date", "AirportName"]).mean())

# viagens_por_aeroporto = data1.groupby(["Date", "AirportName"]).mean()
# print(type(viagens_por_aeroporto))

# viagens_por_aeroporto["PercentOfBaseline"].plot.bar()
# plt.show()
