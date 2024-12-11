# Define the virtual environment directory
$venvDir = "venv"

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Output "Python is not installed or not in PATH. Please install it first."
    exit 1
}

# Create the virtual environment
Write-Output "Creating virtual environment..."
python -m venv $venvDir