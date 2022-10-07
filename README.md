# Algorithm_Study
코테 대비 알고리즘 공부 ( 사용언어: Python, MySQL ) 

[![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=kws4022)](https://solved.ac/kws4022)

## Python 유용한 문법

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

### zip과 enumerate
``` python
list_ex = ['A', 'B', 'C']
list_ex2 = ['a', 'b', 'c']

enumerate(list_ex) # [(0, 'A'), (1, 'B'), (2, 'C')]
zip(list_ex, list_ex2) # [('A', 'a'), ('B', 'b'), ('C', 'c')]

for i, v in enumerate(list_ex):
    print(i, v) # (0, 'A'), (1, 'B'), (2, 'C')

for v1, v2 in zip(list_ex, list_ex2):
    print(v1, v2) # ('A', 'a'), ('B', 'b'), ('C', 'c')
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

``` python
list.sort(key=lambda x: (x[0], x[-1]))
```

### 배열 내 중복 제거
``` python
listA = [A, B, C, D, D]
print(list(set(listA)).sort()) # [A, B, C, D]
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

``` python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 & set2) # {3, 4} - 교집합
print(set1 | set2) # {1, 2, 3, 4, 5, 6} - 합집합
print(set1 - set2) # {1, 2} - 차집합
```

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
    prime_list = [False, False] + [True]*(num-1)
    for i in range(2, math.ceil(num ** (1/2))):
        if prime_list[i]:
            for j in range(2*i, num+1, i):
                prime_list[j] = False
    return [i for i, v in enumerate(prime_list) if v]
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
- DFS: 모든 경로 탐색 시 이용, stack로 구현
- BFS: 최단 경로 탐색 시 이용, deque으로 구현 (from collections import deque)

### 반복(itertools)
- itertools library를 이용
- 완전 탐색(Brute force)를 사용할 수 있는 상황일 때 자주 사용하는 library

``` python
from itertools import combinations, permutations

list_ex = ['a', 'b', 'c']
perm = permuations(list_ex, 2) # [['a', 'b'], ['a', 'c'], ['b', 'c'], ['c', 'a'], ['c', 'b'], ['b', 'a']]
comb = combinations(list_ex, 2) # [['a', 'b'], ['a', 'c'], ['b', 'c']]
```

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
- python에서는 list로 주로 구현하는 편

#### queue
#### deque(double ended queue)
- 내장함수: popleft, appendleft
- 좌우 끝단 데이터 추가/삭제가 O(1)으로 아주 빠름!
- 대신 임의 데이터 접근이 O(N)으로 느림
- 양쪽에 모두 추가/삭제를 해야 하고, 임의 데이터 접근 할 일이 없을 때 아주 좋음
- BFS 구현에 많이 사용함

#### tuple
#### heap(priority queue)
- heapq 모듈 import하여 사용
- 목록의 최솟값이나 최댓값에 접근할 때 O(1)로 아주 빠름
- 기본적으로 최소 heap만 지원함으로 -num을 저장해서 최솟값을 빼내고 다시 -1을 곱하는 식으로 편법 최대 heap 구현이 가능하다

``` python
import heapq

heap = [] # list 기반
heapq.heappush(heap, num) # num을 heap에 추가
heapq.heappop(heap) # min(heap) 반환하면서 heap에서 제거
heap[0] # min(heap) 접근 - O(1)
heapq.nlargest(len(heap), heap)[0] # max(heap) 접근 - O(N) 이상

listA = [7, 1, 5]
heapq.heapify(listA, num) # list를 heap으로 변환?
```

## MySQL 유용한 문법
### SELECT문 기본 구조
- 실행 순서: FROM - (ON) - (JOIN) - WHERE - GROUP BY - HAVING - SELECT - (DISTINCT) - ORDER BY
``` MySQL
SELECT 
FROM
WHERE
GROUP BY
HAVING
ORDER BY
```

### UPDATE문 기본 구조
- 기본 구조: UPDATE - SET - WHERE
``` MySQL
UPDATE Salary
SET sex = 'f'
WHERE sex = m'
```

### DELETE문 기본 구조
- 기본 구조: DELETE [FROM] - WHERE
``` MySQL
DELETE [FROM] Salary
WHERE sex = 'm'
```

### COALESCE
- COALESCE(A, B, C) # NULL이 아닌 첫 요소를 반환

### IF
- IF(조건문, 참일때, 거짓일때)

### SUBSTR
- 부분 문자열 함수
``` MySQL
# Employees Table에서 name의 첫 문자가 'M'인 row들을 출력
SELECT *
FROM Employees
WHERE SUBSTR(name, 1, 1) = 'M' # name의 '1'번째 문자부터 '1'개만 반환
```

### LIKE문
- 문자열 함수
- %: 0개 이상의 문자열
- _: 1개의 문자

``` MySQL
SELECT *
FROM EMPLOYEES
WHERE Name LIKE '_우성' # 이름이 우성인 사람
```

### IN문
``` MySQL
SELECT *
FROM EMPLOYEES
WHERE Name IN ('김우성', '이우성', '박우성') # 이름이 김우성, 이우성, 박우성인 사람
```

### LIMIT문
- LIMIT N: TOP N개만 출력
- LIMIT N, M: 2번째 idx부터 M번째 idx까지 출력됨 # LIMIT(2, 3)면 2, 3번째 출력
- 맨 마지막에 실행됨(ORDER BY, DISTINCT 이후)

``` MySQL
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME ASC
LIMIT 1
```

### JOIN Query
- 문법: FROM A (조인 종류) B ON (조건문)
``` MySQL
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I INNER JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.DATETIME > O.DATETIME
ORDER BY I.DATETIME
```

### 윈도우 함수
- RANK: 공동 순위만큼 건너뜀 (ex: 1, 2, 2, 4...)
- DENSE_RANK: 공동 순위를 뛰어넘지 않음 (ex: 1, 2, 2, 3...)
- ROW_NUMBER: 공동 순위를 무시함 (ex: 1, 2, 3, 4...)
- LAG: 이전 행 값을 반환 (이전 행이 없으면 NULL 반환)
- LEAD: 이후 행 값을 반환 (이전 행이 없으면 NULL 반환)
- 형식: RANK() OVER ([PARTITION BY A] ORDER BY B ASC) # PARTITION BY ~ 문은 선택사항

``` MySQL
SELECT score, DENSE_RANK() OVER (ORDER BY SCORE DESC) AS 'rank'
FROM Scores
```
