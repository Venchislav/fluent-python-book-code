from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)

# We have a really strange method deque rotate

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

# Just appends element on the left
dq.appendleft(-1)
print(dq)

# Just extends deque with unziped elems
dq.extend([11, 12, 13])
print(dq)
# The same thing is about deque extendleft, but it's on left

dq.extendleft([-13, -12, -11])
print(dq)
