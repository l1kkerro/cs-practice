from logstats import count_levels, top_errors, format_report
path = input('file: ')
lines = []
with open(path, encoding='utf-8') as log:
    for line in log:
        lines.append(line)
print(len(lines))

count = count_levels(lines)

print(count['ERROR'])

print(count['BROKEN'])
errors = top_errors(lines, count['ERROR'])
format_report(count, errors)