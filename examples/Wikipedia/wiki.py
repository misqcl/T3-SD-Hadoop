import wikipedia as wiki
wiki.set_lang("es") #solo resultados en español para que se puedan encontrar las palabras buscadas, y evitar errores de lenguaje

articulos = []
urls = []
for i in range(15):
    titulo_articulo = wiki.random()
    
    # Recuperar un articulo aleatorio de wikipedia
    a = wiki.page(titulo_articulo).content
    url_articulo=wiki.page(titulo_articulo).url
    
    # Guardar contenido en variable
    print(f"Articulo aleatorio {i + 1}: {titulo_articulo}")

    # Guardar contenido en la carpeta
    destino = titulo_articulo+".txt"
    with open(destino, "w", encoding="utf-8") as file:
        file.write(a)

    print("Guardado en "+destino)
    articulos.append(titulo_articulo)
    urls.append(url_articulo)
    print("=" * 30)

print("Array de articulos:")
print(articulos)
print("Array de urls:")
print(urls)