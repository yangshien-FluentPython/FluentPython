# -*— coding:utf-8 -*-
# author: yse

import operator
import functools
import collections


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]


# 利用reduce和mul进行累乘
def fact_mul(n):
    return functools.reduce(operator.mul, range(1, n + 1))


# 使用itemgetter排序一个元组列表，穿一个参数可以进行排序
def fact_itemgetter(n):
    """

    :param n: index of sorted
    :return: tuple of sorted
    """
    return sorted(metro_data, key=operator.itemgetter(n), reverse=True)


# attrgetter
def fact_attrgetter():
    LatLong = collections.namedtuple('LatLong', 'lat long')
    Metropolis = collections.namedtuple('Metropolis', 'name cc pop coord')
    metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
    name_lat = operator.attrgetter('name', 'coord.lat')
    for city in sorted(metro_areas, key=operator.attrgetter('coord.lat')):
        print name_lat(city)
    return metro_areas


# methodcaller
def func_methodcaller(s):
    """

    :param s: string
    :return: string
    """
    up_case = operator.methodcaller('upper')
    replace_case = operator.methodcaller('replace', ' ', '-')
    return up_case(s), replace_case(s)


print fact_mul(10)

print fact_itemgetter(2)

cc_name = operator.itemgetter(1, 0)
for i in metro_data:
    print (cc_name(i))

fact_attrgetter()

print func_methodcaller('This Is Test Case')
