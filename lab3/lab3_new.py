import pandas as pd
import matplotlib.pyplot as plt

# given line y=kx+m and point (x, y) return True if the point is over the line
# otherwise return False
def over_line(k, m, x, y):
    return True if k*x + m >= y else False

# read the data into a pandas dataframe
df = pd.read_csv("unlabelled_data.csv", names=["x_axel", "y_axel"], header=None)


# define the line which splits the points equally in terms of
# two points
line_x = [-6, 5]
line_y = [0, 0]

# then using those points calcualte the slope and intercept of a
# linear function
k = (line_y[1] - line_y[0]) / (line_x[1] - line_x[0])
m = line_y[0] - k * line_x[0]

# initialize arrays for the points under and over, also the data for the new file to be written
xo = []
yo = []
xu = []
yu = []
new_data = ""

# loop through each point one by one determining if its over or under
# depending on whether or not its over or under add to respective arrays
# and write corresponding label to the new file
for x, y in zip(df["x_axel"], df["y_axel"]):
    if over_line(k, m, x, y):
        new_data += "0, " + str(x) + ", " + str(y) + "\n"
        xo.append(x)
        yo.append(y)
    else:
        new_data += "1, " + str(x) + ", " + str(y) + "\n"
        xu.append(x)
        yu.append(y)

# save the new file
with open("labelled_data.csv", "w") as f:
    f.write(new_data)

# plot the labelled points
plt.scatter(xo, yo, color = "red")
plt.scatter(xu, yu, color = "green")

# show everything
plt.plot(line_x, line_y)
plt.show()