# -*- coding: utf-8 -*-


def tag(name, *content, **attrs):
    if attrs:
        attr_str = ''.join(' %s=%s' % (attr, value) for attr, value in attrs.items())
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, str(co), name) for co in content)
    else:
        return '<%s%s />' % (name, attr_str)


# print tag('br')
#
# print tag('p', 'hello')
#
# print tag('p', 'hello', id=1)
#
# print tag('p', 'hello', id=1, title='Sun')
#
# mt_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
# print tag(**mt_tag)
print tag.__defaults__
print tag.__code__.co_varnames
print tag.__code__.co_argcount
