#!/usr/bin/env python
#-*- coding: utf-8 -*-

try:
	import itertools
	import threading
	import time
	import sys
except ImportError, err:
	raise "Message: " + str(err)


#arr1 = ['◐','◓', '◑', '◒']
 arr1 = ['>','>>','>>>','>>> !','>','>>','>>>','>>> !!','>','>>','>>>','>>> !!!']
_done = False
#here is the animation
def animate():
    for c in itertools.cycle(arr1):
        if _done:
            break
        sys.stdout.write("\rSend " + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\rDone!     \n")



_loader = threading.Thread(target=animate)
# to start loader use the following:
#l._loader.start() <====  start the thread:animate
#l.time.sleep(5)   <====  runtime
#l._done = True    <====  kill thread
