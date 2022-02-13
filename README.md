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

``` python
print(' '.join(list))
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

### 최대공약수 - 유클리드 호제법
- 최대공약수 구하는 알고리즘
- 고전 로직보다는 확실히 빠름
``` python
# num1 >= num2임을 보장
if num1 < num2:
    num1, num2 = num2, num1

while num2:
    rest = num1 % num2
    num1 = num2
    num2 = rest

print(num1) # 최대공약수
```

### 최소공배수 - 두 수의 곱 = 최소공배수 * 최대공약수
- lcm = (num1 * num2) / gcd(num1, num2)

### 기본 자료 구조
#### list
- [a, b, c, d, e]
- 내장 함수: append, pop, index...
- 데이터 접근이 O(1)으로 매우 빠르다.
- 대신 pop(0), index(), insert() 등의 함수가 O(N)으로 느리다.

#### set
- {a, b, c, d, e}
- 중복을 허용하지 않음

#### dictionary
- {}
- defaultdict 이용하면 편하게 사용할 수 있음
- lambda: 1 등으로 기본 수치 설정 가능
``` python
from collections import defaultdict

dict_ex = defaultdict(list)
print(dict_ex) # defaultdict(<class 'list'>, {})
print(dict_ex[0]) # [] - defaultdict에 없는 key를 호출할 때 dict_ex[0] = []로 자동 생성
```
#### stack
#### queue
#### deque
- 내장함수: popleft, appendleft
- 데이터 접근이 O(N)으로 느림
- 대신 데이터 추가/삭제가 O(1)
#### tuple