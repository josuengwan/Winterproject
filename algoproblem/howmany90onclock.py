#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
시침은 하루에 2회전, 분침은 하루에 24회전 한다.
같은 방향으로 회전하므로 시침에 대한 분침의 "상대적인" 회전수는
하루에 24-2 = 22회전이다.
시침과 분침이 직각을 이루는 경우는 분침이 시침에 대해 다음과 같은 회전수를
했을 경우이다.
1/4, 3/4, 1+1/4, 1+3/4, ... , 21+1/4 , 21+3/4
따라서 하루에 총 44번 직각을 이룬다는 것을 알 수 있다.
위의 수열을 일반항으로 표현하면
(2n-1)/4 (1<=n<=44)이다.
상대적인 1회전에 걸리는 시간은 24/22 = 12/11 시간이고,
위의 일반항에 12/11을 곱하면 24시간중 직각을 이루는 시간의 일반항이 나온다.
즉,
3(2n-1)/11 (1<=n<=44)
위의 결과값은 시간이므로 프로그램에서는 이를 시간과 분으로 적절히 변환해서
표현하면 되겠다.
예) 3.25시 -> 3:15
'''
for n in range(1, 45):
    h=(6*n-3)/11.0
    m = (h-int(h))*60
    print "%02d:%02d"%(h,m)
print "Total:44번!"

#answer : http://codingdojang.com/scode/487?orderby=#answer-filter-area
