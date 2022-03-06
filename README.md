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

### 재귀 문제 팁
``` python
import sys
sys.setrecursionlimit(10 ** 6)
```
- 파이썬 기본 재귀 제한 1,000회에서 재귀 제한을 1,000,000회로 늘리는 설정
- 이거 없으면 대부분의 재귀문제에서 런타임 에러 보게 됨

### * (asterisk)
``` python
list_ex = [1, 2, 3]
print(list_ex) # [1, 2, 3]
print(*list_ex) # 1 2 3

```
- iter 자료형 내부 값들을 unpacking하여 반환함

### 배열 순회
``` python
for i, num in enumerate(list):
    print(i, num)
```

### zip과 enumerate
``` python
list_ex = ['A', 'B', 'C']
list_ex2 = ['a', 'b', 'c']

enumerate(list_ex) # [(0, 'A'), (1, 'B'), (2, 'C')]
zip(list_ex, list_ex2) # [('A', 'a'), ('B', 'b'), ('C', 'c')]

for i, v in enumerate(list_ex):
    pass

for v1, v2 in zip(list_ex, list_ex2):
    pass

```

### 배열 출력
``` python
for i in list: print(i)
```

``` python
print(' '.join(list))
```
- 이 코드는 문자열 리스트에서만 가능

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

### 순열과 조합
``` python
import itertools

list_ex = [1, 2, 3, 4]
itertools.combinations(list_ex, 2) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
itertools.permutations(list_ex, 2)
```

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
dict_A.keys() # ['key']
dict_A.values() # ['value']
dict_A.items() # [('key', 'value')]
```
- key-value 구조를 가지는 자료 구조.

### 문자열 내의 문자가 숫자인지 확인
``` python
str1 = '50'
print(str1.isdigit()) # true 반환
```

### float data가 정수인지 소수인지 확인
``` python
>>> (1.0).is_integer()
True
>>> (1.555).is_integer()
False
```

### 부동 소수점 이슈
``` python
# x와 y의 비율(백분율)을 구할 때
x / y * 100 # False - 바로 나눠서 부동소수점 이슈가 생길 확률이 있다
x * 100 / y # True - x 자릿수를 2개 올리고 y로 나누는 연산을 수행하기 때문에 부동소수점 이슈가 생길 확률이 낮아진다
```

### 반올림, 올림, 버림
``` python
num = 99/2
round(num) # 반올림
math.ceil(num) # 50 - 올림
int(num) # 49 - 버림 or math.trunc
```

### 약수 찾기
- 어떤 수 n의 약수를 찾는 데에는 O(root(n))의 시간이 걸린다.
- 1 ~ root(n) 까지의 수만 n의 약수인지 조사하면, 나머지 약수들은 n // [이미 조사한 약수들]이기 때문이다.

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

### 그래프
- DFS: 최단 경로 탐색, deque로 구현
- BFS: 모든 경로 탐색, stack으로 구현

### 기본 자료 구조
#### list
- [a, b, c, d, e]
- 내장 함수: append, pop, index...
- 데이터 접근(listA[n]), 데이터 맨뒤에 추가(append), 맨뒤 삭제(pop()) 등이 O(1)으로 매우 빠르다.
- reverse - O(N)
- 데이터 맨 뒤에서만 추가, 삭제하는 경우에 아주 어울리는 자료 구조
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
dict_ex2 = defaultdict(lambda: -1) # 없는 key 호출 시 -1로 생성되는 int형 dictionary 생성
```
#### stack
#### queue
#### deque(double ended queue)
- 내장함수: popleft, appendleft
- 데이터 접근이 O(N)으로 느림
- 대신 데이터 추가/삭제가 O(1)
#### tuple
#### heap(priority queue)
- heapq 모듈 import하여 사용
``` python
import heapq

heap = [] # list 기반
heapq.heappush(heap, num) # num을 heap에 추가
heap[0] # min(heap) 접근 - O(1)
heapq.nlargest(len(heap), heap)[0] # max(heap) 접근 - O(N) 이상

listA = [7, 1, 5]
heapq.heapify(listA, num) # list를 heap으로 변환?
```