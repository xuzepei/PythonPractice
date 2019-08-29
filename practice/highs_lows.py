import csv

from matplotlib import pyplot as plt
from datetime import datetime
from matplotlib.ticker import FormatStrFormatter
import matplotlib.dates as mdate

filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:

        highs.append(int(row[1]))
        lows.append(int(row[3]))

        date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(date)



#Plot data.
fig = plt.figure(dpi=128, figsize=(8, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format dates
fig.axes[0].xaxis.set_major_formatter(mdate.DateFormatter('%b %d %Y'))
fig.autofmt_xdate()

# Format plot.
plt.title("Daily high temperatures, July 2014", fontsize=20)
plt.xlabel('', fontsize=10)
plt.ylabel("Temperature (F)", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()