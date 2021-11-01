import matplotlib.pyplot as plt
from timeit import repeat

# Test complexity of build stat method. #
len_items = 100
times = []
for index_list in range(100):
    code = f"import random;" \
           f"from main import DataCapture;" \
           f"capture = DataCapture();" \
           f"random_number = random.randint(1, {len_items});" \
           "capture.add(random_number);"
    stmt = "capture.build_stats()"
    time_execution = repeat(setup=code, stmt=stmt, repeat=3, number=5)
    times.append(min(time_execution))

plt.plot(range(len_items), times)
plt.xlabel('items (Lenght of the list - %s)' % len_items)
plt.ylabel('time (s)')
plt.title('Time Complexity of method build_stats()')
plt.show()
