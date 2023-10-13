$Hello = "Hello, PowerShell"
Write-host($Hello)
Function getIP{ 

    (get-netipaddress).ipv4address | Select-String "192*" 

} 
write-host(getIP) gir st
$IP = getIP atusg

Write-Host(“This machine’s IP is $IP”) 

Write-Host(“This machine’s IP is {0}” -f $IP)