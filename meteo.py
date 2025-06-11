from datetime import datetime
from meteostat import Stations, Daily
import matplotlib.pyplot as plt

year = 2020
start = datetime(year, 1, 1)
end = datetime(year, 12, 31)

data = Daily('10513', start=start, end=end)
#data = data.normalize()
data = data.aggregate('1d')
data = data.fetch()
data = data.reset_index()
test1 = data.groupby("time")["prcp"].count()


test2 = data[data["time"].dt.year == year][["time","prcp"]].groupby([data["time"].dt.month])["prcp"].sum()
fig, ax = plt.subplots()
ax.bar(test2.index, test2.values)
plt.show()
print(test2)
