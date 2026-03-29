class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        keyList = self.timeMap[key]
        l, r = 0, len(keyList) - 1
        lastPrevValue = ""
        while l <= r:
            m = l + (r -l) // 2           
            if keyList[m][0] <= timestamp:
                lastPrevValue = keyList[m][1]
                l = m + 1
            else:
                r = m - 1
        return lastPrevValue

        
