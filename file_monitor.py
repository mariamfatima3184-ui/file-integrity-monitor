import hashlib
import json

files_to_monitor = ["test.txt", "test2.txt"]

def calculate_hash(filename):
    with open(filename, "rb") as file:
        data= file.read()
    
    return hashlib.sha256(data).hexdigest()

with open("hashes.json", "r") as file:
    hashes= json.load(file)

for filename in files_to_monitor:
    if filename not in hashes:
        hashes[filename]= calculate_hash(filename)
        with open("hashes.json", "w") as file:
            json.dump(hashes, file, indent=4)
    
    else:
        current_hash=calculate_hash(filename)

        if current_hash== hashes[filename]:
            print(f"[OK] {filename} has not been modified.")
        else:
            print(f"[ALERT] {filename} has been modified!")