import codewars_test as test
from solution import minimum_transportation_price

@test.describe("5 Fixed tests")
def fixed_tests():
    @test.it("5 Sample tests")
    def sample_tests():
        suppliers = [10, 7, 13]
        consumers = [6, 20, 4]
        costs = [
            [4, 12, 3],
            [20, 1, 6],
            [7, 0, 5]
        ]
        test.assert_equals(minimum_transportation_price(suppliers, consumers, costs), 43)

        suppliers = [8, 15, 21]
        consumers = [8, 36]
        costs = [
            [9, 16],
            [7, 13],
            [25, 1]
        ]
        test.assert_equals(minimum_transportation_price(suppliers, consumers, costs), 288)

        suppliers = [31, 16]
        consumers = [14, 17, 16]
        costs = [
            [41, 18, 0],
            [4, 16, 37]
        ]
        test.assert_equals(minimum_transportation_price(suppliers, consumers, costs), 358)

        suppliers = [10, 20, 20]
        consumers = [5, 25, 10, 10]
        costs = [
            [2, 5, 3, 0],
            [3, 4, 1, 4],
            [2, 6, 5, 2]
        ]
        test.assert_equals(minimum_transportation_price(suppliers, consumers, costs), 150)

        suppliers = [13, 44, 27, 39, 17]
        consumers = [28, 12, 30, 17, 19, 34]
        costs = [
            [6, 6, 12, 8, 13, 13],
            [7, 20, 5, 16, 11, 16],
            [4, 6, 19, 0, 2, 18],
            [1, 16, 6, 11, 8, 11],
            [5, 6, 11, 1, 6, 14]
        ]
        test.assert_equals(minimum_transportation_price(suppliers, consumers, costs), 759)