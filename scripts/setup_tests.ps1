param (
    [string]$prefix
)

try {
    $pyFiles = Get-ChildItem -Path .\StenLib\ -Filter *.py
    foreach ($file in $pyFiles) {
        $baseName = $file.BaseName
        if ($baseName -notmatch "__") {
            $testFile = New-Item -Path ".\tests\$baseName`_test.py" -ItemType File -Force
            $testCode = python -c "import sys; sys.path.insert(0, './template'); import test_template; print(test_template.get_test_code('$baseName'))"
            Add-Content -Path $testFile.FullName -Value $testCode
            Write-Host -NoNewline "$prefix " -ForegroundColor Green; Write-Host "Test file $baseName`_test.py created successfully."
        }
    }
} catch {
    Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "An error occurred while creating test files."
}
