run : 
	make clean
	python3 main.py
	convert result.ppm result.jpg

clean : 
	rm -f result.ppm

show : 
	display result.jpg
