import sys
if len(sys.argv) < 2:
    print("Usage: python si.py <principle> <time> <rate>")
    sys.exit(1)
principle = int(sys.argv[1])
time = int(sys.argv[2])   
rate = int(sys.argv[2])  
simple_interest = (principle * time * rate) / 100
print("Simple interest:",simple_interest)
