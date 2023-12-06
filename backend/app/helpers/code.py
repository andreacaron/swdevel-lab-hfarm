import csv 
import pandas as pd

dove_alloggiare = '/app/app/dove-alloggiare.csv'
with open(dove_alloggiare, "r", newline= "", encoding="utf-8") as file_csv:
    lettore_csv = csv.reader(file_csv)
    print('ciao')


    for riga in lettore_csv:
        print(riga)


# Creazione di un DataFrame 
df = pd.read_csv('/app/app/dove-alloggiare.csv')

# Controllo dei valori mancanti in tutto il DataFrame
valori_mancanti_totali = df.isnull().sum().sum()

if valori_mancanti_totali > 0:
    print(f"È presente un totale di {valori_mancanti_totali} valori mancanti nel DataFrame.")
    # Mostra il conteggio dei valori mancanti per ogni colonna
    valori_mancanti_per_colonna = df.isnull().sum()
    print("Conteggio dei valori mancanti per ogni colonna:")
    print(valori_mancanti_per_colonna)
else:
    print("Non ci sono valori mancanti nel DataFrame.")

# Eliminazione NA values
df_cleaned = df.dropna()
print(df_cleaned)

# Check per vedere che non ci siano più valori mancanti 
ci_sono_na = df_cleaned.isna().any().any()
if ci_sono_na:
    print("Ci sono valori mancanti nel DataFrame.")
else:
    print("Non ci sono valori mancanti nel DataFrame.")

