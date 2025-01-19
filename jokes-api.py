import requests

def get_jokes():
    url = 'https://api.freeapi.app/api/v1/public/randomjokes'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        if data['success'] and 'data' in data:
            jokes = data['data']['data']
            
            # print(jokes)
            result = []
            for joke in jokes:
                categories = joke['categories']
                content = joke['content']
                result.append((categories, content))
                
                cate = joke.get('categories')
                con = joke.get('content')
                result.append((cate, con))
            
                
            return result
        else:
            raise Exception("Failed to get responce from url.")
                
def main():
    try:
        result = get_jokes()
        for idx, (categories, content) in enumerate(result):
            print("ID :", idx+1)
            print("Categories :", ', '.join(categories))
            print("Content :", content)
            print()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()