import unittest
# def max_element(lst):
#     max_element = lst[0]
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if i > max_element: 
#                 max_element = lst[j]
#     return max_element

def max_element_linear(lst):
    max_el = lst[0]
    for i in range(len(lst)):
        if i > max_el:
            max_el = lst[i]


class TestMax(unittest.TestCase):
    def test_max(self):
        assert max_element_linear([1,5,3,9,2]) == 9
        assert max_element_linear([-10, -5, -8, -3]) == -3
        assert max_element_linear([0,0,0,00,0,0]) == 0

if __name__ == "__main__":
    unittest.main()