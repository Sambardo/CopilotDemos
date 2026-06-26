"SessionStart hook ran at $(Get-Date)" | Add-Content ".github/hooks/session-start.log"

$message = @{
    systemMessage = "Workshop hook loaded from .github/hooks/scripts/session-start-message.ps1. This message came from a SessionStart hook."
}

$message | ConvertTo-Json -Compress