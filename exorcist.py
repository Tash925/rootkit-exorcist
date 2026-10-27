import argparse
from pathlib import Path

from detectors import scan_script
from ai_priest import summon_priest


def main():
    parser = argparse.ArgumentParser(
        description="The Rootkit Exorcist: Static script analyzer"
    )

    parser.add_argument(
        "file",
        help="Script to investigate"
    )

    parser.add_argument(
        "--mode",
        choices=["soc", "exorcist"],
        default="exorcist",
        help="Choose professional SOC or theatrical Exorcist reporting"
    )

    parser.add_argument(
    "--output",
    help="Save the analysis as a Markdown report"
    )

    args = parser.parse_args()
    path = Path(args.file)

    if not path.is_file():
        parser.error("The specified file does not exist.")

    if path.stat().st_size > 1024 * 1024:
        parser.error("File exceeds the 1 MB analysis limit.")

    content = path.read_text(
        encoding="utf-8",
        errors="replace"
    )

    findings = scan_script(content)

    if args.mode == "soc":
        print("\nROOTKIT EXORCIST | SOC ANALYSIS")
        print("Static script analysis report\n")
    else:
        print("\n✝ THE ROOTKIT EXORCIST ✝")
        print("The terminal is blessed. The scripts are not.\n")

    if not findings:
        print("No suspicious patterns detected by current rules.")
        print("This does NOT guarantee the script is safe.")
        return

    print(f"I sense {len(findings)} suspicious indicator(s)!\n")

    for finding in findings:
        print(f"[{finding['severity']}] {finding['name']}")
        print(f"  Line: {finding['line']}")
        print(f"  MITRE ATT&CK: {finding['technique']}")
        print(f"  Evidence: {finding['evidence']}")
        print(f"  Meaning: {finding['description']}\n")

    if args.mode == "exorcist":
        print("✝ THE POWER OF CHMOD COMPELS YOU! ✝")

    print("Verdict: Manual investigation required.")

    print("\n" + "=" * 45)

    if args.mode == "soc":
        print("AI-ASSISTED INVESTIGATION NOTES")
    else:
        print("✝ THE AI PRIEST SPEAKS ✝")

    print("=" * 45)

    explanation = summon_priest(findings, mode=args.mode)
    print(explanation)
   
    if args.output:
        report = [
            "# The Rootkit Exorcist — Analysis Report",
            "",
            f"**Analyzed file:** `{path.name}`",
            "",
            f"**Reporting mode:** {args.mode.upper()}",
            "",
            "## Static Detection Findings",
            "",
            "**Verdict:** Manual investigation required.",
            "",
        ]

        for finding in findings:
            report.extend([
                f"### {finding['name']}",
                "",
                f"- **Severity:** {finding['severity']}",
                f"- **Line:** {finding['line']}",
                f"- **MITRE ATT&CK:** {finding['technique']}",
                f"- **Evidence:** `{finding['evidence']}`",
                f"- **Description:** {finding['description']}",
                "",
            ])

        report.extend([
            "## AI-Generated Investigation Notes",
            "",
            "> AI-generated content is supplementary and may be inaccurate.",
            "",
            "```text",
            explanation.replace("```", "'''"),
            "```",
            "",
            "## Limitations",
            "",
            "- Findings are heuristic indicators, not proof of malware.",
            "- No script execution or automatic remediation was performed.",
            "",
        ])

        output_path = Path(args.output)
        output_path.write_text(
            "\n".join(report),
            encoding="utf-8"
        )

        print(f"\nMarkdown report saved to: {output_path}")

if __name__ == "__main__":
    main()
