
import  turtle as tt

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

draw_rectangle()