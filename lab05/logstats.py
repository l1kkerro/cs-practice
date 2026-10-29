def parse_event(line):
    try:
         time, level, message = line.split()
         return {
              'time': time,
              'level': level,
              'message': message
         }
    except ValueError:
         raise ValueError
def count_levels(lines):

     levels = {
          'BROKEN': 0,
          'DEBUG': 0,
          'ERROR': 0,
          'INFO': 0,
          'WARNING': 0
     }
     for line in lines:
          try:
               level = parse_event(line)['level']
               levels[level] += 1
          except ValueError:
               levels['broken'] += 1

def top_errors(lines, n):
     error_list = [None]
     for line in lines:
          try:
               parsed = parse_event(line)
               if parsed['level'] == 'ERROR':
                    for index, error in error_list:
                         if parsed('message') in error:
                              error_list[index][1] += 1
                              break
                    else:
                         error_list.append([parsed['message'], 1])
          except ValueError:
               continue
     sorted_error_list = sorted(error_list, key=lambda x: (x[1],x[0]), reverse=True)
     return sorted_error_list[:n]

def format_report(counts, errors):
     with open('report.txt', 'w', encoding='utf-8') as file:
          file.write('Отчет по журналу')
          for level in counts.keys():
               file.write(f"{level}: {counts[level]}")
          for error in errors:
               file.write(f"-{error[0]}- {error[1]}")
