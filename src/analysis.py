import csv

def read_dialog(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    return rows


def count_all_ponies(rows):
    counts = {}

    for row in rows:
        ponies = row["pony"].split(" and ")

        for pony in ponies:
            if pony in counts:
                counts[pony] += 1
            else:
                counts[pony] = 1
        
    return counts


def calculate_percentage(counts, total):
    percentage = counts / total * 100
    return percentage
    


