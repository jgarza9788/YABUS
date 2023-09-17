import re
import subprocess as sp

def get_drives():
    # logging.info('getting list of all drives')
    command = "wmic logicaldisk get deviceid, volumename" 
    pipe = sp.Popen(command,shell=True,stdout=sp.PIPE,stderr=sp.PIPE)    

    # result = ''
    result = []
    for line in pipe.stdout.readlines():
        # print(line)
        line = str(line)
        if 'DeviceID' in line:
            continue
        if 'b\'\\r\\r\\n\'' == line:
            continue
        temp = line.replace('b\'','') 
        temp = temp.replace('\\r\\r\\n\'','')
        temp = temp.split(' ',1)

        t2 = {}
        for index,t in enumerate(temp):
            if index == 0:
                t2['letter'] = t.strip()
            else:
                t2['label'] = t.strip()
        result.append(t2)
        
        # print(temp)
        # logging.info(f'found drive: {temp}')
    
    return result 


def get_drivedata_details():
    # logging.info('getting list of all drives')
    command = "wmic logicaldisk get caption, volumename, size, freespace" 
    pipe = sp.Popen(command,shell=True,stdout=sp.PIPE,stderr=sp.PIPE)    

    # result = ''
    result = []
    for line in pipe.stdout.readlines()[1::]:
        line = str(line)
        # print(line)
        line = re.sub(r"(b\'|\\r|\\n|\')", '', line)
        line = re.sub(r"\s+",' ', line)
        line = line.replace('Google Drive','Google_Drive')
        # line = line.replace('\\r\\r\\n\'','')
        # print(line)

        item = {}
        for index,t in enumerate(line.split(' ')):
            # print(t)
            if t == '':
                # print('empty')
                continue
            if index == 0:
                item['letter'] = t.strip()
            elif index == 1:
                item['freespace'] = int(t.strip()) / 1024 / 1024 / 1024
            elif index == 2:
                item['size'] = int(t.strip()) / 1024 / 1024 / 1024
            elif index == 3:
                item['volumename'] = t.strip()
        
        if len(item) > 0:
            item['size_round'] = float('{:.2f}'.format(item['size']))
            item['freespace_round'] = float('{:.2f}'.format(item['freespace']))
            item['used_round'] = float('{:.2f}'.format(item['size'] - item['freespace']))
            item['percent_used'] = float('{:.2f}'.format(((item['size'] - item['freespace'])/item['size']) * 100.0))
            item['percent_free'] = float('{:.2f}'.format(100.0 - item['percent_used']))
            result.append(item)
    
    return result 

if __name__ == '__main__':

    print(*get_drives(),sep='\n')