#1. 받은 알파벳을 k개로 나눈다
#1-5. 받은s의 갯수를 숫자로 치환
#2. k개로 나눈 알파벳을 중복 검사해서 중복인 단어는 제
#3. 제거후 남은 알파벳만 출력
#-*- coding:utf-8 -*-
def merge_the_tools(s, k):
    split_len = k
    lst = []
    new_lst = []
    for i in range(0, len(s), split_len):
        lst.append(s[i : (i + split_len)])
    for j in lst:
        for l in j:
            if l not in new_lst:
                new_lst.append(l)
        print("".join(new_lst))
        new_lst = []
