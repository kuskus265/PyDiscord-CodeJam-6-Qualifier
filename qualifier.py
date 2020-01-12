import datetime, re

def parse_iso8601(timestamp: str) -> datetime.datetime:
  pattern = re.compile("(\d{2})\.(\d{3,6})")
  ms = pattern.findall(timestamp)
  if re.match("(\d{4})[-](\d{2})-(\d{2})T(\d{2})?\:?(\d{2})?\:?(\d{2})?\.?(\d{3,6})?", timestamp) or re.match("(\d{4})[-](\d{2})-(\d{2})$", timestamp):
    d_temp = timestamp[0:10].split('-')
    date = list(map(int, d_temp))
    if timestamp.find("T") == -1:
       time = [0, 0, 0, 0]
    elif timestamp.find("T") != -1:
        pattern = re.compile("(\d{2})\.(\d{3,6})")
        ms = pattern.findall(timestamp)
        t = timestamp[timestamp.find("T") + 1:]
        t_temp = t.split(":")
        try:
          if ms != None:
            t_temp[2] = t_temp[2][0:2]
            t_temp.append(ms[0][1])
        except:
          pass
        time = list(map(int, t_temp))
        while len(time) < 4 :
          time.append(0)
    return datetime.datetime(date[0], date[1], date[2], time[0], time[1], time[2], time[3])
    
  elif re.match("(\d{8})T(\d{6})", timestamp) or re.match("(\d{8}$)", timestamp):
    d_temp = [timestamp[0:4], timestamp[4:6], timestamp[6:8]]
    date = list(map(int, d_temp))
    if timestamp.find("T") != -1:
        t = timestamp[timestamp.find("T") + 1:]
        t_temp = [t[0:2], t[2:4], t[4:6]]
        t_temp = list(filter(None, t_temp))
        try:
          if ms != None:
            t_temp[2] = t_temp[2][0:2]
            t_temp.append(ms[0][1])
        except:
          pass
        time = list(map(int, t_temp))
        while len(time) < 4 :
          time.append(0)
    else:
        time = [0, 0, 0]
    return datetime.datetime(date[0], date[1], date[2], time[0], time[1], time[2], time[3])
  else:
    raise ValueError("Invalid Input String")

