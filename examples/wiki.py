import wikipedia as wiki
from bs4 import BeautifulSoup
from wikipedia.exceptions import DisambiguationError
wiki.set_lang("es") #solo resultados en español para que se puedan encontrar las palabras buscadas, y evitar errores de lenguaje

articulos = []
urls = []

def articulo_wiki():
    while True:
        titulo_articulo = wiki.random()
        if '/' not in titulo_articulo:
            return titulo_articulo
        
for i in range(30):
    titulo_articulo = articulo_wiki()
    try:
        # Recuperar un articulo aleatorio de wikipedia
        contenido=wiki.page(titulo_articulo).content
        soup=BeautifulSoup(contenido,'html.parser')
        texto_articulo=soup.get_text()

        url_articulo=wiki.page(titulo_articulo).url
        
        # Guardar contenido en variable
        print(f"Articulo aleatorio {i + 1}: {titulo_articulo}")

        # Guardar contenido en la carpeta
        if i <= 14:
            destino = "./1-15/"+titulo_articulo+".txt"
        else:
            destino = "./16-30/"+titulo_articulo+".txt"

        with open(destino, "w", encoding="utf-8") as file:
            file.write(texto_articulo)

        print("Guardado en "+destino)
        articulos.append(titulo_articulo)
        urls.append(url_articulo)

        print("=" * 50)

    except DisambiguationError as e:
        # Elige la primera opcion en caso de error
        selected_option = e.options[0]
        print(f"Disambiguation error. Selecting option: {selected_option}")
        titulo_articulo = selected_option

print("Array de articulos:")
print(articulos)
print("Array de urls:")
print(urls)

array_string = '\n'.join(articulos)
destino_array = "articulos.txt"

with open(destino_array, "w", encoding="utf-8") as file:
    file.write(array_string)