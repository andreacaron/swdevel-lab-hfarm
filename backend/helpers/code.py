import csv 

dove_alloggiare = '/app/app/dove-alloggiare.csv'
with open(dove_alloggiare, "r", newline= "", encoding="utf-8") as file_csv:
    lettore_csv = csv.reader(file_csv)


    for riga in lettore_csv:
        print(riga)