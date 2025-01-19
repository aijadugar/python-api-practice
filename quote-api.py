import requests

def get_quote():
    url = 'https://api.freeapi.app/api/v1/public/quotes'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['success'] and 'data' in data:
            quotes = data['data']['data']
            
            # print(quotes)
            res = []
            for quote in quotes:
                author = quote.get('author', '')
                content = quote.get('content', '')
                res.append((author, content))
            return res
        else:
            raise Exception("Failed to get response from url.")

def main():
    try:
        res = get_quote()
        for idx, (author, content) in enumerate(res):
            print("ID :", idx+1)
            print("Author :", author)
            print("Content :", content)
            print()
            
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()