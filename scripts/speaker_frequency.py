from src.analysis import read_dialog, count_all_ponies, calculate_percentage


def get_speaker_frequencies():
    rows = read_dialog("data/clean_dialog.csv")
    
    counts = count_all_ponies(rows)
    total = sum(counts.values())

    results = []
    for pony, count in counts.items():
        percentage = calculate_percentage(count, total)
        results.append([pony, count, f"{percentage:.5f}"])

    return results
