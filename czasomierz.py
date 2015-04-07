__author__ = 'Agnieszka'

from threading import Timer

#
# def input_with_timeout(x):
#
#     def time_up():
#         answer= None
#         print 'time up...'
#
#     t = Timer(10,time_up) # x is amount of time in seconds
#     t.start()
#     try:
#         answer = input("enter answer : ")
#     except Exception:
#         print 'pass\n'
#         answer = None
#
#     if answer != True:   # it means if variable have somthing
#         t.cancel()       # time_up will not execute(so, no skip)
#
# input_with_timeout(5) # try this for five seconds

# import msvcrt
# import time
#
# def raw_input_with_timeout(prompt, timeout=30.0):
#     print prompt,
#     finishat = time.time() + timeout
#     result = []
#     while True:
#         if msvcrt.kbhit():
#             result.append(msvcrt.getche())
#             if result[-1] == '\r':   # or \n, whatever Win returns;-)
#                 return ''.join(result)
#             time.sleep(0.1)          # just to yield to other processes/threads
#         else:
#             if time.time() > finishat:
#                 return None
#     print result
#
# raw_input_with_timeout("Ada", 10)


import thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      print count
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 10, ) )
   thread.start_new_thread( print_time, ("Thread-2", 2, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass