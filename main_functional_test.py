import random
from main import DataCapture

# Functional test with random values in a len list and items. #
input_number = int(input("Select a number between 1 and 999: "))
random_list_length = random.randint(1, input_number)
random_list = []
random_number = None

capture = DataCapture()

for index_list in range(random_list_length):
    random_number = random.randint(1, input_number)
    capture.add(random_number)

capture.build_stats()
print("-Ordered list-")
print(capture.order_data_list)
print("Capture less method")
less = random.choice(capture.order_data_list)
print("Less number: %s" % less)
print(capture.less(less))
print("-Capture greater method-")
greater = random.choice(capture.order_data_list)
print("Greater number: %s" % greater)
print(capture.greater(greater))
print("-Capture between method-")
n1 = random.choice(capture.order_data_list)
n2 = random.choice(capture.order_data_list)
if n1 < n2:
    print("Between %s and %s" % (n1, n2))
    print(capture.between(n1, n2))
else:
    print("Between %s and %s" % (n2, n1))
    print(capture.between(n2, n1))
