import sys
if len(sys.argv) == 4:
  script_name = sys.argv[0] 
  principle = int(sys.argv[1]) 
  time = int(sys.argv[2])   
  rate = int(sys.argv[2])  
  simple_interest = (principle * time * rate) / 100
  print("Simple interest:",simple_interest )

else:
  script_name = sys.argv[0] 
  principle = 2000 
  time = 2   
  rate = 5  
  simple_interest = (principle * time * rate) / 100
  print("Simple interest:",simple_interest )
