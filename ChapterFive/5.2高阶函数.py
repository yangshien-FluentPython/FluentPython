# -*- coding: utf-8 -*-
# author: yse

import operator


def fact(n):
    return 1 if n < 2 else n * fact(n - 1)


# map(function, sequence) ：对sequence中的item依次执行function(item)，将执行结果function(item)组成一个List返回。
# map 构建0!到5！的阶乘
print map(fact, xrange(6))
print [fact(m) for m in xrange(6)]

# filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）。
print filter(lambda f: f % 2, range(6))
print [n for n in range(6) if n % 2]

# reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用。
# function接收的参数个数只能为2，先把sequence中第一个值和第二个值当参数传给function，再把function的返回值和第三个值当参数传给function，然后只返回一个结果。
print reduce(operator.add, xrange(101))
