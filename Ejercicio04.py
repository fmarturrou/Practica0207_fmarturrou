import urllib.request

url = "http://textfiles.com/adventure/aencounter.txt"

try:
    with urllib.request.urlopen(url) as response:
        text = response.read().decode('utf-8')

    words = text.split()
    num_words = len(words)

    print(f"El número de palabras en el fichero es: {num_words}")

except Exception as e:
    print(f"No se pudo acceder al fichero. Error: {e}")
