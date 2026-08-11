import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        fi = []
        points.sort()
        print(points)
        for i in range(len(points)):
            pt = points[i]
            x = pt[0]
            y = pt[1]
            dist = math.sqrt(((x)**2) + ((y)**2))
            t = [dist , x,y]
            fi.append(t)
        fi.sort()
        print(fi)
        g = []
        for j in range(k):
            ch = fi[j]
            g.append([ch[1],ch[2]])
        print(g)
        return g

