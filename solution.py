"""Solution by <USERNAME>."""


class Solution:
    """Solution to the duplicate zeros problem."""

    def duplicate_zeros(self, arr):
        """Modifies arr in place duplicating all zeros while maitining the original length."""
        i = 0
        j = 0
        arr2 = [i for i in arr]
        while i < len(arr):
            if not arr2[j]:
              arr[i] = 0
              i += 1
              if i < len(arr):
                  arr[i] = 0
            else:
              arr[i] = arr2[j]
            j += 1
            i += 1
        return arr
