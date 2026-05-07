$ErrorActionPreference = "Stop"

$rubyBin = "C:\Ruby33-x64\bin"
$env:PATH = "$rubyBin;$env:PATH"
$env:BUNDLE_USER_HOME = Join-Path $PSScriptRoot ".bundle-home"
$env:BUNDLE_PATH = Join-Path $PSScriptRoot "vendor\bundle"
$env:BUNDLE_BIN = Join-Path $PSScriptRoot ".bundle\bin"

Set-Location $PSScriptRoot
& "$rubyBin\bundle.bat" exec jekyll serve --host 127.0.0.1 --port 4000 --baseurl= --no-watch
