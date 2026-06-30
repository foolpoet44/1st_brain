# Extracted Knowledge from Conv: 074abd86-d3d6-45c6-addf-b0a98d09cb81

**Date**: 2025-08-23T22:58:54.356435Z

### Extracted Code (vba)

```vba
Function GetURL(cell As Range) As String
    If cell.Hyperlinks.Count > 0 Then
        GetURL = cell.Hyperlinks(1).Address
    Else
        GetURL = ""
    End If
End Function
```

### Extracted Code (vba)

```vba
Sub ExtractURLs()
    Dim cell As Range
    For Each cell In Selection
        If cell.Hyperlinks.Count > 0 Then
            cell.Offset(0, 1).Value = cell.Hyperlinks(1).Address
        End If
    Next cell
End Sub
```
