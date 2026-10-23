def parse_record(line: str) -> dict:
    try: city, temp, date = line.split(';')
    except ValueError: raise ValueError('Полей не ровно три')
    
    if not (city and city.strip()) or not (date and date.strip()): 
        raise ValueError('Город или дата пустые')
    
    try: float(temp)
    except ValueError: raise ValueError('Температура не число')
    return {
        'город': city.strip(),
        'температура': float(temp),
        'дата': date
    }

def read_valid(lines: list[str]) -> list[dict]:
    list = []
    for line in lines:
        try: 
            list.append(parse_record(line))
        except ValueError:
            continue
    return list
