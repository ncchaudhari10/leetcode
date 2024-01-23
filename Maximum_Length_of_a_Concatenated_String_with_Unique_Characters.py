class Solution:
    def recur(self, arr, i, data):
        # Base case: If we have processed all strings in the array, return the length of the current set of characters.
        if i == len(arr):
            return len(data)

        # Initialize variables for "pick" and "not pick" scenarios.
        pick = notpick = -float('inf')
        
        # Flag to determine if the current string can be added to the set.
        flag = True

        # Temporary set to store characters from the current string.
        temp = set()

        # Iterate through characters in the current string.
        for s in arr[i]:
            # Check if the character is already in the current set.
            if s in data:
                flag = False
                break
            temp.add(s)

        # If the flag is True, it means we can pick the current string and update the set.
        if flag:
            temp = data.union(temp)
            pick = self.recur(arr, i + 1, temp)
        
        # Regardless of whether we pick the current string or not, make a recursive call without the current string.
        notpick = self.recur(arr, i + 1, data)

        # Return the maximum length between "pick" and "not pick".
        return max(pick, notpick)

    def maxLength(self, arr: List[str]) -> int:
        # Filter out strings with duplicate characters.
        strings = [i for i in arr if len(i) == len(set(i))]
        
        # Start the recursive process from the beginning with an empty set.
        return self.recur(strings, 0, set())
