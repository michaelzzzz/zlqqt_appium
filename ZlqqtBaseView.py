class ZlqqtBaseView(object):
    '''
    基类封装
    '''
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def get_size(self):
        '''
        获取屏幕分辨率
        :param driver:
        :return: x:横屏;y:竖屏
        '''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipt_left(self):
        '''
        对屏幕进行左滑操作
        :return:
        '''
        l = self.get_size()
        x1 = int(l[0] * 0.90)
        x2 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.50)
        return self.driver.swipe(x1, y1, x2, y1, 1000)

    def touch_tap(self,x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
        '''
        method explain:点击坐标
        parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
            device.touch_tap(277,431)      #277.431为点击某个元素的x与y值
        '''
        # 获取当前屏幕的宽
        screen_width = self.driver.get_window_size()['width']
        # 获取当前屏幕的高
        screen_height = self.driver.get_window_size()['height']
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        return self.driver.tap([(x1, y1), (x1, y1)], duration)