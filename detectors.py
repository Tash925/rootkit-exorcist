
import re

RULES = [
    {
    "id": "EXO-001",
    "name": "Potential Cron Persistence",
    "pattern": (
    r"\bcrontab\s+(?:-[eu]\b|-(?![a-zA-Z]))"
    r"|(?:>>?|tee(?:\s+-a)?)\s*/etc/cron(?:\.[\w-]+)?(?:/[^\s;|]*)?"
  ),
    "technique": "T1053.003",
    "severity": "MEDIUM",
    "description": (
        "Possible installation or modification of a scheduled cron job. "
        "Review the command and surrounding context."
    ),
  },
    {
        "id": "EXO-002",
        "name": "Download and Execute",
        "pattern": r"\b(?:curl|wget)\b[^\n]{0,300}\|\s*(?:bash|sh)\b",
        "technique": "T1105",
        "severity": "HIGH",
        "description": "A remote script may be downloaded and passed to a shell.",
    },
    {
        "id": "EXO-003",
        "name": "PowerShell Encoded Command",
        "pattern": r"\b(?:powershell|pwsh)(?:\.exe)?\b[^\n]{0,300}-(?:enc|encodedcommand)\b",
        "technique": "T1027",
        "severity": "MEDIUM",
        "description": "PowerShell may be running an encoded command.",
    },
]


def scan_script(content):
    findings = []

    for rule in RULES:
        for match in re.finditer(
            rule["pattern"], content, flags=re.IGNORECASE
        ):
            findings.append({
                "id": rule["id"],
                "name": rule["name"],
                "severity": rule["severity"],
                "technique": rule["technique"],
                "description": rule["description"],
                "line": content.count("\n", 0, match.start()) + 1,
                "evidence": match.group(0)[:200],
            })

    return findings
