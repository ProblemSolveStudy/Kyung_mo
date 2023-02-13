# subway = [10, 20, 30]

# print(subway.index(20))

# subway.append(40)
# print(subway)

# subway.insert(1, 50)
# print(subway)

# subway.sort()
# print(subway)

# subway.clear()
# print(subway)

# mix_list = ["hi", 20, True]

# subway.extend(mix_list)
# print(subway)

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[100])

# # print(cabinet.get(3))
# print(cabinet.get(5, "사용가능"))
# print(cabinet[3])

# cabinet = {"A-3" : "유재석" , "B-100" : "김태호"}

# print(cabinet["A-3"])
# print(cabinet["B-100"])

# print(cabinet)
# cabinet["C-20"] = "조세호"

# print(cabinet)

# del cabinet["A-3"]
# print(cabinet.keys())
# print(cabinet.values())

# print(cabinet.items())


# # 목욕탕 폐점
# cabinet.clear()

# print(cabinet)

# menu = ("돈까스" , "치즈까스")
# print(menu[0])
# print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# print(3 in cabinet)
# print(5 in cabinet)


# 집합 (set)
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수", "유재석"])

# # 합집합 ()
# print(java | python)
# print(java.union(python))

# # 교집합 (java와 python을 모두 할 수 있는 개발자)
# print(java & python)

# # 차집합 (java 가능, python 못하는 개발자)
# print( java- python)
# print(java.difference(python))

# # python 할 줄 아는사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 가먹었어요

# java.remove("김태호")
# print(java)

# 자료구조의 변경
# menu ={"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# from random import *
# lst = [1,2,3,4,5]
# # print(lst)
# # shuffle(lst)
# # print(lst)
# print(sample(lst, 1))

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용
# 치킨 1명, 커피 3명


# from random import *

# lst = list(range(1, 21))

# print(lst)
# lst.reverse()
# print(lst)
# # shuffle(lst)

# winner = sample(lst, 4)


# print(" -- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winner[0]))
# print("커피 당첨자 : {0}".format(winner[1:]))
# print(" -- 축하합니다 --")

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? " ))

# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp< 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요."

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# # while person != customer:
# #     print("{0}, 커피가 준비 되었습니다.".format(customer))
# #     person = input("이름이 어떻게 되세요? ")

# absent = [2,5]
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책 읽어봐".format(student))

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]

# print (students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper()for i in students]
# print(students)

# from random import *

# check = " "
# number = 1
# cnt = 0
# while number <= 50:
#     time = randint(5, 50)
#     if 5<= time <= 15:
#         check="O"
#         cnt += 1    
#     print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, number, time))
#     check = " "
#     number += 1

# print("총 탑승 승객 : {0}분".format(cnt))

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
    

# def withdraw_night(balance, money):
#     commision = 100
#     return commision, balance - money - commision

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance , 500)
# commision, balance = withdraw_night(balance , 500)
# print("수수료 {0}원이며, 잔액은 {1} 원입니다.".format(commision, balance))


# def profile(name, age, main_lang):
#     print("이름 : {0} \t나이 : {1}\t주 사용 언어: {2}" \
#           .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

 
# def profile(name, age, main_lang):
#     print("이름 : {0} \t나이 : {1}\t주 사용 언어: {2}" \
#           .format(name, age, main_lang))
    
# profile("유재석")
# profile("김태호")

# stack = [0,1,2,3]

# if stack:
#     print(stack)

# a = 0
# def func():
#     a = 0
#     a += 1
    
# for i in range(10):
#     func()

# print(a)

# def add(a, b):
#     return a+b

# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]

# print(add(list1,list2))
# n=3
# m=4

# array = [[0] * m for _ in range(n)]
# array[1][0] = 5 
# print(array)

# result = eval("(3+5)*7")
# print(result)

# from itertools import product

# data = ['a','b','c']

# result = list(product(data, repeat=2))

# print(result)

# from collections import deque

# deq = deque()

# for i in range(10):
#     deq.append(i)

# print(deq[0])

import heapq

heap = []
values = [1,5,3,2,4,7,6]

for value in values:
    heapq.heappush(heap, value)

print(heap)