
from datetime import datetime
from dateutil.relativedelta import relativedelta

def minimize_path(path:str,maxlen:int=35):
    """minimized the path to fit in the UI

    Args:
        path (str): _description_

    Returns:
        _type_: _description_
    """
    if len(path) <= maxlen:
        return path
    else: 
        return path[0:3] + '...\\' + path.split('\\')[-1]

    
def format_lastbackup(lastbackup:str):
    if lastbackup == None:
        return 'None'
    return lastbackup[0:4] + '.' + lastbackup[4:6] + '.' + lastbackup[6:8] + ' | ' + lastbackup[8:10] + ':' + lastbackup[10:12]

def time_difference(lastbackup:str):
    if lastbackup == None:
        return 'None'
    
    lbu = datetime(
        year= int(lastbackup[0:4]),
        month= int(lastbackup[4:6]),
        day=int(lastbackup[6:8]),
        hour=int(lastbackup[8:10]),
        minute=int(lastbackup[10:12]),
    )
    now  = datetime.now()  
    ago = relativedelta(now,lbu)
    years_ago = ago.years
    months_ago = ago.months
    days_ago = ago.days
    hours_ago = ago.hours
    minutes_ago = ago.minutes

    return f'{years_ago} years ago \n{months_ago} months ago \n{days_ago} days ago \n{hours_ago} hours ago \n{minutes_ago} minutes ago'




if __name__ == '__main__':

    print(format_lastbackup('202304011613'))