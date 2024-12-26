'''
242. Valid Anagram

Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

'''

# Other Approaches includes using a Counter from Collections and or Sorting but not sure what to reference 



def isAnagram(s, t):
    if len(s) != len(t):
        return False
    freqs,freqt = {},{}   
    for i in range(len(s)):
        freqs[s[i]] = 1 + freqs.get(s[i],0) 
        freqt[t[i]] = 1 + freqt.get(t[i],0) 
    if freqs == freqt: 
        return True
    else:
        return False







print(isAnagram( "anagram","nagaram"))
print(isAnagram( "rat","car"))






'''
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

'''
