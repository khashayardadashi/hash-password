import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    hash_pass = {}
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            hash_pass [row[0]] = row[1]

    hash_map = {}
    for i in range (1000, 10000):
        hsh = hashlib.sha256 (str(i).encode('UTF-8')).hexdigest()
        hash_map [hsh] = str(i)

    for pw in hash_pass:
        current_hash = hash_pass[pw]
        reverse_hash = hash_map [current_hash]
        hash_pass[pw] = reverse_hash

    with open (output_file_name, 'w') as out:
        count = 0
        for person in hash_pass:
            count += 1
            if count != 1:
                out.write("\n"+ person + "," + hash_pass [person])
            else:
                out.write(person + "," + hash_pass [person])
