import matplotlib.pyplot as plt
import pandas as pd
import ast
import sys

model = []
count = []
f1 = []

with open(sys.argv[1], mode='r') as f:
    for line in f:
        ls = line.split()
        model.append(ls[0])
        count.append(int(ls[1]))
        f1.append(float(ls[2]))

f.close()

print(model)
print(f1)


fig, ax1 = plt.subplots(1, 1, figsize=(10, 8))
ax2 = ax1.twinx()

ax1.bar(model, count, label="sentences", color="lightblue")

ax2.plot(model, f1, label="F1-score", color="black")


handler1, label1 = ax1.get_legend_handles_labels()
handler2, label2 = ax2.get_legend_handles_labels()
ax1.legend(handler1 + handler2, label1 + label2, borderaxespad=0)
ax1.grid(True)

plt.show()
