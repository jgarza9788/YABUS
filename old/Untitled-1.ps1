$Path = "C:\Users\JGarza\Github\YABUS"
$excludePattern = ".*\.csv"  # Example exclusion pattern

# Get files in the specified path and apply the exclusion filter
$files = Get-ChildItem -Path $Path -File | Where-Object {
    # $exclude = $_.FullName -match $excludePattern
    # if ($exclude) {
    #     # Write-Host "Excluded: $($_.FullName)"
    # }
    # return !$exclude

    $_.FullName -notmatch $excludePattern
}

# Display the list of files
$files | ForEach-Object { Write-Host $_.FullName }
