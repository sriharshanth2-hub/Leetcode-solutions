from datetime import datetime
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        date1 = datetime.strptime(arriveAlice,"%m-%d")
        date2 = datetime.strptime(leaveAlice,"%m-%d")
        date3 = datetime.strptime(arriveBob,"%m-%d")
        date4 = datetime.strptime(leaveBob,"%m-%d")
        d1 = max(date1,date3)
        d2 = min(date2,date4)
        if d1 > d2:
            return 0

        return (d2 - d1).days + 1