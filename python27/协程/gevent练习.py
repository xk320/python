# -*- coding: UTF-8 -*-
from gevent import monkey;

monkey.patch_all()
import gevent
import urllib2


def test(n):
    with(open('a', 'a')) as f:
        print 'my read %s' % n
        f.write(n)
        print 'my write %s' % n


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(test, '1'),
        gevent.spawn(test, '\n2'),
        gevent.spawn(test, '\n3'),
        gevent.spawn(test, '\n4'),
        gevent.spawn(test, '\n5'),
        gevent.spawn(test, '\n6'),
        gevent.spawn(test, '\n7'),
        gevent.spawn(test, '\n8'),
        gevent.spawn(test, '\n9'),
        gevent.spawn(test, '\n10'),
        gevent.spawn(test, '\n11'),
        gevent.spawn(test, '\n12'),
        gevent.spawn(test, '\n13'),
        gevent.spawn(test, '\n14')
    ])
