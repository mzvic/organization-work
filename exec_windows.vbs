Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "exec_windows_with_cmd.bat" & Chr(34), 0
Set WshShell = Nothing