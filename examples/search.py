import json
import argparse

def search_word_top5(json_data, search_word):
    results = []

    if search_word in json_data:
        documents = json_data[search_word]

        sorted_documents = sorted(documents.items(), key=lambda x: int(x[1].get("count", 0)), reverse=True)

        top5_documents = sorted_documents[:5]

        for document, info in top5_documents:
            count = info.get("count", "")
            url = info.get("url", "")

            result = {
                "Palabra": search_word,
                "Documento": {document: {"Frecuencia": count, "url": url}}
            }
            results.append(result)

    return results

def main():
    parser = argparse.ArgumentParser(description='Search for a word and get the top 5 documents based on counts.')
    parser.add_argument('search_word', type=str, help='The word to search for')
    args = parser.parse_args()

    with open('datos.json', 'r') as json_file:
        data = json.load(json_file)

    search_results = search_word_top5(data, args.search_word)

    for result in search_results:
        print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
