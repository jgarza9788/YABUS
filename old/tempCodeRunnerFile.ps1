$fullPath = "C:\Users\JGarza\GitHub\YABUS\YABUS.py"

# Get the root path (drive or network share) without the file name
$rootPath = (Get-Item $fullPath).Root.FullName

# Output the root path
Write-Host $rootPath
