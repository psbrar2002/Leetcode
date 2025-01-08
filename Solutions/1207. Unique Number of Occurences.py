from collections import defaultdict

def uniqueOccurrences(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = defaultdict(int)
        
        for i in range(len(arr)):
            
            freq[arr[i]] += 1
        ok = list(freq.values())
        return len(ok) == len(set(ok))

print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1,2]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))