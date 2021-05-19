import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'limegreen', 
          'red', 'navy', 'blue', 'magenta', 'crimson']
explode = (0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, .01)
labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

fig, ax = plt.subplots()

def update(num):
    ax.clear()
    ax.axis('equal')
    str_num = str(num)
    for x in range(10):
        nums[x] += str_num.count(str(x))
    ax.pie(nums, explode=explode, labels=labels, colors=colors, 
            autopct='%1.1f%%', shadow=True, startangle=140)
    ax.set_title(str_num)

ani = FuncAnimation(fig, update, frames=range(100), repeat=False)
plt.show()
