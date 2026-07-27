param(
    [Parameter(Mandatory=$true)][string]$DocxPath,
    [Parameter(Mandatory=$true)][string]$OutputTxt
)

Add-Type -AssemblyName System.IO.Compression.FileSystem

$zip = [System.IO.Compression.ZipFile]::OpenRead($DocxPath)
try {
    $entry = $zip.Entries | Where-Object { $_.FullName -eq 'word/document.xml' }
    if ($null -eq $entry) { throw "document.xml not found in $DocxPath" }
    $stream = $entry.Open()
    $reader = New-Object System.IO.StreamReader($stream)
    $xml = $reader.ReadToEnd()
    $reader.Close()
    $stream.Close()
} finally {
    $zip.Dispose()
}

# Convert paragraph and break tags to newlines BEFORE stripping markup
$xml = $xml -replace '</w:p>', "`n"
$xml = $xml -replace '<w:br[^/]*/>', "`n"
$xml = $xml -replace '<w:tab[^/]*/>', "`t"

# Strip all remaining XML tags
$text = [regex]::Replace($xml, '<[^>]+>', '')

# Decode common XML entities
$text = $text -replace '&amp;', '&' -replace '&lt;', '<' -replace '&gt;', '>' -replace '&quot;', '"' -replace '&apos;', "'"

# Collapse runs of blank lines
$text = [regex]::Replace($text, "(\r?\n){3,}", "`n`n")

Set-Content -Path $OutputTxt -Value $text -Encoding utf8
Write-Output "Wrote $OutputTxt ($($text.Length) chars)"
