import pandas as pd

data = pd.read_excel(r'resources/faturas/202301_fatura.xls')
data = data.drop(columns=data.columns[2])
data = data.drop(range(0,20))
data.columns = ["data", "descricao", "valor"]
df = pd.DataFrame(data, columns=['data', 'lançamento', 'valor'])
print(data)