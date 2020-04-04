##  哈工程平安行动自动打卡垃圾脚本

如果图片显示有问题可以下载pdf版本

####  更新说明

#####  2020.4.4-0.1版本

此版本极为粗糙，使用限制极多，比如屏幕分辨率限制为1920*1080（其他分辨率可以更改，但比较繁琐），没有打包为exe，需要有python运行环境，浏览器限制为chrome 等等

PS.由于这个最多用一个月，所以，并不知道有没有后续版本更新

#### 使用说明

##### 1、pyautogui

```shell
win: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyautogui
liunx: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pyautogui
```

##### 2、 Selenium和ChromeDriver的安装与配置

* 安装selenium:

```shell
win: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
liunx: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
```

* 安装ChromeDriver,

  该工具供selenium使用Chrome.

下载地址: http://npm.taobao.org/mirrors/chromedriver/

下载前先查看Chrome版本, 然后去上面的link中下载对应的ChromeDriver版本.

| ChromeDriver版本 | 支持的Chrome版本 |
| ---------------- | ---------------- |
|v2.37|v64-66|
|v2.36|v63-65|
|v2.35|v62-64|
|...|...|

Chrome 70.0.3538.16以后ChromeDriver版本号与Chrome版本号相同


* 配置

  进行解压ChromeDriver.
  将解压后的文件放入合适的位置.
  Windows: 将解压后的文件放入配置了环境变量的文件夹, 如System32
  Linux: 将解压后的文件移动到/usr/loacl/bin目录中.

##### 3、参数改动

* py文件相应位置，改为自己的学号，密码

  **请务必保留密码之后的"\n"**

  **请务必保留密码之后的"\n"**

  **请务必保留密码之后的"\n"**

代码示意：

```python
driver.find_element_by_id('username').send_keys('XXXXXXXXXX')#此处改为自己的学号
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('XXXXXXXX\n')#此处改为自己的密码，并保留"\n"
```



* 鉴于本人水平有限，使用的是最暴力原始的方案，即根据像素点坐标点击，故对于其他分辨率屏幕，需要自行更改坐标

分别得到以下四个位置的坐标（图中所示区域内任何一点均可）

**1、**

![image-20200404200623388](https://github.com/AlbertZorichHawking/HEU-COVID-19/tree/master/img/image-20200404200623388.png)

**2、**

![image-20200404200653289](https://github.com/AlbertZorichHawking/HEU-COVID-19/tree/master/img/image-20200404200653289.png)

**3、**

![image-20200404200802208](https://github.com/AlbertZorichHawking/HEU-COVID-19/tree/master/img/image-20200404200802208.png)

**4、**

![image-20200404200834255](https://github.com/AlbertZorichHawking/HEU-COVID-19/tree/master/img/image-20200404200834255.png)

获取方法为：

1、 进入平安行动界面**最底端**!**最底端**!**最底端**!

2、全屏截图，将截图放于PS等画图软件之后，鼠标置于上四图位置获得坐标

3、更改py文件

代码示意：

```python
time.sleep(1.5)
pyautogui.click(725, 822)#第一位置坐标
time.sleep(1.5)
pyautogui.click(113, 163)#第二
time.sleep(1.5)
pyautogui.click(1256, 640)#第三
time.sleep(5)
pyautogui.click(1151, 623)#第四
```

