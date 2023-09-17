$currentUserName = $env:username
$hostname = $env:COMPUTERNAME
$psVersion =$PSVersionTable.PSVersion
$CurremtDateTime = Get-Date
$IP = getIP atusg
$body =“This machine’s IP is $IP. User is $currentUserName. The hostname is $hostname. Powershell version is $psVersion. Today's date and time is $CurremtDateTime. "
Write-Host $body

$body | Out-file c:\lab03.txt