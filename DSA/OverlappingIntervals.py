class Overlapping:
    def Interval(self,interval):
        interval.sort(key=lambda x: x[1])
        n=len(interval)

        # prev=interval[0][1]
        prev=0
        count=1
        for i in range(1,n):
            if interval[i][0]>= interval[prev][1]:
                count+=1
                prev=i

        return n-count
    
inter=Overlapping()
# interval=[[1,3],[4,5],[2,6],[6,9],[5,8]]
n = int(input("How many intervals? "))
interval = []

for i in range(n):
    # 2. Get space-separated values for each duplet (e.g., "1 3")
    user_input = input(f"Enter duplet {i+1} (start end): ").split()
    
    # 3. Convert strings to integers and store as a list [start, end]
    duplet = [int(x) for x in user_input]
    interval.append(duplet)

print("Your intervals:", interval)
a=inter.Interval(interval)
print(f"Intervals to remove: {a}")



print()
class Overlapping:
    def Interval(self, interval):
        # Sort by END time for the greedy approach to work
        interval.sort(key=lambda x: x[1])
        n = len(interval)

        # Variables to track non-overlapping intervals
        prev_end = 0
        non_overlap_count = 1  # The first one is always counted

        for i in range(1, n):
            # If current start >= previous end, they don't overlap
            if interval[i][0] >= interval[prev_end][1]:
                non_overlap_count += 1
                prev_end = i # Update end to the current one

        # Total intervals minus those we kept = minimum removals
        return n - non_overlap_count

inter = Overlapping()
# Note: Ensure the input is a list of lists or list of tuples
data = [[1,3], [4,5], [2,6], [6,9], [5,8]]
a = inter.Interval(data)
print(f"Intervals to remove: {a}") 

