# $Id: test_multi4.py,v 1.1 2002/08/08 15:12:37 kjetilja Exp $

import sys, select, time
import pycurl

c1 = pycurl.init()
c2 = pycurl.init()
c3 = pycurl.init()
c1.setopt(pycurl.URL, 'http://www.python.org')
c2.setopt(pycurl.URL, 'http://curl.haxx.se')
c3.setopt(pycurl.URL, 'http://slashdot.org')
c1.body = file("doc1", "w")
c2.body = file("doc2", "w")
c3.body = file("doc3", "w")
c1.setopt(pycurl.WRITEFUNCTION, c1.body.write)
c2.setopt(pycurl.WRITEFUNCTION, c2.body.write)
c3.setopt(pycurl.WRITEFUNCTION, c3.body.write)

m = pycurl.multi_init()
m.add_handle(c1)
m.add_handle(c2)
m.add_handle(c3)

num_handles = m.perform()

while num_handles:

    if 0:
        # XXX: this does not work for some reason, num_handles never goes 0
        # if we call m.fdset()
        r, w, e = m.fdset()
    num_handles = m.perform()
    print num_handles
        
m.remove_handle(c3)
m.remove_handle(c2)
m.remove_handle(c1)
m.cleanup()
c1.body.close()
c2.body.close()
c3.body.close()
c1.cleanup()
c2.cleanup()
c3.cleanup()
