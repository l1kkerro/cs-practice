def parse_record(line: str) -> dict:
    try: city, temp, date = line.split(';')
    except ValueError: raise ValueError('Полей не ровно три')
    
    if not (city and city.strip()) or not (date and date.strip()): 
        raise ValueError('Город или дата пустые')
    
    try: float(temp)
    except ValueError: raise ValueError('Температура не число')
    return {
        'city': city.strip(),
        'temperature': float(temp),
        'date': date
    }

def read_valid(lines: list[str]) -> list[dict]:
    list = []
    for line in lines:
        try: 
            list.append(parse_record(line))
        except ValueError:
            continue
    return list


from collections import defaultdict

def average_by_city(records: list[dict]) -> dict:
    city_totals = defaultdict (float)
    city_counts = defaultdict (int)

    for entry in records:
        city = entry['city']
        temperature = entry['temperature']

        city_totals[city] += temperature
        city_counts[city] += 1

    averages = {city : round(city_totals[city] / city_counts[city], 1) for city in city_totals}

    return averages
