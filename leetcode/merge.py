#python3

class Solution:
    def merge(self,intervals):
        #get list[list]; return list[list]
        intervals.sort(key = lambda x:x[0])
        #sort the list base on the left point

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])
        
        return merged


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1,4],[3,5]]))