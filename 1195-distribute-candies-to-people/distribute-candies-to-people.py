class Solution(object):
    def distributeCandies(self, candies, num_people):
        res=[0]*num_people
        i=1
        person = 0
        while candies>0:
            give=min(i,candies)

            res[person]+=give
            candies-=give

            i+=1
            person+=1
            if person == num_people:
                person = 0
        return res