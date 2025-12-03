'''
# http://naver.com

# url = "http://naver.com"
# url = "http://daum.net"
url = "http://google.com"


my_str = url.replace("http://", "")

my_str = my_str[:my_str.index(".")]

print(f'{url}의 패스워드는 {my_str[0:3]}{len(my_str)}{my_str.count("e")}{"!"}')
'''

subway = [10, 20, 30]

print(subway)