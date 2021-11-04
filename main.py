def data_validator(number):
    """
    data_validator: Validates the data inputted by the user is an integer.

    Args:
        number (int): Inter between 1 and 999.

    Raises:
        ValueError: Must be a positive integer number.
    """
    if not number or not isinstance(number, int) or number < 0 or number > 999:
        raise ValueError(
            '%s must be greater than 0 and less than 1000.' % number)


class DataCapture:
    """
    A class used to accepts numbers and returns an object for querying
    statistics about the inputs. Specifically, the returned object supports
    querying how many numbers in the collection are less than a value, greater
    than a value, or within a range.
    """
    raw_data_list = []
    order_data_list = []
    list_of_counts = []

    def add(self, number):
        """
        add: Add a number to the list.

        Args:
            number (int): Integer number to add to the list.
        """
        data_validator(number)
        self.raw_data_list.append(number)

    def build_stats(self):
        """build_stats: Generate data structure and sum repeated numbers."""
        self.list_of_counts = [0] * (max(self.raw_data_list) + 1)
        for number in self.raw_data_list:
            self.list_of_counts[number] += 1
        for count in range(len(self.list_of_counts)):
            if self.list_of_counts[count] > 0:
                self.order_data_list.extend(
                    [count] * self.list_of_counts[count])


    def less(self, number):
        """
        less: Get the number of an index and return the number of items
        before the index number.

        Args:
            number (int): Index number from a item in a list.

        Returns:
            int: Return the number of items in the list before the index number
        """
        return len(
            self.order_data_list[:self.order_data_list.index(number)])

    def greater(self, number):
        """
        greater [summary]

        Args:
            number (int):  Index number from a item in a list.

        Returns:
            int: Return the number of items in the list after the index number
        """
        return len(
            self.order_data_list[self.order_data_list.index(number)+1:])

    def between(self, init_number, stop_number):
        """
        between: Get the number of an index and return the number of items

        Args:
            init_number (int): Index number from a item in a list.
            stop_number (int): Index number from a item in a list.

        Returns:
            int: Return the number of items in the list between the
            index numbers, including the index of the last member.
        """
        init_pos = self.order_data_list.index(init_number)
        stop_pos = self.order_data_list.index(stop_number)
        return len(self.order_data_list[init_pos:stop_pos]) + 1


if __name__ == '__main__':
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    capture.build_stats()
    print(capture.less(4))
    print(capture.between(3, 6))
    print(capture.greater(4))
