import pandas as pd
import matplotlib.pyplot as plt

def over_line(k, m, x, y):
    return True if k*x + m >= y else False

df = pd.read_csv("unlabelled_data.csv")
df.columns = df.columns.str.replace("-1.885907518189583", "x_axel").str.replace("-1.997407599218205", "y_axel")

line_x = [-6, 5]
line_y = [0, 0]
k = (line_y[1] - line_y[0]) / (line_x[1] - line_x[0])
m = line_y[0] - k * line_x[0]

xo = []
yo = []
xu = []
yu = []
new_data = ""

for x, y in zip(df["x_axel"], df["y_axel"]):
    if over_line(k, m, x, y):
        new_data += "0, " + str(x) + ", " + str(y) + "\n"
        xo.append(x)
        yo.append(y)
    else:
        new_data += "1, " + str(x) + ", " + str(y) + "\n"
        xu.append(x)
        yu.append(y)

with open("labelled_data.csv", "w") as f:
    f.write(new_data)

plt.scatter(xo, yo, color = "red")
plt.scatter(xu, yu, color = "green")

plt.plot(line_x, line_y)
plt.show()