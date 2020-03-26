# HNU_ClockIn
使用Python+Selenium进行自动打卡




## 前情
公元2020年上半年
COVID-19荼毒中华大地
众多湖大学子转校加里敦
为了使“早起”的各位同学
不需要因为忘记打卡而烦恼
我特此编写如下自动打卡脚本
一次运行，无人值守。
*仅供交流学习，由此出现的任何问题，与本人无关

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

1.本地安装宝塔面板windows，设置nginx反向代理，并设置内容替换：

sub_filter '<script src=static/js/app.c99fa379.js>' '<script src="127.0.0.1/js/app.js">';
    
2.把app.c99fa379.js Copy到本地网站默认目录/js/app.js，用文本编辑器打开，修改上述三项信息，比如

	RealProvince:"湖南省",
	
	RealCity:"长沙市",
	
	RealCounty:"岳麓区",
	

3.安装python运行环境，下载Chrome浏览器或国产双核浏览器以及相应版本的Chromedriver

4.按照源代码提示进行修改运行即可。















