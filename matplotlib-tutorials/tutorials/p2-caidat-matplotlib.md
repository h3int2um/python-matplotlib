# Cài đặt Matplotlib trên Ubuntu 16.04

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 23 tháng 11 năm 2016

## Tài liệu tham khảo

1. [How to Install Pip on Ubuntu 14.04 LTS](https://www.liquidweb.com/kb/how-to-install-pip-on-ubuntu-14-04-lts/).

2. [Introduction to Matplotlib and basic line](https://pythonprogramming.net/matplotlib-intro-tutorial/).

3. [Matplotlib - Troubleshooting](http://matplotlib.org/faq/troubleshooting_faq.html).

## Cách cài đặt

* Cài đặt Matplotlib trên Ubuntu 16.04:	

	+ Mở cửa sổ Terminal (nhấn `Ctrl + Alt + T`), gõ lệnh sau để cài đặt `python-pip` 
	(nếu đã cài đặt rồi thì bỏ qua bước này):
	
			$ sudo apt-get install python-pip
			
		![](https://raw.githubusercontent.com/h3int2um/python-matplotlib/master/matplotlib-tutorials/images/setup-matplotlib/caidat-matplotlib-ubuntu.png)

	+ Tiếp tục gõ lệnh sau trong cửa sổ Terminal để cài đặt `Matplotlib`:
	
			$ sudo pip install matplotlib
			
		![](https://raw.githubusercontent.com/h3int2um/python-matplotlib/master/matplotlib-tutorials/images/setup-matplotlib/caidat-python-pip-ubuntu.png)
		
	+ Kiểm tra cài đặt: gõ các lệnh sau, nếu không báo lỗi nghĩa là cài đặt thành công. 
	Trong trường hợp này phiên bản cài đặt là `1.5.3`.
	
			$ python
			
			>>> import matplotlib
			
			>>> matplotlib.__version__
			
			'1.5.3'
		
		![](https://raw.githubusercontent.com/h3int2um/python-matplotlib/master/matplotlib-tutorials/images/setup-matplotlib/kiemtra-caidat-matplotlib.png)
