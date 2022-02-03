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

- set()을 사용하면 중복이 제거된다! 단 순서도 뒤섞이기 때문에 다시 sort 해준다.
- for문을 이용하여 중복을 제거 할 수도 있다.

### set(집합)
- 집합 자료형으로, 중복을 허용하지 않음
- add(), remove(), discard(), clear() 등의 내장 함수가 있음

### set.remove() vs set.discard()
- set.remove(20) 호출 시 20이 set 내에 없다면 keyError를 반환한다.
- set.discard(20)은 호출 시 20이 있다면 제거, 없다면 keyError를 반환하지 않는다(아무 행동도 하지 않음).

### dictionary
``` python
dict_A = {}
dict_A['key'] = 'value'
print(dict_A['key']) = 'value'
```
- key-value 구조를 가지는 자료 구조.


### 문자열 내의 문자가 숫자인지 확인
``` python
str1 = '50'
print(str1.isdigit()) # true 반환
```

### 소수 판별법
#### 수학적 개념에 입각
- 2 ~ num-1 사이 구간에서 num의 약수가 있는지 판단
``` python
def isPrime(num):
    for i in range(2, num): 
        if num % i == 0:
            return False
        
    return True
```

#### 보다 빠른 방법
- 2 ~ sqrt(num) 사이 구간에서 num의 약수가 있는지 판단
``` python
def isPrime(num):
    for i in range(2, math.ceil(num ** 1/2)): 
        if num % i == 0:
            return False
        
    return True
```

### 에라스토테네스의 체
- 어떤 구간에서 소수의 list를 얻고 싶을 때 사용
- 2 ~ num 사이의 소수 list를 얻고 싶다면
``` python
def getPrimeList(num):
    listA = [0]* (num + 1)
    for i in range(2, math.ceil(num ** 1/2)):
        if listA[i] == 0: continue
        for j in range(2*i, num + 1, i):
            listA[j] == 0
```