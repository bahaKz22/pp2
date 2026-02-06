colors = ("red", "green", "blue")
colors = colors[:1] + ("yellow", "orange") + colors[3:]
print(colors)  # ('red', 'yellow', 'orange')
