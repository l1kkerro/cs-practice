def parse_event(line : str):
    try:
         levels = ['BROKEN','DEBUG','ERROR','INFO','WARNING']
         time, level, message = line.split(maxsplit=2)
         if level not in levels:
              raise ValueError
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
               levels['BROKEN'] += 1
     return levels

def top_errors(lines, n):
     error_list = [[1]]
     for line in lines:
          try:
               parsed = parse_event(line)
               if parsed['level'] == 'ERROR':
                    for index, error in enumerate(error_list):
                         if parsed['message'] in error:
                              error_list[index][1] += 1
                              break
                    else:
                         error_list.append([parsed['message'], 1])
          except ValueError:
               continue
     sorted_error_list = sorted(error_list[1:], key=lambda x: (x[1],x[0]), reverse=True)
     return sorted_error_list

def format_report(counts, errors):
     with open('report.txt', 'a', encoding='utf-8') as file:
          file.write(f'Отчет по журналу \n\n')
          for level in counts.keys():
               file.write(f"{level}: {counts[level]} \n")
          for error in errors:
               file.write('\n')
               file.write(f"- {error[0][:-2]} - {error[1]}")
          file.write('\n')
