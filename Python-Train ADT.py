def get_train_code(train):
    return train[0]
    pass

def make_line(name, stations):
    return (name, stations)
    pass
def get_line_name(line):
    return line[0]
    pass
def get_line_stations(line):
    return line[1]
    pass
def get_station_by_name(line, station_name):
    for i in get_line_stations(line):
        if station_name in i:
            return i
    else:
        return None
    pass
def get_station_by_code(line, station_code):
    for i in get_line_stations(line):
        if station_code in i:
            return i
    else:
        return None
    pass
def get_station_position(line, station_code):
    s = get_line_stations(line)
    x = len(s)
    for i in range(0,x):
        if station_code in s[i]:
            return i
    return -1 
# if you want the loop to continue and only print the o/p for none at the end then bring the return outside!
    passdef make_line(name, stations):
    return (name, stations)
    pass
def get_line_name(line):
    return line[0]
    pass
def get_line_stations(line):
    return line[1]
    pass
def get_station_by_name(line, station_name):
    for i in get_line_stations(line):
        if station_name in i:
            return i
    else:
        return None
    pass
def get_station_by_code(line, station_code):
    for i in get_line_stations(line):
        if station_code in i:
            return i
    else:
        return None
    pass
def get_station_position(line, station_code):
    s = get_line_stations(line)
    x = len(s)
    for i in range(0,x):
        if station_code in s[i]:
            return i
    return -1 
# if you want the loop to continue and only print the o/p for none at the end then bring the return outside!
    pass

def get_is_moving(train_position):
    return train_position[0]
    '''your code here'''
    pass
def get_direction(line, train_position):
    position1 = get_station_position(line,get_station_code(get_from_station(train_position)))
    position2 = get_station_position(line,get_station_code(get_next_station(train_position)))
    if position1 < position2:
        return 0
    else:
        return 1
    pass
def get_from_station(train_position):
    return train_position[1]
    pass
'''
get_stopped_station(train_position) takes in a TrainPosition and returns the Station
that the train is currently stopped at. If the train is stationary, it is currently
stopped at the from_station. If the train is not stationary, return None.
'''
def get_stopped_station(train_position):
    if get_is_moving(train_position) == False :
        return train_position[1]
    else:
        return None
    pass
def get_previous_station(train_position):
    if get_is_moving(train_position) == True :
        return train_position[1]
    else:
        return None
    pass
def get_next_station(train_position):
    return train_position[2]
    pass
def get_is_moving(train_position):
    return train_position[0]
    '''your code here'''
    pass
def get_direction(line, train_position):
    position1 = get_station_position(line,get_station_code(get_from_station(train_position)))
    position2 = get_station_position(line,get_station_code(get_next_station(train_position)))
    if position1 < position2:
        return 0
    else:
        return 1
    pass
def get_from_station(train_position):
    return train_position[1]
    pass
'''
get_stopped_station(train_position) takes in a TrainPosition and returns the Station
that the train is currently stopped at. If the train is stationary, it is currently
stopped at the from_station. If the train is not stationary, return None.
'''
def get_stopped_station(train_position):
    if get_is_moving(train_position) == False :
        return train_position[1]
    else:
        return None
    pass
def get_previous_station(train_position):
    if get_is_moving(train_position) == True :
        return train_position[1]
    else:
        return None
    pass
def get_next_station(train_position):
    return train_position[2]
    pass


def make_schedule_event(train, train_position, time):
    return (train, train_position, time)
    pass
def get_train(schedule_event):
    return schedule_event[0]
    '''your code here'''
    pass
def get_train_position(schedule_event):
    return schedule_event[1]
    pass
def get_schedule_time(schedule_event):
    return schedule_event[2]
    passdef make_schedule_event(train, train_position, time):
    return (train, train_position, time)
    pass
def get_train(schedule_event):
    return schedule_event[0]
    '''your code here'''
    pass
def get_train_position(schedule_event):
    return schedule_event[1]
    pass
def get_schedule_time(schedule_event):
    return schedule_event[2]
    pass

def parse_lines(data_file):
    rows = read_csv(data_file)[1:]
    lines = ()
    curr_line_name = rows[0][2]
    curr_line_stations = ()
    for row in rows:
        code, station_name, line_name = row
        if line_name == curr_line_name:
            curr_line_stations = curr_line_stations + (make_station(code,station_name),)
            pass
        else:
            lines = lines + ((curr_line_name,curr_line_stations),)
            curr_line_name = line_name
            curr_line_stations = (make_station(code,station_name),)
            pass
    lines = lines + ((curr_line_name,curr_line_stations),)
    return lines
def parse_lines(data_file):
    rows = read_csv(data_file)[1:]
    lines = ()
    curr_line_name = rows[0][2]
    curr_line_stations = ()
    for row in rows:
        code, station_name, line_name = row
        if line_name == curr_line_name:
            curr_line_stations = curr_line_stations + (make_station(code,station_name),)
            pass
        else:
            lines = lines + ((curr_line_name,curr_line_stations),)
            curr_line_name = line_name
            curr_line_stations = (make_station(code,station_name),)
            pass
    lines = lines + ((curr_line_name,curr_line_stations),)
    return lines


def parse_events_in_line(data_file, line):
    rows = read_csv(data_file)[1:]
    events = ()
    for row in rows:
        train_code, is_moving, fromstn_code, tostn_code, date, time = row
        yr = int(date[6:])
        mth = int(date[3:5])
        day = int(date[0:2])
        hour = int(time[0:2])
        minute = int(time[3:])
        fromstn_code = get_station_by_code(line, fromstn_code)
        tostn_code = get_station_by_code(line, tostn_code)
        if is_moving.upper() == 'TRUE':
            is_moving = True 
        else:
            is_moving = False
            
        events += ((make_train(train_code,),make_train_position(is_moving,fromstn_code,tostn_code), 
        datetime.datetime(yr,mth,day,hour,minute)),)
        pass
    return events
def parse_events_in_line(data_file, line):
    rows = read_csv(data_file)[1:]
    events = ()
    for row in rows:
        train_code, is_moving, fromstn_code, tostn_code, date, time = row
        yr = int(date[6:])
        mth = int(date[3:5])
        day = int(date[0:2])
        hour = int(time[0:2])
        minute = int(time[3:])
        fromstn_code = get_station_by_code(line, fromstn_code)
        tostn_code = get_station_by_code(line, tostn_code)
        if is_moving.upper() == 'TRUE':
            is_moving = True 
        else:
            is_moving = False
            
        events += ((make_train(train_code,),make_train_position(is_moving,fromstn_code,tostn_code), 
        datetime.datetime(yr,mth,day,hour,minute)),)
        pass
    return events


from math import * 
def is_valid_event_in_line(bd_event, line):
    station1 = get_from_station(get_train_position(bd_event))
    station2 = get_next_station(get_train_position(bd_event))
    s1 = get_station_position(line,get_station_code(station1))
    s2 = get_station_position(line,get_station_code(station2))
    diff = s1 - s2 
    bdtime = get_schedule_time(bd_event)
    bdtimeh = bdtime.hour 
    bdtimem = bdtime.minute 
    if abs(diff) == 1:
        if bdtimeh < 23 and bdtimeh > 6:
            return True
        elif bdtimeh == 23 and bdtimem == 0 :
            return True
        else:
            return False
    else:
        return False
        
    pass
def get_from_station(train_position):
    return train_position[1]from math import * 
def is_valid_event_in_line(bd_event, line):
    station1 = get_from_station(get_train_position(bd_event))
    station2 = get_next_station(get_train_position(bd_event))
    s1 = get_station_position(line,get_station_code(station1))
    s2 = get_station_position(line,get_station_code(station2))
    diff = s1 - s2 
    bdtime = get_schedule_time(bd_event)
    bdtimeh = bdtime.hour 
    bdtimem = bdtime.minute 
    if abs(diff) == 1:
        if bdtimeh < 23 and bdtimeh > 6:
            return True
        elif bdtimeh == 23 and bdtimem == 0 :
            return True
        else:
            return False
    else:
        return False
        
    pass
def get_from_station(train_position):
    return train_position[1]

def get_location_id_in_line(bd_event, line):
    train_position = get_train_position(bd_event)
    is_moving = get_is_moving(train_position)  
    st1 = get_from_station(train_position)
    st2 = get_next_station(train_position)
    st1code = get_station_code(st1)
    st2code = get_station_code(st2)
    st1p = get_station_position(line,st1code)
    st2p = get_station_position(line,st2code)
    if not is_moving:
        location = st1p 
    else:
        if st1p > st2p:
            location =  0.5 + st2p:
        else:
            location = 0.5 + st1p
            
    return location 
    pass
def get_from_station(train_position):
    return train_position[1]def get_location_id_in_line(bd_event, line):
    train_position = get_train_position(bd_event)
    is_moving = get_is_moving(train_position)  
    st1 = get_from_station(train_position)
    st2 = get_next_station(train_position)
    st1code = get_station_code(st1)
    st2code = get_station_code(st2)
    st1p = get_station_position(line,st1code)
    st2p = get_station_position(line,st2code)
    if not is_moving:
        location = st1p 
    else:
        if st1p > st2p:
            location =  0.5 + st2p:
        else:
            location = 0.5 + st1p
            
    return location 
    pass
def get_from_station(train_position):
    return train_position[1]

def get_schedules_at_time(train_schedule, time):
    counter = ()
    for event in train_schedule:
        if get_schedule_time(event) == time:
            counter = counter + (event, )
    return counter 
def get_schedules_near_loc_id_in_line(train_schedule, line, loc_id):
    counter = ()
    for event in train_schedule:
        if abs((get_location_id_in_line(event, line))- loc_id) <= 0.5:
            counter = counter + (event, )
    return counter 
def get_rogue_schedules_in_line(train_schedule, line, time, loc_id):
    rtime = get_schedules_at_time(train_schedule, time)
    tpl = get_schedules_near_loc_id_in_line(rtime,line,loc_id)
    return tpl
def get_schedules_at_time(train_schedule, time):
    counter = ()
    for event in train_schedule:
        if get_schedule_time(event) == time:
            counter = counter + (event, )
    return counter 
def get_schedules_near_loc_id_in_line(train_schedule, line, loc_id):
    counter = ()
    for event in train_schedule:
        if abs((get_location_id_in_line(event, line))- loc_id) <= 0.5:
            counter = counter + (event, )
    return counter 
def get_rogue_schedules_in_line(train_schedule, line, time, loc_id):
    rtime = get_schedules_at_time(train_schedule, time)
    tpl = get_schedules_near_loc_id_in_line(rtime,line,loc_id)
    return tpl


def calculate_blame_in_line(full_schedule, valid_bd_events, line, scorer):
    for event in valid_bd_events:
        t = get_schedule_time(event)
        loc = get_location_id_in_line(event,line)
        rog_sched = get_rogue_schedules_in_line(full_schedule, line, t, loc)
        def last_train(schedule):
            tpl = ()
            for i in schedule:
                train = get_train(i)
                code = get_train_code(train)
                if code not in tpl:
                    tpl += (code,)
            return tpl 
        for x in last_train(rog_sched):
            score = blame_train(scorer, x)
    return scorer

def calculate_blame_in_line(full_schedule, valid_bd_events, line, scorer):
    for event in valid_bd_events:
        t = get_schedule_time(event)
        loc = get_location_id_in_line(event,line)
        rog_sched = get_rogue_schedules_in_line(full_schedule, line, t, loc)
        def last_train(schedule):
            tpl = ()
            for i in schedule:
                train = get_train(i)
                code = get_train_code(train)
                if code not in tpl:
                    tpl += (code,)
            return tpl 
        for x in last_train(rog_sched):
            score = blame_train(scorer, x)
    return scorer



def find_max_score(scorer):
    score = get_blame_scores(scorer)
    x = max(map(lambda x: x[1],score))
    return x
def find_max_score(scorer):
    score = get_blame_scores(scorer)
    x = max(map(lambda x: x[1],score))
    return x

def find_rogue_train(scorer, max_score):
    for i in get_blame_scores(scorer):
        if i[1] == max_score:
            return i[0]def find_rogue_train(scorer, max_score):
    for i in get_blame_scores(scorer):
        if i[1] == max_score:
            return i[0]



