    result = get_jokes()
        for idx, (categories, content) in enumerate(result):
            print("ID :", idx+1)
            print("Categories :", ', '.join(categories))
            print("Content :", content)
            print()
    except Exception as e:
        print(e)