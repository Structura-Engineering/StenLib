$prefix = "(Setup):"

Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "Running setup_python.ps1..." -ForegroundColor Cyan
.\scripts\setup_python.ps1 -prefix $prefix
if ($LASTEXITCODE -ne 0) {
    Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "An error occurred during Python setup." -ForegroundColor Red
    exit
}

Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "Running setup_venv.ps1..." -ForegroundColor Cyan
.\scripts\setup_venv.ps1 -prefix $prefix
if ($LASTEXITCODE -ne 0) {
    Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "An error occurred during virtual environment setup." -ForegroundColor Red
    exit
}

Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "Running setup_pip_packages.ps1..." -ForegroundColor Cyan
.\scripts\setup_pip_packages.ps1 -prefix $prefix
if ($LASTEXITCODE -ne 0) {
    Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "An error occurred during pip package setup." -ForegroundColor Red
    exit
}

Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "Running setup_pytests.ps1..." -ForegroundColor Cyan
.\scripts\setup_pytests.ps1 -prefix $prefix
if ($LASTEXITCODE -ne 0) {
    Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "An error occurred during test setup." -ForegroundColor Red
    exit
}

Write-Host -NoNewline "$prefix " -ForegroundColor Red; Write-Host "Setup complete!" -ForegroundColor Green
Pause
Clear-Host
