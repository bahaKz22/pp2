import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Мой Paint")
        self.root.geometry("800x600")

        # начальные значения
        self.tool = "pencil" 
        self.color = "black"
        self.start_x = 0
        self.start_y = 0
        self.shape_id = None # чтобы фигура не двоилась при растягивании мышкой

        self.make_interface()
        self.bind_mouse()

    def make_interface(self):
        # панелька для кнопок сверху
        panel = tk.Frame(self.root, bg="lightgray")
        panel.pack(side=tk.TOP, fill=tk.X)

        # обычные инструменты
        tk.Button(panel, text="Карандаш", command=lambda: self.set_tool("pencil")).pack(side=tk.LEFT)
        tk.Button(panel, text="Ластик", command=lambda: self.set_tool("eraser")).pack(side=tk.LEFT)
        tk.Button(panel, text="Цвет", command=self.get_color).pack(side=tk.LEFT)

        # кнопки для фигур
        tk.Button(panel, text="Прямоугольник", command=lambda: self.set_tool("rect")).pack(side=tk.LEFT)
        tk.Button(panel, text="Квадрат", command=lambda: self.set_tool("square")).pack(side=tk.LEFT)
        tk.Button(panel, text="Прямоуг. треуг", command=lambda: self.set_tool("r_tri")).pack(side=tk.LEFT)
        tk.Button(panel, text="Равностор. треуг", command=lambda: self.set_tool("eq_tri")).pack(side=tk.LEFT)
        tk.Button(panel, text="Ромб", command=lambda: self.set_tool("rhomb")).pack(side=tk.LEFT)

        # холст где будем рисовать
        self.c = tk.Canvas(self.root, bg="white")
        self.c.pack(fill=tk.BOTH, expand=True)

    def bind_mouse(self):
        # привязываем мышку
        self.c.bind("<Button-1>", self.click)
        self.c.bind("<B1-Motion>", self.drag)
        self.c.bind("<ButtonRelease-1>", self.release)

    def set_tool(self, t):
        self.tool = t

    def get_color(self):
        # вызываем окно выбора цвета
        color = colorchooser.askcolor(color=self.color)[1]
        if color != None:
            self.color = color

    def click(self, event):
        # запоминаем откуда начали рисовать
        self.start_x = event.x
        self.start_y = event.y

    def drag(self, event):
        if self.tool == "pencil":
            # рисуем линию карандашом
            self.c.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color, width=2)
            self.start_x = event.x
            self.start_y = event.y
            
        elif self.tool == "eraser":
            # ластик это просто толстая белая линия
            self.c.create_line(self.start_x, self.start_y, event.x, event.y, fill="white", width=15)
            self.start_x = event.x
            self.start_y = event.y
            
        else:
            # удаляем старый контур фигуры пока тянем мышку
            if self.shape_id != None:
                self.c.delete(self.shape_id)
            self.shape_id = self.draw(self.start_x, self.start_y, event.x, event.y)

    def release(self, event):
        # когда отпускаем мышь, фигура окончательно остается на холсте
        if self.tool not in ["pencil", "eraser"]:
            if self.shape_id != None:
                self.c.delete(self.shape_id)
                self.shape_id = None
            self.draw(self.start_x, self.start_y, event.x, event.y)

    def draw(self, x1, y1, x2, y2):
        # функция которая рисует саму фигуру
        if self.tool == "rect":
            return self.c.create_rectangle(x1, y1, x2, y2, outline=self.color)
        
        elif self.tool == "square":
            # считаем сторону для квадрата чтобы он был ровный
            side = max(abs(x2 - x1), abs(y2 - y1))
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            return self.c.create_rectangle(x1, y1, x1 + side*dx, y1 + side*dy, outline=self.color)
            
        elif self.tool == "r_tri":
            # прямоугольный треугольник
            return self.c.create_polygon(x1, y1, x1, y2, x2, y2, outline=self.color, fill="")
            
        elif self.tool == "eq_tri":
            # равнобедренный треугольник
            mx = (x1 + x2) / 2
            return self.c.create_polygon(mx, y1, x1, y2, x2, y2, outline=self.color, fill="")
            
        elif self.tool == "rhomb":
            # ромб
            mx = (x1 + x2) / 2
            my = (y1 + y2) / 2
            return self.c.create_polygon(mx, y1, x2, my, mx, y2, x1, my, outline=self.color, fill="")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()