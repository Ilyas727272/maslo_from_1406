
import datetime
import time
def main():
	while(1):
		current_time = datetime.datetime.now().time()
		print(current_time)
		time.sleep(5)

if __name__ == "__main__":
	main()