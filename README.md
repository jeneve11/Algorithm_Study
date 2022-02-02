# Algorithm_Study
코테 대비 알고리즘 공부 ( 사용언어: Python ) 


## 유용한 문법

### 여러 숫자 한 줄에 입력받을 때
``` python
input_nums = [int(i) for i in input().split()]
# 혹은
input_nums = list(map(int, input().split()))
```

### 여러 줄 입력
``` python
sys.stdin.readline().rstrip()
```
- input()과 같지만 여러 줄 (more than 1,000 lines) 입력 받을 때 훨씬 빠르다.
- rstrip()은 문자열 우측 개행문자를 제거해준다.

### 배열 순회
``` python
for i, num in enumerate(list):
    print(i, num)
```

### 배열 출력
``` python
for i in list:
    print(i)
```

### 배열 정렬
``` python
list = [A, B, C, D, E]
list.sort()
# 혹은
new_list = sorted(list)
```
- sort는 반환값 없이 기존 list를 수정하고,
sorted 함수는 기존 list에는 변화 없이 새로운 list를 만들어서 반환한다.

### 배열 내 중복 제거
``` python
list = [A, B, C, D, D]
print(list(set(list)).sort()) # [A, B, C, D]
```

- set() 함수를 사용하면 중복이 제거된다! 단 순서도 마구 뒤섞이기 때문에 다시 sort 해준다.
- for문을 이용하여 중복을 제거 할 수도 있다.

### 문자열 내의 문자가 숫자인지 확인
``` python
str1 = '50'
print(str1.isdigit()) # true 반환
```
