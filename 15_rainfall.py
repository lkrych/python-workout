def get_rainfall():
    rainfall_dict = {}
    while True:
        city = input("City Name: ").strip()
        if not city:
            break
        rainfall = int(input("Rainfall (mm): ").strip())
        if city in rainfall_dict:
            rainfall_dict[city] = rainfall_dict[city] + rainfall
        else:
            rainfall_dict[city] = rainfall

    for k,v in rainfall_dict.items():
        print(f'{k}: {v}')

get_rainfall()


