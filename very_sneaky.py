name = input("What's your name? ")
print("Hello, %s" % (name))
fl = input("What was the first letter from the youtube video? ")
month = input("What is the first letter of the month you were born in? ")
tafl = input("What were the next two letters from the video? ")
num = input("What was the number from the video? ")
lltrs = input("What are the first two letters of the color that is the opposite of black? ")
rest_of_the_url = str(fl) + "--" + str(month) + str(tafl) + str(num) + str(lltrs) + ".repl.co"
print("According to your answers, you should go to this URL: https://" + rest_of_the_url)
