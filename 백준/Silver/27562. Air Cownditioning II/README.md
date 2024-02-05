# [Silver II] Air Cownditioning II - 27562 

[문제 링크](https://www.acmicpc.net/problem/27562) 

### 성능 요약

메모리: 31120 KB, 시간: 72 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 2월 6일 08:51:57

### 문제 설명

<p>With the hottest recorded summer ever at Farmer John's farm, he needs a way to cool down his cows. Thus, he decides to invest in some air conditioners.</p>

<p>Farmer John's $N$ cows ($1 \leq N \leq 20$) live in a barn that contains a sequence of stalls in a row, numbered $1 \ldots 100$. Cow $i$ occupies a range of these stalls, starting from stall $s_i$ and ending with stall $t_i$. The ranges of stalls occupied by different cows are all disjoint from each-other. Cows have different cooling requirements. Cow $i$ must be cooled by an amount $c_i$, meaning every stall occupied by cow $i$ must have its temperature reduced by at least $c_i$ units.</p>

<p>The barn contains $M$ air conditioners, labeled $1 \ldots M$ ($1 \leq M \leq 10$). The $i$th air conditioner costs $m_i$ units of money to operate ($1 \leq m_i \leq 1000$) and cools the range of stalls starting from stall $a_i$ and ending with stall $b_i$. If running, the $i$th air conditioner reduces the temperature of all the stalls in this range by $p_i$ ($1 \leq p_i \leq 10^6$). Ranges of stalls covered by air conditioners may potentially overlap.</p>

<p>Running a farm is no easy business, so FJ has a tight budget. Please determine the minimum amount of money he needs to spend to keep all of his cows comfortable. It is guaranteed that if FJ uses all of his conditioners, then all cows will be comfortable.</p>

### 입력 

 <p>The first line of input contains $N$ and $M$.</p>

<p>The next $N$ lines describe cows. The $i$th of these lines contains $s_i$, $t_i$, and $c_i$.</p>

<p>The next $M$ lines describe air conditioners. The $i$th of these lines contains $a_i$, $b_i$, $p_i$, and $m_i$.</p>

<p>For every input other than the sample, you can assume that $M = 10$.</p>

### 출력 

 <p>Output a single integer telling the minimum amount of money FJ needs to spend to operate enough air conditioners to satisfy all his cows (with the conditions listed above).</p>

