# powershell is faster for getting a list of files
# but this script only brings back a portion of the files 


import os 
import time
import subprocess as sp
import pandas as pd
import json5 as json

# # cmd = ["pwsh", "-Command", r"Get-ChildItem -Path D:\UnityProjects -File -Recurse -Depth 999 | Where-Object { $_.FullName -notmatch '.*\.bin' } | Select-Object -Property FullName"]
# cmd = ["pwsh", "-Command", r"Get-ChildItem -Path D:\UnityProjects -File -Recurse "]
# cmd = " ".join(cmd)

# cmd = "pwsh .\\utils\\get_files.ps1 . \"(\.git|__pycache__)\"" # ✅
# cmd = "pwsh .\\utils\\get_files.ps1 ~\GitHub\YABUS \"(\.git|__pycache__)\"" # ✅
# cmd = "pwsh .\\utils\\get_files.ps1 D:\\UnityProjects\\ZoomEcho \"(\.git|__pycache__)\"" # ✅
cmd = "pwsh .\\utils\\get_files.ps1 D:\\UnityProjects \"(\.git|__pycache__)\"" #
print(cmd)

pipe = sp.Popen(cmd,shell=True,stdout=sp.PIPE,stderr=sp.PIPE)    


# Wait for the process to complete and capture its output
stdout, stderr = pipe.communicate()

# Check for errors
if pipe.returncode == 0:
    # # Print the command output
    # # print("PowerShell Command Output:")
    # # print(stdout)
    # # print(str(stdout))
    out = str(stdout)[2::]
    out = out.replace('\\r\\n','')
    out = out[:-2]
    out = '[' + out + ']'
    # # print(out[-100::])
    # # out = out.replace('\"','\\"')
    print(out[16600:16620])
    # # print('[' + out + ']')
    print(out[-100::])
    # # print(out[1::])
    out = pd.DataFrame(json.loads( out ))
    print(len(out))
    print(out)
    # print(stdout[:100])

quit()
########################################

result = sp.run(["pwsh",".\\utils\\get_files.ps1", "." ,"(.git|__pycache__)"], capture_output=True, text=True, shell=True)

# result = sp.run(['pwsh .\\utils\\get_files.ps1 . (.git|__pycache__)'], capture_output=True, text=True, shell=True)

if result.returncode != 0:
    print(result.stderr)
    quit()

# print(type(result.stdout))
# print(result.stdout.replace('\n',','))
# out = str(result.stdout)[2::]
# out = out.replace('\\r\\n',',')
# out = out[:-2]
# out = '[' + out + ']'
out = result.stdout.replace('\n','').replace('\\','\\\\')
# out = out[:-1]
# out = '[' + out + ']'
# print(out)
print(out[0:100])
print(out[100::])
# print(out[11580:11590])
# df = pd.DataFrame(json.loads( out ,encoding='utf8'))
# print(len(df))
# print(df)

#     # Print the command output
#     print("PowerShell Command Output:")
#     # print(type(result.stdout))
#     print(result.stdout)
# else:
#     # Print any error messages
#     print("PowerShell Command Error:")
#     # print(type(result.stderr))
#     print(result.stdout)
#     print(result.stderr)

quit()

cmd = "pwsh .\\utils\\get_files.ps1 . \"(\.git|__pycache__)\"" 
print(cmd)

pipe = sp.Popen(cmd,shell=False,stdout=sp.PIPE,stderr=sp.PIPE)    


# Wait for the process to complete and capture its output
stdout, stderr = pipe.communicate()

# Check for errors
if pipe.returncode == 0:
    # Print the command output
    # print("PowerShell Command Output:")
    # print(stdout)
    # print(str(stdout))
    out = str(stdout)[2::]
    out = out.replace('\\r\\n',',')
    out = out[:-2]
    out = '[' + out + ']'
    # print(out[-100::])
    # out = out.replace('\"','\\"')
    # print(out[16600:16700])
    # print('[' + out + ']')
    # print(out[-100::])
    # print(out[1::])
    out = pd.DataFrame(json.loads( out ))
    print(len(out))
    print(out)

    # lines = str(stdout).split('\\r\\n')
    # # print(len(lines))
    # for index,l in enumerate(lines):
    #     if len(l) > 50:
    #         print(index,l)

    # print('*')
    # print(*lines,sep='\n')
    # print('*')
    # print(*lines,sep='\n')
else:
    # Print any error messages
    print("PowerShell Command Error:")
    print(stderr)

# result = sp.run(["pwsh", "-Command", r"Get-ChildItem -Path D:\UnityProjects -File -Recurse -Depth 999 | Where-Object { $_.FullName -notmatch '.*\.bin' } | Select-Object -Property FullName"], capture_output=True, text=True, shell=True)

# time.sleep(10)

# if result.returncode == 0:
#     # Print the command output
#     print("PowerShell Command Output:")
#     # print(type(result.stdout))
#     print(result.stdout)
# else:
#     # Print any error messages
#     print("PowerShell Command Error:")
#     # print(type(result.stderr))
#     print(result.stdout)


# for l in result.stderr.readlines():
#     print(l)

# # | Where-Object { $_.FullName -notmatch \".*\" }
# cmd = r"pwsh -command 'Get-ChildItem -Path D:\UnityProjects -s' "
# pipe = sp.Popen(cmd,shell=True,stdout=sp.PIPE,stderr=sp.PIPE)    

# # print(type(pipe))
# for l in pipe.stdout.readlines():
#     print(l)
# # print(pipe.stdout.readlines())
# # print(*pipe,sep='\n')


