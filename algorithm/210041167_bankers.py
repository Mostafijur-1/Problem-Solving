import csv
from itertools import permutations

def read_input_from_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Read header row
            
            # print("Detected Headers:", headers)  # Debugging step
            
            # Identify resource types dynamically
            resource_types = sorted(set(h.split('_')[-1] for h in headers if '_' in h))
            num_resources = len(resource_types)
            
            # Expected headers based on detected resource types
            expected_headers = ["PID"] + \
                               [f"Allocation_{r}" for r in resource_types] + \
                               [f"Max_{r}" for r in resource_types] + \
                               [f"Available_{r}" for r in resource_types]

            # # Debug: Print expected headers
            # print("Expected Headers:", expected_headers)  
            
            # Validation step: Check if all expected headers exist
            if not all(h in headers for h in expected_headers):
                print("Invalid File Format")
                exit()
            
            print("Valid File Format")

            processes = []
            allocation = []
            max_need = []
            available = []

            rows = list(reader)

            for row in rows[:-1]:  
                processes.append(row[0]) 
                allocation.append(list(map(int, row[1:num_resources+1])))
                max_need.append(list(map(int, row[num_resources+1:2*num_resources+1])))

           
            available = list(map(int, rows[-1][2*num_resources+1:]))

           

            return processes, allocation, max_need, available, num_resources
    except Exception as e:
        print("Error reading file:", e)
        exit()
        
# Helper Function

def is_safe_sequence(sequence, available, max_need, allocation, num_resources):
    avail = available[:]  
    finish = [False] * len(sequence)
    
    
    for i in sequence:
        need = [max_need[i][j] - allocation[i][j] for j in range(num_resources)]
       
        
        if all(need[j] <= avail[j] for j in range(num_resources)):
         
            avail = [avail[j] + allocation[i][j] for j in range(num_resources)]
            finish[i] = True
        else:
           
            return False
    
    return True

def find_safe_sequences(processes, available, max_need, allocation, num_resources):
    safe_sequences = []
    process_indices = list(range(len(processes)))
    
    for perm in permutations(process_indices):
        if is_safe_sequence(perm, available, max_need, allocation, num_resources):
            safe_sequences.append([processes[i] for i in perm])
    
    return safe_sequences

# Main Execution
file_path = "C:/Users/mostafij/Desktop/Problem Solving/algorithm/input1.csv"

processes, allocation, max_need, available, num_resources = read_input_from_csv(file_path)
safe_sequences = find_safe_sequences(processes, available, max_need, allocation, num_resources)

# Output Results
if safe_sequences:
    print(f"Total number of safe sequences: {len(safe_sequences)}")
    print(f"One safe sequence: {safe_sequences[0]}")
else:
    print("System is in an unsafe state. No safe sequences found.")
