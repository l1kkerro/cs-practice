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
          'broken': 0,
          'debug': 0,
          'error': 0,
          'info': 0,
          'warning': 0
     }
     for line in lines:
          try:
               level = parse_event(line)['level']
               levels[level] += 1
          except ValueError:
               levels['broken'] += 1