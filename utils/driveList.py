
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

if __name__ == '__main__':

    print(*get_drives(),sep='\n')