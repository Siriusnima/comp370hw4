import csv
from scripts.speaker_frequency import get_speaker_frequencies

results = get_speaker_frequencies()

with open("speaker_freqnency.csv", "w", newline = "") as file:
    writer = csv.writer(file)

    writer.writerow([
        "pony_name",
        "total_line_count",
        "percent_all_lines"
    ])

    writer.writerows(results)