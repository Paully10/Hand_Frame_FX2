' Launch Hand Frame FX with no console window — feels like a normal app.
' Must stay in the same folder as venv\ and handy_eff.py.

Set fso = CreateObject("Scripting.FileSystemObject")
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

pythonExe = scriptDir & "\venv\Scripts\python.exe"
target = scriptDir & "\handy_eff.py"

If Not fso.FileExists(pythonExe) Then
    MsgBox "Couldn't find " & pythonExe & vbCrLf & vbCrLf & _
           "Make sure this file is in the same folder as your 'venv' folder " & _
           "and that you've already run 'pip install -r requirements.txt' once.", _
           vbExclamation, "Hand Frame FX"
    WScript.Quit
End If

Set shell = CreateObject("WScript.Shell")
shell.Run """" & pythonExe & """ """ & target & """", 0, False
