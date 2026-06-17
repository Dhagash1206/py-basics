class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        def func(l, r, lmax, rmax):

            if l > r:
                return 0

            if lmax <= rmax:

                water = max(0, lmax - height[l])

                return water + func(
                    l + 1,
                    r,
                    max(lmax, height[l]),
                    rmax
                )

            else:

                water = max(0, rmax - height[r])

                return water + func(
                    l,
                    r - 1,
                    lmax,
                    max(rmax, height[r])
                )

        return func(0, n - 1, 0, 0)




# 2nd Solution 


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water