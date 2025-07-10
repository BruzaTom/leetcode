class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Set to store characters currently in the substring window
        char_set = set()

        # Left pointer of the sliding window
        left = 0

        # Tracks the maximum length of substring found so far
        max_len = 0

        # Loop through the string with the right pointer
        for right in range(len(s)):

            # If the character at 'right' is already in the set, it means a duplicate is found
            # Move 'left' forward to remove duplicates until 's[right]' can be added safely
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set (it's now unique in the window)
            char_set.add(s[right])

            # Update max_len to reflect the length of the current valid window
            max_len = max(max_len, right - left + 1)

        # Return the maximum length found
        return max_len
