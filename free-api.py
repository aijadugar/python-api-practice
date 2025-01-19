import requests

def fetch_data():
    url = "https://api.freeapi.app/api/v1/public/books"
    responce = requests.get(url)
    
    if responce.status_code == 200:
        data = responce.json()
    
        if "data" in data["data"] and "data" in data:
            books = data["data"]["data"]
            
            results = []
            for book in books:
                etag = book['etag']
                volume_info = book.get('volumeInfo', {})
                authors = volume_info.get("authors", [])
                categories = volume_info.get("categories", [])
                results.append((etag, authors, categories))
            return results
        else:
            raise Exception("Fail to get url data.")
    

def main():
    try:
        results = fetch_data()
        for idx, (etag, authors, categories) in enumerate(results):
            print(f"Book {idx}")
            print(f"etag: {etag}")
            print(f"Authors: {', '.join(authors)}")
            print(f"Categories: {', '.join(categories)}")
            print()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()