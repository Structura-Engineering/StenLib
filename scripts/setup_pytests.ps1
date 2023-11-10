param (
    [string]$prefix
)

try {
    $pyFiles = Get-ChildItem -Path .\StenLib\ -Filter *.py -Recurse
    foreach ($file in $pyFiles) {
        $relativePath = $file.FullName.Substring((Resolve-Path .\StenLib\\).Path.Length)
        $relativeDir = (Split-Path -Path $relativePath -Parent).Replace('\', '.')
        $baseName = $file.BaseName

        if ($baseName -notmatch "__") {
            $testDirPath = ".\tests\" + (Split-Path -Path $relativePath -Parent)
            $testDir = New-Item -Path $testDirPath -ItemType Directory -Force
            $testFile = New-Item -Path "$testDir\$baseName`_test.py" -ItemType File -Force
            $importPath = if ($relativeDir) { "StenLib.$relativeDir.$baseName" } else { "StenLib.$baseName" }
            $testCode = @"
import pytest
from $importPath import *

def test_sample():
    assert True
"@            
            Add-Content -Path $testFile.FullName -Value $testCode
            Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "Test file $relativeDir\$baseName`_test.py created successfully."
        }
    }
}
catch {
    Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "An error occurred while creating test files." -ForegroundColor Red;
}
