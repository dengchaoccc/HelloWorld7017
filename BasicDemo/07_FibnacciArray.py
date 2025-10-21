class Solution():
    #类里的函数，必须使用self作为第一个入参，而且必须要显示的
    def fibbonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            #如果要递归调用，必须要使用self
            return self.fibbonacci(n-1) + self.fibbonacci(n -2)

    def startTest(self):
        i = 3
        print("fib{} = {}",i, self.fibbonacci(i))

