# 模拟网络登录

通过浏览器打开登录界面，模拟键盘输入用户名和密码，模拟鼠标点击，实现账户登录。

以Windows为例，使用方法如下：

1. 安装python3及相关模块

2. 安装[Firefox浏览器](http://www.firefox.com/)

3. 将```geckodriver.exe```文件复制到python安装目录，并将该目录添加到`Path`环境变量中
   
4. 将`username.send_keys('replace with username')`中的字符串`replace with username`替换为用户名，`password.send_keys('replace with password')`中的字符串`replace with password`替换为登录密码
   
5. 将`sleep_time = 5`中的数字更改为合适的时间（单位为分钟），每隔该时间检测网络是否畅通，如果网络不通，则执行登录操作
   
6. 执行`auto-login-NCU-NetWork.pyw`