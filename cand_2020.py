import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
low_memory=False



df = pd.read_csv('DataAnalysisConsulta_cand_2020\consulta_cand_2020.csv',
                 delimiter=';',
                 encoding='iso-8859-1',
                 usecols={"DT_GERACAO", "HH_GERACAO", "ANO_ELEICAO", "CD_TIPO_ELEICAO", "NM_TIPO_ELEICAO", "NR_TURNO", "CD_ELEICAO", "DS_ELEICAO", "DT_ELEICAO", "TP_ABRANGENCIA", "SG_UF", "SG_UE", "NM_UE", "CD_CARGO", "DS_CARGO", "SQ_CANDIDATO", "NR_CANDIDATO", "NM_CANDIDATO", "NM_URNA_CANDIDATO", "NM_SOCIAL_CANDIDATO", "NR_CPF_CANDIDATO", "NM_EMAIL", "CD_SITUACAO_CANDIDATURA", "DS_SITUACAO_CANDIDATURA", "CD_DETALHE_SITUACAO_CAND", "DS_DETALHE_SITUACAO_CAND", "TP_AGREMIACAO", "NR_PARTIDO", "SG_PARTIDO", "NM_PARTIDO", "SQ_COLIGACAO", "NM_COLIGACAO", "DS_COMPOSICAO_COLIGACAO", "CD_NACIONALIDADE", "DS_NACIONALIDADE", "SG_UF_NASCIMENTO", "CD_MUNICIPIO_NASCIMENTO", "NM_MUNICIPIO_NASCIMENTO", "DT_NASCIMENTO", "NR_IDADE_DATA_POSSE", "NR_TITULO_ELEITORAL_CANDIDATO", "CD_GENERO", "DS_GENERO", "CD_GRAU_INSTRUCAO", "DS_GRAU_INSTRUCAO", "CD_ESTADO_CIVIL", "DS_ESTADO_CIVIL", "CD_COR_RACA", "DS_COR_RACA", "CD_OCUPACAO", "DS_OCUPACAO", "VR_DESPESA_MAX_CAMPANHA", "CD_SIT_TOT_TURNO", "DS_SIT_TOT_TURNO", "ST_REELEICAO", "ST_DECLARAR_BENS", "NR_PROTOCOLO_CANDIDATURA", "NR_PROCESSO", "CD_SITUACAO_CANDIDATO_PLEITO", "DS_SITUACAO_CANDIDATO_PLEITO", "CD_SITUACAO_CANDIDATO_URNA", "DS_SITUACAO_CANDIDATO_URNA", "ST_CANDIDATO_INSERIDO_URNA"})

print(df.describe())

print(df.head(n=10))
print(df.tail())
print(df["SG_UF"].unique())
print(df["SG_UF"].value_counts())
print(df["SG_UF"].value_counts(normalize = True))

#print(df.groupby("NO_MUNICIPIO_ESCOLA").mean())

##grafio ta ficando grande demais
# plt.bar(df["SG_UF_ESCOLA"], df["NU_MEDIA_MT"], color="red")
# plt.show()
#print(df["NU_MATRICULAS"].plot.hist(bins=30, edgecolor='black'))
print(df.sample(10).sort_values(by='CD_TIPO_ELEICAO'))
# print(df.sample(3).sort_values(by= "NU_MEDIA_CN"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_CH"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_LP"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_MT"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_RED"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_OBJ"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_TOT"))
# print(df.sample(3).sort_values(by= "NU_TAXA_APROVACAO"))
# print(df.sample(3).sort_values(by= "NU_TAXA_REPROVACAO"))
# print(df.sample(3).sort_values(by= "NU_TAXA_ABANDONO"))
# print(df.sample(3).sort_values(by= "NU_TAXA_PARTICIPACAO"))