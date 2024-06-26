class Solution:
    def toh(self, N, fromm, to, aux):
        if N == 1:
            print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
            print("\n")
            return 1
        moves = 0
        moves += self.toh(N - 1, fromm, aux, to) # Recursive call
        moves += 1 # Increment the total moves count for the current step # Move the remaining largest disk from 'fromm' to 'to'
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        moves += self.toh(N - 1, aux, to, fromm) # Recursive call
        return moves # Return the total moves made for this step and all recursive steps
print(Solution().toh(4, 1, 3, 2))