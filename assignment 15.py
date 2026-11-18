import gc
import sys
import time
import weakref

# Reference counting
class Demo:
    pass

obj = Demo()

print("Reference count:", sys.getrefcount(obj))

# Check tracked object
print("Is tracked:", gc.is_tracked(obj))

# Create circular reference
a = []
b = []

a.append(b)
b.append(a)

del a
del b

# Garbage collection information
print("Garbage count:", gc.get_count())
print("Threshold:", gc.get_threshold())

# Manual garbage collection
print("Collected objects:", gc.collect())

# Disable automatic garbage collection
gc.disable()
print("GC disabled")

# Enable automatic garbage collection
gc.enable()
print("GC enabled")

# Debug garbage collection
gc.set_debug(gc.DEBUG_SAVEALL)
gc.collect()

print("Garbage objects:", len(gc.garbage))

# Clear debug mode
gc.set_debug(0)

# Weak reference example
obj = Demo()
ref = weakref.ref(obj)

print("Weak reference:", ref())

del obj

print("After deletion:", ref())

print("Program completed")