import csv
import argparse
import os

class Expense:

    def __init__(self,category,amount):
        self.category = category
        self.amount = amount

    def to_list(self):
        return [self.category,self.amount]

class BudgetManager:

    def __init__(self,filename='budget.csv'):
        self.filename = filename
        self.setupfile()

    def setupfile(self):
        if not os.path.exists(self.filename):
            with open(self.filename,mode='w',newline='',encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Kategorie','Betrag'])

    def addnewexpense(self,expense):
        with open(self.filename,'a',newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(expense.to_list())

    def get_total(self):
        total = 0.0
        with open (self.filename,'r',encoding= 'utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                total += float(row['Betrag'])
        return total

    def resetliste(self):
        with open(self.filename,mode='w',newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Kategorie','Betrag'])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    manager1 = BudgetManager()

    print("+++ BUDGET MANAGER V1.0 2026 APRIL +++")
    while True:

        print("\n--- MENÜ ---")
        print("1: Ausgabe hinzufügen")
        print("2: Gesamtausgaben anzeigen")
        print("3: CSV Datei zurücksetzen")
        print("4: Beenden")

        auswahl = input ("WÄHLEN SIE ZWISCHEN (1),(2),(3),(4)")

        if auswahl == "1":
            try:
                category = input("WAS HAST DU GEKAUFT? ")
                price = input("WIE VIEL HAT ES GEKOSTET? ")

                new_expense = Expense(category,price)

                manager1.addnewexpense(new_expense)
                print("+++NEUE AUSGABE",category,",",price,"€ WURDE HINZUGEFÜGT")
            except ValueError:
                print("+++FEHLER! ZAHLEN SIND DIE EINZIGE ZULÄSSIGE EINGABE!!!+++")

        elif auswahl == "2":
            print(f"+++ AUSGABEN INSGESAMT: {manager1.get_total():.2f}€ +++")

        elif auswahl == "3":
            manager1.resetliste()
            print("+++ LISTE WURDE ZURÜCKGESETZT! +++")

        elif auswahl == "4":
            print("+++ PROGRAMM WURDE BEENDET. +++")
            break


        else:
            print("+++ BITTE EINE GÜLTIGE EINGABE (1,2,3) ANGEBEN +++")
            manager1.resetliste()
