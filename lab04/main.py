from stats import average_by_city, read_valid, warmest_city
import sys 

lines = sys.stdin.read().splitlines()
records = read_valid(lines)

average = average_by_city(records)
warmest = warmest_city(records)
lines_done = len(records)
lines_skipped = len(lines) - lines_done
max_avg_temp = average[warmest]

print(lines_done)
print(lines_skipped)
print(max_avg_temp)