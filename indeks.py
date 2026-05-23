
def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    """
    Przetwarza dokumenty i zapytania, zwracając listy indeksów dokumentów,
    w których występuje zapytanie, posortowane według częstości wystąpienia
    danego wyrazu (malejąco), a w przypadku równych częstości - malejąco wg numeru dokumentu.
    """
    results = []

    for query in queries:

        query = query.lower()

        counts = []

        for i, doc in enumerate(documents):

            # usuwanie podstawowej interpunkcji
            cleaned = doc.lower()

            for znak in ".,!?;:":
                cleaned = cleaned.replace(znak, "")

            words = cleaned.split()

            count = words.count(query)

            if count > 0:
                counts.append((i, count))

        counts.sort(key=lambda x: (-x[1], x[0]))

        results.append([doc_id for doc_id, _ in counts])

    return results
    


# Przykładowe wywołanie:
if __name__ == "__main__":
    # Pobranie liczby dokumentów
    n = int(input("Podaj liczbę dokumentów: "))
    documents = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(n):
        documents.append(input())

    # Pobranie liczby zapytań
    m = int(input("Podaj liczbę zapytań: "))
    queries = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(m):
        queries.append(input().strip())

    # Przetworzenie zapytań
    results = index_documents(documents, queries)

    # Wypisanie wyników
    print("Wyniki:")
    for res in results:
        print(res)