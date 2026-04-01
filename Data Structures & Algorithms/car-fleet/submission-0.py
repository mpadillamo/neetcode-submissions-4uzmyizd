class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        new_arr = []
        #N
        for i in range(len(position)):
            new_arr.append([position[i],speed[i]])

        #N LOGN
        new_arr.sort()

        #N
        time = []
        for i in range(len(new_arr)):
            p, s = new_arr[i]

            time.append((target - p) / s)
        
        print("TIME:")
        print(time)

        n = 0
        ant = 0
        #N
        for i in range(len(time)-1, -1, -1):
            if time[i] > ant:
                ant = time[i]
                n += 1
        
        return n


            