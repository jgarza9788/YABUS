# this will be used by python to speed up getting the file list from storage

param (
    [string]$Path
    # ,
    # [string]$excludePattern 
)

# Write-Host $excludePattern 
# # $excludePattern = "(\.git|__pycache__)"
# $excludePattern = [regex]::Escape($excludePattern)
# Write-Host $excludePattern 

# Write-Host $Path
# Write-Host $excludePattern 

# $Host.UI.RawUI.BufferSize = New-Object Management.Automation.Host.Size(2400, 2400)


Get-ChildItem -Path $Path -s -File 
# | Where-Object { 
#     $_.FullName -notmatch $excludePattern
# }
| Where-Object { 
    $_.FullName -notmatch "\.archive"
}
| ForEach-Object { 
    '{' + 
    '"relpath":' + '"' + $_.FullName.Replace($Path+'\',"") + '"' + ',' + 
    '"fullpath":' +  '"' + $_.FullName + '"' + ',' + 
    '"filename":' +  '"' + $_.Name + '"' + ',' + 
    '"size":' + $_.Length + ',' + 
    '"modified":' + [System.Math]::Round(($_.LastWriteTimeUtc - [System.DateTime]::Parse("1970-01-01 00:00:00")).TotalSeconds) + ',' + 
    '"rootpath":' +  '"' + $Path + '"' + ',' + 
    '},'
}  
# | Out-File -FilePath "files.txt" -Encoding UTF8
# Get-ChildItem -Path $Path -s -File | Where-Object { $_.FullName -notmatch $excludePattern  } | Format-Table -Property FullName, Length, LastWriteTime

