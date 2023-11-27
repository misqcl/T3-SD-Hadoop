import json

with open("urls.txt", "r", encoding="utf-8") as url_file:
    urls = [url.strip() for url in url_file.readlines()]

with open("./output/part-00000", "r", encoding="utf-8") as read_file:
    read_file.readline()
    files = {}

    for i, line in enumerate(read_file):
        elementos = line.split('\t')
        if len(elementos) != 2:
            print(f"Saltando línea inválida {i + 1}: {line}") #Algunas líneas ejecutan incorrectamente, y es más conveniente saltarlas
            continue

        word, document = elementos
        # Separación de caracteres para elegir la palabra, documento y cuenta
        word = line.split('(')[0].strip(" '")
        document = line.split('(')[-1].split(',')[0].strip()
        count = line.split(',')[-1].split(')')[0].strip()

        if int(document)-1 < len(urls):
            url = urls[int(document)-1]
        else:
            url = "No hay Link disponible"

        if word in files.keys():
            files[word][document] = {"count":count,"url": url}
            print("Insertada la palabra "+word+" del documento "+document)
        else:
            print("Insertada la palabra "+word+" del documento "+document)
            files[word] = {document: {"count":count,"url": url}}

with open("datos.json", "w", encoding="utf-8") as outfile:
    json.dump(files, outfile, indent=4)
