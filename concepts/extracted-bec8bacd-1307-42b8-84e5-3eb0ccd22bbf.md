# Extracted Knowledge from Conv: bec8bacd-1307-42b8-84e5-3eb0ccd22bbf

**Date**: 2026-03-18T00:16:46.156365Z

### Extracted Code (vb)

```vb
Sub SendAllEML()
    Dim folderPath As String
    Dim fileName As String
    Dim olApp As Object
    Dim olMail As Object
    
    folderPath = "C:\Users\YourName\Downloads\eml_output\" ' ← 압축 해제 경로로 수정
    fileName = Dir(folderPath & "*.eml")
    
    Set olApp = CreateObject("Outlook.Application")
    
    Do While fileName <> ""
        Set olMail = olApp.CreateItemFromTemplate(folderPath & fileName)
        olMail.Send
        fileName = Dir()
    Loop
    
    MsgBox "발송 완료!"
End Sub
```

### Extracted Code (text)

```text
[고정 - 회색]                    [입력 - 노란색]
년도 | Project Code | 과제명 | 총액  |  1)수주장비  |  2)PM여부  |  3)수행인원  |  4)투입시점  |  5)종결시점
                                      분류         (Y/N)      (N일때만)
```
