class TimeMap:

    def __init__(self):
        self.strg = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.strg:
            self.strg[key] = {timestamp:value}
        else:
            self.strg[key][timestamp] = value

  
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.strg:
            return ''
        elif timestamp in self.strg[key]:
            return self.strg[key][timestamp]
        else:
            latest_ts = max([i if i <= timestamp else -9999 for i in self.strg[key]])
            if latest_ts == -9999:
                return ''
            return self.strg[key][latest_ts]

        
