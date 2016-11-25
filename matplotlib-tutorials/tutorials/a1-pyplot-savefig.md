# Lưu trữ đồ thị khi vẽ bằng Matplotlib

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 24 tháng 11 năm 2016

## Tài liệu tham khảo

1. [Matplotlib - Pyplot - matplotlib.pyplot](http://matplotlib.org/api/pyplot_api.html).

2. [matplotlib savefig in jpeg format](http://stackoverflow.com/questions/8827016/matplotlib-savefig-in-jpeg-format).

3. [Matplotlib - colors - matplotlib.colors](http://matplotlib.org/api/colors_api.html).


## Phiên bản Matplotlib được sử dụng

Matplotlib 1.5.3

## Lưu lại đồ thị trong Matplotlib với lệnh savefig

* Các tham số của lệnh savefig:
		
		savefig(fname, dpi=None, facecolor='w', edgecolor='w',
				orientation='portrait', papertype=None, format=None,
				transparent=False, bbox_inches=None, pad_inches=0.1,
				frameon=None)

	Trong đó:
	
	+ `fname=/path/filename`:
	
		Gồm chuỗi chứa *đường dẫn lưu trữ - path* và *tên figure - filename* của đồ thị. 
	Nếu bỏ qua *đường dẫn lưu trữ - path* thì figure được lưu trữ ngay thư mục hiện tại. 
	Ví dụ: `/home/username/matplotlib/figure.png` hoặc `figure.png` đều được.
	
		- Nếu chỉ đưa vào tham số `fname`, bỏ qua các tham số còn lại thì định dạng của figure 
	sẽ được xác định theo định dạng của *tên figure - filename*.
		
		- Các định dạng của *tên figure - filename* được hỗ trợ:
			
				eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff
	
	+ `dpi=None|scalar > 0|'figure'`:
	
		Xác định độ phân giải của figure - số chấm trên mỗi inch.
	
		- Nếu `dpi=None`: lấy giá trị mặc định của `savefig.dpi` trong file `matplotlibrc`.
		
		- Nếu `dpi='figure'`: thì giá trị của `dpi` được đặt theo giá trị của figure.
		
	+ `facecolor='color'`:
	
		Với `color` là giá trị màu mà `matplotlib.colors` hỗ trợ. 
		Xác định màu nền của hình chữ nhật bao xung quanh figure. 
		Ví dụ: `facecolor='b'` hoặc `facecolor='blue'` hoặc `facecolor='#eeefff'` hoặc `facecolor='0.75'` đều được.
	
	+ `edgecolor='color'`:
	
		Chưa nhìn thấy sự khác biệt khi thay đổi tham số này.
	
	+ `orientation='landscape'|'portrait'`:
	
		Xác định chiều khổ giấy, định dạng này chỉ có tác dụng với figure có định dạng `postscript - *.ps`.
	
	+ `papertype=None|'letter'|'legal'|'executive'|'ledger'|'a0'-->'a10'|'b0'-->'b10'`:
	
		Xác định loại giấy, định dạng này chỉ có tác dụng với figure có định dạng `postscript - *.ps`.
	
	+ `format=None|'png'|'pdf'|'ps'|'eps'|'svg'`:
	
		Hỗ trợ định dạng chính với đặc điểm của định dạng phụ được khai báo thêm.
	
	+ `transparent=True|False`:
	
		Chưa hiểu cách sử dụng tham số này.
	
	+ `frameon=None|True|False`:
	
		Chưa hiểu cách sử dụng tham số này.
	
	+ `bbox_inches=None|'tight'`:
	
		- Nếu `bbox_inches=None`: thì hình chữ nhật phía bên ngoài figure được để mặt định, không được cắt bỏ khoảng trắng thừa.
		
		- Nếu `bbox_inches='tight'`: thì hình chữ nhật phía bên ngoài figure được cắt bỏ đi những khoảng trắng thừa.
	
	+ `pad_inches=value inch`:
	
		Định dạng `pad_inches` đi cùng với định dạng `bbox_inches='tight'` quy định khoảng trắng thừa được cắt bỏ 
	với khoảng cách là `value inch` (tính từ mép ngoài đi vào trong đến figure).
	
	+ `bbox_extra_artists`
	
		Chưa hiểu cách sử dụng tham số này.
