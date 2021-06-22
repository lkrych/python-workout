def get_rainfall():
    rainfall_dict = {}
    while True:
        city = input("City Name: ").strip()
        if not city:
            break
        try:
            rainfall = int(input("Rainfall (mm): ").strip())
            rainfall_dict[city] = rainfall_dict.get(city, 0) + rainfall
        except:
            print("You did not enter a valid integer")
            continue
    for k,v in rainfall_dict.items():
        print(f'{k}: {v}')

get_rainfall()


