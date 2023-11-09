param (
    [string]$prefix
)

try {
    $pyFiles = Get-ChildItem -Path .\StenLib\ -Filter *.py
    foreach ($file in $pyFiles) {
        $baseName = $file.BaseName
        if ($baseName -notmatch "__") {
            $testFile = New-Item -Path ".\tests\$baseName`_test.py" -ItemType File -Force
            $testCode = @"
import pytest
from StenLib.$baseName import *

def test_sample():
    assert True
"@            
            Add-Content -Path $testFile.FullName -Value $testCode
            Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "Test file $baseName`_test.py created successfully."
        }
    }
} catch {
    Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "An error occurred while creating test files." -ForegroundColor Red;
}
