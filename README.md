# HNU_ClockIn
使用Python+Selenium进行HNU疫情防控自动打卡




## 前情

公元2020年上半年

COVID-19荼毒中华大地

众多湖大学子转校加里敦

为了使“早起”的各位同学

不需要因为忘记打卡而烦恼

我特此编写如下自动打卡脚本

一次运行，无人值守。

*仅供交流学习，由此出现的任何问题，与本人无关

*代码有不完善之处，请大佬尽管喷

## 技术栈
Nginx反向代理；

Python+Selenium

## 实现原理

普通打卡流程：

打开打卡网页->选择地理位置->填写表单->触摸“打卡”按钮，提交表单->服务器端数据验证->验证通过，打卡成功

其中，打卡网页地址:(居然没有用https实在方便抓包hhh)

http://fangkong.hnbu.edu.cn/app

网页架构：Vue

提交表单的API：

http://fangkong.hnu.edu.cn/api/v1/clockinlog/add

本来是想直接请求API完成打卡的。但是不知为何总是出错：（

于是使用Selenium实现自动登陆以及自动填写表单。

但是难点在于，选择地理位置 这一项，其值不能直接填写，而是需要与微信的API配合

这就很头秃。。。

经过分析。我发现地理位置的数据绑定有三个，位于app_c99fa374.js

	RealProvince:e,
	
	RealCity:t,
	
	RealCounty:n,
	

那么我们将这个网址反向代理，自己复制一个app.js，将app_c99fa374.js替换成自己的这个app.js,然后把这三项改成我们自己的信息就可以了。


## 步骤:

1.本地安装宝塔面板windows，安装nginx，在默认主机下设置nginx反向代理，并设置内容替换：
代理名称:随便填
目标URL：http://fangkong.hnu.edu.cn 发送域名：fangkong.hnu.edu.cn
内容替换：<script src=static/js/app.c99fa379.js>   替换为 <script src="http://127.0.0.1:81/js/app.js">

2.新建网站，端口为81.
把app.c99fa379.js Copy到新建网站目录/js/app.js，用文本编辑器打开，修改上述三项信息，比如

	RealProvince:"湖南省",
	
	RealCity:"长沙市",
	
	RealCounty:"岳麓区",
	

3.安装python运行环境，下载Chrome浏览器或国产双核浏览器以及相应版本的Chromedriver。
Chromedriver下载地址：http://npm.taobao.org/mirrors/chromedriver/
注意：要查看你的浏览器Chrome内核版本号。方法：点击浏览器的帮助->关于，大概率会出现，比如是78,就下载chromedriver 78开头的driver

4.按照源代码提示进行修改并运行即可。




## 支持
如有任何问题，欢迎发issue提问，有时间的话，我会手把手教[doge]










