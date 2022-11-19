toolbar = input("Color for toolbar: ")
menu_bar = input("Color for menu bar: ")

with open("customize/color_toolbar.txt", "w") as f:
    f.write(toolbar)

with open("customize/menu_bar_color.txt", "w") as f:
    f.write(menu_bar)