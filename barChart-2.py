import matplotlib as mb
import matplotlib.pyplot as plt

mb.rcParams['font.size']=25

# x = dataset["Region"]
# y = dataset["Jan"]
# Another way:
x = dataset.loc[0:3,'Region'].tolist()
y = dataset.loc[0:3,'Jan'].tolist()

plt.bar(x,y, width=0.5, color='skyblue')

# To set the data label I need to use for loop
# Giving label by zip and including $ and K sign
# Bringing the label in the middle by (ha = horizontal alignment)
# Keeping a little space between labels and Bars (xytext = (o,10))- first one for left/right, second one for up/down
for x,y in zip(x,y):
    label = '${:,.2f}K'.format(y/1000)
    plt.annotate(label,(x,y), ha='center',textcoords='offset points',xytext=(0,10))

plt.show()