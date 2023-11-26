import wikipedia as wiki
from bs4 import BeautifulSoup
from wikipedia.exceptions import DisambiguationError
wiki.set_lang("es") #solo resultados en español para que se puedan encontrar las palabras buscadas, y evitar errores de lenguaje

articulos = []
urls = []

def articulo_wiki():
    while True:
        titulo_articulo = wiki.random()
        if '/' and '(' and ')' not in titulo_articulo: #Se evitan los caracteres "dañinos"
            return titulo_articulo
        
for i in range(1):
    titulo_articulo = articulo_wiki()
    try:
        # Recuperar un articulo aleatorio de wikipedia
        contenido=wiki.page(titulo_articulo).content
        soup=BeautifulSoup(contenido,'html.parser')
        texto_articulo=soup.get_text()

        url_articulo=wiki.page(titulo_articulo).url
        
        # Guardar contenido en variable
        print(f"Articulo aleatorio {i + 1}: {titulo_articulo}")
        articulos.append(titulo_articulo)
        urls.append(url_articulo)

        # Guardar contenido en la carpeta
        titulo_articulo = titulo_articulo.replace(" ", "_") #se reemplazan los espacios para poder mover los datos con hdfs
        if i <= 16:
            destino = "./1/"+str(i+1)+".txt"
        else:
            destino = "./2/"+str(i+1)+".txt"

        with open(destino, "w", encoding="utf-8") as file:
            file.write(titulo_articulo+"\n")
            file.write(texto_articulo)

        print("Guardado en "+destino)
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

articulos_string = '\n'.join(articulos)
destino_articulos = "articulos.txt"
urls_string = '\n'.join(urls)
destino_urls = "urls.txt"

with open(destino_articulos, "w", encoding="utf-8") as file:
    file.write(articulos_string)
with open(destino_urls, "w", encoding="utf-8") as file:
    file.write(urls_string)