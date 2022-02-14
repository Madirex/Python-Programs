import os
import pandas as pd
import matplotlib.pyplot as plt

class PandasCsv:
    def load_dataset(self):
        PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
        RESOURCES_DIR = PROJECT_DIR + "/resources/"
        return pd.read_csv(RESOURCES_DIR + "titanic3.csv")

    def __init__(self):
        #Cargar dataset
        print("\n🛳️  Cargando dataset...")
        df = self.load_dataset()
        
        #Mostrar primeras filas
        num = int(input("Introduce el número de filas a mostrar:"))
        print("\n🛳️  Mostrando las primeras " + str(num) + " filas indicadas por teclado:")
        print(df.head(num))

        #Media pasajeros
        print("\n🛳️  La media de edad de los pasajeros es: " + str(df[['age']].mean(axis='index')))

        #Histograma
        print("\n🛳️  Creando histograma...")
        plt.hist(df['age'],bins=1000)
        plt.show()

        #Número de pasajeros con billetes de primera, segunda y tercera clase.
        print("\n🛳️  Cantidad de personas según el tipo de clase de billete:")
        print(df.groupby('pclass').size())
        
        #Tabla pivot con la tasa de supervivencia en función del tipo de billete.
        def survivers(survivers):
            if survivers == 1:
                return "Supervivientes"
            else:
                return "Muertos"
        
        df['Supervivencia'] = df['survived'].apply(survivers)
        survived = pd.DataFrame(df.survived.value_counts(normalize=True)*100).reset_index()
        survived.columns = ['survived', '% de supervivencia']
        df = pd.merge(left=df, right=survived, how='inner', on=['survived'])
        table = pd.pivot_table(df, index=['Supervivencia', '% de supervivencia', 'pclass'])
        print("\n🛳️  Tabla de tasa de supervivencia según tipo de clase de billete:")
        print(table)

if __name__ == '__main__':
    PandasCsv()