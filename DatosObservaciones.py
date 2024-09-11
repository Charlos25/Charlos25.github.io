from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get('https://cifras.biodiversidad.co/boyaca').text
soup = BeautifulSoup(html_text, 'lxml')

data_container = soup.find_all('div', class_ = 'bg-white flex flex-col justify-between text-black-2 py-3 px-4 w-auto gap-y-2 shadow-default hover:shadow-select')
#print(product_list2)

dato_pais = []
dato_name = []
# data_rows1 = []
# data_rows2 = []
data_valor1 = []
data_valor2 = []

# Iterar sobre los elementos y extraer la información
for data in data_container:
    pais = data.find('p', class_ = 'text-sm italic')
    nombre = data.find('a')
    
    data_pais = pais.text.strip()
    data_nombre = nombre.text.strip()
    # Buscar las tablas dentro de cada contenedor
    data_tables = data('table') # Esto devuelve una lista de tablas
    
    for table in data_tables:
        #print(table.prettify()) # Imprimir cada tabla con formato legible
        rows = table.find_all('th') # Buscar todas las filas de la tabla
        if len(rows) > 1:
            # data_row1 = rows[0].text.strip()
            data_row2 = rows[1].text.strip()
            # data_row3 = rows[2].text.strip()
            data_row4 = rows[3].text.strip()
            #print(data_row3)
            # data_rows1.append(data_row1) 
            data_valor1.append(data_row2.replace('.', '').replace('-','0')) 
            # data_rows2.append(data_row3)
            data_valor2.append(data_row4.replace('.', '').replace('-','0'))


    
    dato_pais.append(data_pais)   
    dato_name.append(data_nombre)


df=pd.DataFrame({
    'País':dato_pais,
    # 'Organización':dato_name,
    'Observaciones':data_valor1,
    'Especies':data_valor2,
})

agrupado=df

# print(df)
agrupado["Especies"] = agrupado["Especies"].astype(int, errors="raise")
agrupado["Observaciones"] = agrupado["Observaciones"].astype(int, errors="raise")
# agrupado = agrupado.drop ('Organización', axis = 1)
agrupado=df.groupby('País').sum()
print(agrupado.head())



# df.to_csv('observacionEspecies_cundinamarca.csv', index=False)
agrupado.to_csv('agrupado_boyaca.csv', index=True)