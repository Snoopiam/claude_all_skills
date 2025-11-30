#!/usr/bin/env python3
"""
CSS/UI-UX Analyzer Script
Scans CSS files for common issues and generates audit reports.
"""

import re
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Tuple
from collections import defaultdict


@dataclass
class Issue:
    severity: str  # critical, major, minor
    category: str
    message: str
    line: int
    code: str
    suggestion: str = ""


@dataclass
class FileReport:
    filepath: str
    issues: List[Issue] = field(default_factory=list)
    stats: Dict = field(default_factory=dict)


class CSSAnalyzer:
    """Analyzes CSS files for common issues."""
    
    # Patterns for issue detection
    PATTERNS = {
        # Critical
        'outline_none': (r'outline\s*:\s*none', 'critical', 'accessibility',
            'Removes focus indicator without replacement',
            'Add alternative focus styling or use :focus-visible'),
        'important_abuse': (r'!important', 'major', 'specificity',
            '!important found - may indicate specificity issues',
            'Fix selector specificity instead of using !important'),
        
        # Major
        'hardcoded_color': (r'(?<!var\()#[0-9a-fA-F]{3,8}(?!\))', 'major', 'design-tokens',
            'Hardcoded color value',
            'Use CSS variable: var(--color-name)'),
        'hardcoded_px': (r':\s*\d{2,}px', 'minor', 'design-tokens',
            'Hardcoded pixel value (consider variable)',
            'Use spacing variable: var(--spacing-*)'),
        'id_selector': (r'#[a-zA-Z][\w-]*\s*\{', 'major', 'specificity',
            'ID selector used for styling',
            'Use class selector instead'),
        'deep_nesting': (r'(\s+&|\s+\.|\s+>){4,}', 'major', 'complexity',
            'Deeply nested selector (4+ levels)',
            'Flatten selector structure'),
            
        # Minor
        'empty_rule': (r'\{\s*\}', 'minor', 'cleanup',
            'Empty rule set',
            'Remove empty rule or add styles'),
        'duplicate_property': (r'(\b\w+\b)\s*:[^;]+;\s*\1\s*:', 'minor', 'cleanup',
            'Duplicate property in same rule',
            'Remove duplicate, keep intended value'),
        'z_index_high': (r'z-index\s*:\s*[5-9]\d{2,}', 'major', 'layout',
            'Very high z-index value',
            'Use z-index scale: 10, 20, 30, 40, 50'),
        'commented_code': (r'/\*[\s\S]*?(color|margin|padding|display)[\s\S]*?\*/', 'minor', 'cleanup',
            'Commented-out CSS code',
            'Remove if not needed'),
    }
    
    # Checks for missing interactive states
    INTERACTIVE_ELEMENTS = ['button', 'a', 'input', 'select', 'textarea', '.btn', '.link']
    REQUIRED_STATES = [':hover', ':focus', ':active', ':disabled']
    
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.content = ""
        self.lines = []
        self.issues: List[Issue] = []
        self.stats = defaultdict(int)
        
    def load(self) -> bool:
        """Load CSS file content."""
        try:
            self.content = self.filepath.read_text(encoding='utf-8')
            self.lines = self.content.split('\n')
            return True
        except Exception as e:
            print(f"Error loading {self.filepath}: {e}")
            return False
    
    def analyze(self) -> FileReport:
        """Run all analysis checks."""
        if not self.load():
            return FileReport(str(self.filepath))
        
        self._check_patterns()
        self._check_missing_states()
        self._check_selector_specificity()
        self._calculate_stats()
        
        return FileReport(
            filepath=str(self.filepath),
            issues=self.issues,
            stats=dict(self.stats)
        )
    
    def _check_patterns(self):
        """Check for regex pattern matches."""
        for name, (pattern, severity, category, message, suggestion) in self.PATTERNS.items():
            for i, line in enumerate(self.lines, 1):
                if re.search(pattern, line, re.IGNORECASE):
                    self.issues.append(Issue(
                        severity=severity,
                        category=category,
                        message=message,
                        line=i,
                        code=line.strip()[:80],
                        suggestion=suggestion
                    ))
    
    def _check_missing_states(self):
        """Check for missing interactive states."""
        # Find selectors for interactive elements
        for element in self.INTERACTIVE_ELEMENTS:
            # Check if element has base styles
            base_pattern = rf'{re.escape(element)}\s*\{{'
            if re.search(base_pattern, self.content, re.IGNORECASE):
                # Check for each required state
                for state in [':hover', ':focus']:
                    state_pattern = rf'{re.escape(element)}{re.escape(state)}'
                    if not re.search(state_pattern, self.content, re.IGNORECASE):
                        self.issues.append(Issue(
                            severity='major',
                            category='accessibility',
                            message=f'Missing {state} state for {element}',
                            line=0,
                            code=f'{element}',
                            suggestion=f'Add {element}{state} {{ ... }}'
                        ))
    
    def _check_selector_specificity(self):
        """Check for overly specific selectors."""
        selector_pattern = r'([^{]+)\{'
        for match in re.finditer(selector_pattern, self.content):
            selector = match.group(1).strip()
            # Count specificity indicators
            parts = len(re.findall(r'[\s>+~]', selector))
            if parts >= 4:
                line_num = self.content[:match.start()].count('\n') + 1
                self.issues.append(Issue(
                    severity='major',
                    category='specificity',
                    message=f'Overly specific selector ({parts+1} levels)',
                    line=line_num,
                    code=selector[:60],
                    suggestion='Simplify selector, use BEM naming'
                ))
    
    def _calculate_stats(self):
        """Calculate file statistics."""
        self.stats['lines'] = len(self.lines)
        self.stats['rules'] = len(re.findall(r'\{[^}]+\}', self.content))
        self.stats['variables'] = len(re.findall(r'var\(--[\w-]+\)', self.content))
        self.stats['important'] = len(re.findall(r'!important', self.content))
        self.stats['media_queries'] = len(re.findall(r'@media', self.content))
        
        # Issue counts by severity
        for issue in self.issues:
            self.stats[f'{issue.severity}_count'] = self.stats.get(f'{issue.severity}_count', 0) + 1


def generate_report(reports: List[FileReport], output_path: str = "CSS_AUDIT_REPORT.md"):
    """Generate markdown audit report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Aggregate stats
    total_files = len(reports)
    total_critical = sum(r.stats.get('critical_count', 0) for r in reports)
    total_major = sum(r.stats.get('major_count', 0) for r in reports)
    total_minor = sum(r.stats.get('minor_count', 0) for r in reports)
    
    md = f"""# CSS/UI-UX Audit Report
Generated: {timestamp}

## Summary

| Metric | Count |
|--------|-------|
| Files Analyzed | {total_files} |
| Critical Issues | {total_critical} |
| Major Issues | {total_major} |
| Minor Issues | {total_minor} |
| **Total Issues** | **{total_critical + total_major + total_minor}** |

---

## Files Reviewed

"""
    
    for report in reports:
        if not report.issues:
            md += f"### ✅ {report.filepath}\nNo issues found.\n\n"
            continue
            
        md += f"### ⚠️ {report.filepath}\n\n"
        md += f"**Stats:** {report.stats.get('lines', 0)} lines, {report.stats.get('rules', 0)} rules, "
        md += f"{report.stats.get('variables', 0)} variables used\n\n"
        
        md += "| # | Severity | Category | Issue | Line |\n"
        md += "|---|----------|----------|-------|------|\n"
        
        for i, issue in enumerate(report.issues, 1):
            severity_icon = {'critical': '🔴', 'major': '🟠', 'minor': '🟡'}[issue.severity]
            md += f"| {i} | {severity_icon} {issue.severity.title()} | {issue.category} | {issue.message} | {issue.line} |\n"
        
        md += "\n**Suggestions:**\n"
        seen = set()
        for issue in report.issues:
            if issue.suggestion and issue.suggestion not in seen:
                md += f"- {issue.suggestion}\n"
                seen.add(issue.suggestion)
        md += "\n---\n\n"
    
    md += """## Recommended Next Steps

1. **Address Critical Issues First** - Focus on accessibility and layout-breaking bugs
2. **Implement Design Tokens** - Create CSS variables for colors, spacing, typography
3. **Simplify Selectors** - Reduce specificity, adopt BEM or similar convention
4. **Add Missing States** - Ensure all interactive elements have hover/focus/active states
5. **Clean Up** - Remove commented code, empty rules, and duplicates

## Design Token Template

See `references/audit-checklist.md` for recommended CSS variable structure.
"""
    
    Path(output_path).write_text(md)
    print(f"Report saved to: {output_path}")
    return md


def main():
    parser = argparse.ArgumentParser(description='CSS/UI-UX Analyzer')
    parser.add_argument('path', nargs='?', help='CSS file or directory to analyze')
    parser.add_argument('--dir', '-d', help='Directory to scan for CSS files')
    parser.add_argument('--report', '-r', action='store_true', help='Generate markdown report')
    parser.add_argument('--report-only', action='store_true', help='Generate report without fixes')
    parser.add_argument('--json', '-j', action='store_true', help='Output JSON format')
    parser.add_argument('--output', '-o', default='CSS_AUDIT_REPORT.md', help='Report output path')
    
    args = parser.parse_args()
    
    # Determine files to analyze
    files = []
    scan_path = args.dir or args.path or '.'
    
    if Path(scan_path).is_file():
        files = [scan_path]
    else:
        extensions = ['*.css', '*.scss', '*.sass', '*.less']
        for ext in extensions:
            files.extend(Path(scan_path).rglob(ext))
        # Filter out node_modules
        files = [f for f in files if 'node_modules' not in str(f)]
    
    if not files:
        print(f"No CSS files found in {scan_path}")
        sys.exit(1)
    
    print(f"Analyzing {len(files)} file(s)...")
    
    # Analyze each file
    reports = []
    for filepath in files:
        analyzer = CSSAnalyzer(str(filepath))
        report = analyzer.analyze()
        reports.append(report)
        
        # Print summary for each file
        issue_count = len(report.issues)
        if issue_count > 0:
            critical = report.stats.get('critical_count', 0)
            major = report.stats.get('major_count', 0)
            minor = report.stats.get('minor_count', 0)
            print(f"  {filepath}: {critical} critical, {major} major, {minor} minor")
        else:
            print(f"  {filepath}: ✓ No issues")
    
    # Output
    if args.json:
        output = [{
            'file': r.filepath,
            'issues': [vars(i) for i in r.issues],
            'stats': r.stats
        } for r in reports]
        print(json.dumps(output, indent=2))
    elif args.report or args.report_only:
        generate_report(reports, args.output)
    
    # Summary
    total_issues = sum(len(r.issues) for r in reports)
    print(f"\nTotal: {total_issues} issues found across {len(reports)} files")


if __name__ == '__main__':
    main()
