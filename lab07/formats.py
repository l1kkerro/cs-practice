def csv_to_records(text):
    result = []
    if ',' in text:
        lines = text.rstrip('\n').split('\n')
        title = lines[0].split(',')
        for line in lines[1:]:
            value = line.split(',')
            result.append({title[0].strip():value[0].strip(),title[1].strip():value[1].strip()})
        return result
    else:
        return result
    
def parse_value(value):
    value_low = value.lower()
    if value_low in ['true','yes']:
        return True
    if value_low in ['false','no']:
        return False
    if all(s in ['0','1','2','3','4','5','6','7','8','9',',','.'] for s in value):
        if any(s in [',','.'] for s in value):
            value = value.replace(',','.')
            return float(value)
        return int(value)
    return(value)
    
def parse_settings(lines):
    result = {}
    current_list_key = None

    for raw_line in lines:
        line = raw_line.split('#', 1)[0].strip()
        if not line:
            continue

        if line.startswith('- '):
            if current_list_key is not None:
                result[current_list_key].append(parse_value(line[2:].strip()))
            continue

        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            if value == '':
                current_list_key = key
                result[key] = []
            else:
                current_list_key = None
                result[key] = parse_value(value)
    return result

def merge_by_key(rows, extra, key):
    result = []
    for row in rows:
        value = row.get(key)
        if value in extra:
            merged_row = {**extra[value], **row}
        else:
            merged_row = row.copy()
        result.append(merged_row)
    return result

print(csv_to_records("город, цена \n Азов , 100 \n"))