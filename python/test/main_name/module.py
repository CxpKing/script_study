'''
运行当前文件，打印结果为
We are in __main__
'''
def main():
	print('We are in ',__name__)

if __name__ == "__main__":
	main()
	print(__name__)