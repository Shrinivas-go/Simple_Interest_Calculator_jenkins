import sys


if len(sys.argv) == 4:
    script_name = sys.argv[0]
    principle = int(sys.argv[1])
    rate = int(sys.argv[2])
    time = int(sys.argv[3])
else:
    
    script_name = sys.argv[0]
    principle = 30000
    rate = 3
    time = 2

simple_interest = (principle * rate * time) / 100

print(f"Simple Interest = {simple_interest:.2f}")
