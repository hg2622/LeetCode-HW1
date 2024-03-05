class Solution(object):
    def videoStitching(self, clips, time):
        sort2 = sorted(clips, key=lambda x: x[0])
       
    

        if (sort2[0][0] != 0):
            return -1

        record = 2
        top = sort2[0][1]
        low=top

        i=1
        while(i<len(sort2)):
            if (sort2[i][0] > top):
                return -1
        

            first=True
            while(sort2[i][0]<=low):
                if (sort2[i][1] > top):
                    top = sort2[i][1]
                if (i==len(sort2)-1):
                    record+=1
                    break
                first=False
                i+=1

            if (i == len(sort2) - 1):
                break


            if(sort2[0][0]==0):
                record-=1

            record+=1
            low=top
           



        if(top>=time):
            return record

        return -1
