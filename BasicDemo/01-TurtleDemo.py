
'''
turtle功能有限，更多的是作为一个教学工具来做演示
'''
import  turtle as tt

'''
用不同的颜色画一个长方形
'''
def draw_rectangle():

    #设置笔刷宽度
    tt.width(4)
    tt.forward(200)

    tt.right(90)#右转90度
    tt.pencolor("red")
    tt.forward(100)

    tt.right(90)
    tt.pencolor("green")
    tt.forward(200)

    tt.right(90)  # 右转90度
    tt.pencolor("blue")
    tt.forward(100)
    tt.done()#调用done窗口，程序不会立即关闭

def draw_cycle():
    screen = tt.Screen()
    screen.setup(600, 600)  # 设置窗口大小
    screen.bgcolor("white")  # 设置背景颜色
    screen.title("用海龟工具做教学演示")  # 设置窗口标题

    t = tt.Turtle()
    t.shape("turtle")  # 设置光标形状为海龟
    t.color("darkgreen")  # 设置画笔颜色
    t.pensize(3)  # 设置画笔粗细
    t.speed(8)  # 设置绘图速度 (1-10，0最快)

    t.penup()
    t.goto(100, 100)  # 移动到新位置
    t.pendown()
    t.color("red", "yellow")  # 设置画笔颜色和填充色
    t.begin_fill()
    t.circle(80)  # 画一个半径为80的圆
    t.end_fill()

    '''打印一些文字'''
    t.penup()
    t.goto(-150, 150)
    t.color("blue")
    t.write("你好，Turtle!", font=("SimHei", 16, "bold"))  # 使用黑体字体

    # 点击窗口关闭
    screen.exitonclick()  # 点击画布窗口后退出

#draw_rectangle()
draw_cycle()