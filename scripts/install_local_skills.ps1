param(
    [string]$CodexSkillsDir = "$env:USERPROFILE\.codex\skills",
    [string]$SourceSkillsDir = (Join-Path $PSScriptRoot "..\skills")
)

$ErrorActionPreference = "Stop"

$sourceRoot = (Resolve-Path -LiteralPath $SourceSkillsDir).Path
$destRoot = $CodexSkillsDir
New-Item -ItemType Directory -Force -Path $destRoot | Out-Null
$destRoot = (Resolve-Path -LiteralPath $destRoot).Path

if ([string]::IsNullOrWhiteSpace($sourceRoot) -or [string]::IsNullOrWhiteSpace($destRoot)) {
    throw "SourceSkillsDir and CodexSkillsDir must resolve to non-empty paths."
}

$sourceSkills = Get-ChildItem -LiteralPath $sourceRoot -Directory -Filter "coff0xc-*"
if ($sourceSkills.Count -eq 0) {
    throw "No coff0xc-* skill directories found under $sourceRoot"
}

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$backupRoot = Join-Path (Split-Path -Parent $destRoot) "skills-backup-coff0xc-$stamp"
New-Item -ItemType Directory -Force -Path $backupRoot | Out-Null

$installed = @()
foreach ($skill in $sourceSkills) {
    $target = Join-Path $destRoot $skill.Name
    if (Test-Path -LiteralPath $target) {
        Move-Item -LiteralPath $target -Destination (Join-Path $backupRoot $skill.Name)
    }
    Copy-Item -LiteralPath $skill.FullName -Destination $destRoot -Recurse
    $installed += $skill.Name
}

$result = [ordered]@{
    source = $sourceRoot
    destination = $destRoot
    backup = $backupRoot
    installed_count = $installed.Count
    installed = $installed
}

$result | ConvertTo-Json -Depth 4
