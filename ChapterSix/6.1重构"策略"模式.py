# coding=utf-8
# author: yse
# data: 2020-08-21

from collections import namedtuple
from abc import ABCMeta, abstractmethod


Customer = namedtuple('Customer', 'name fidelity')


class LineItem(object):
    """
    商品类
    """
    def __init__(self, product, quantity, prize):
        self.product = product
        self.quantity = quantity
        self.prize = prize

    def total(self):
        return self.quantity * self.prize


class Order(object):
    """
    订单类
    上下文
    """
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '_total'):
            self._total = sum(item.total() for item in self.cart)
        return self._total

    def due(self):
        discount = 0
        if self.promotion.discount:
            print '1111', self.promotion
            discount = self.promotion.discount(self)
        return self._total - discount

    def __repr__(self):
        fmt = '<Order total {:.2f} discount {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABCMeta):
    @staticmethod
    def discount(order):
        """
        返回折扣金额
        """
        pass


class FidelityPromo(Promotion):  # 第一个具体策略
    """
    为积分为1000或以上的顾客提供5%折扣
    """
    @staticmethod
    def discount(order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # 第二个具体策略
    """单个商品为20个或以上时提供10%折扣"""

    @staticmethod
    def discount(order):
        discount = 0
        for item in order.cart:
            discount += item.total() * 0.1 if item.quantity >= 20 else 0
        return discount


class LargeOrderPromo(Promotion):  # 第三个具体策略
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    @classmethod
    def discount(cls, order):
        return order.total() * 0.07 if len({item.product for item in order.cart}) >= 10 else 0


jone = Customer('jone', 1000)
tom = Customer('tom', 0)
lisa = Customer('lisa', 0)
jone_cart = [LineItem('banana', 20, 0.5), LineItem('apple', 10, 1.5)]
print Order(jone, jone_cart, LargeOrderPromo)
