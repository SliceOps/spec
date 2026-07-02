# SPDX-License-Identifier: MIT
"""Build-Complexity Profile + Build Velocity — reference measurement (Layer B.1).

Read-only. Computes the git-derived substrate (velocity with commit hygiene, LOC,
decisions, dates, and the Code axis via a pluggable CCN tool) and emits the result
skeleton. The five judgment axes (state, concurrency, integrations, trust,
intelligence) are NOT auto-derivable — they are scored by hand from the rubric in
README.md against repo evidence, and left null here on purpose.

Usage:
    python3 measure.py [repo ...] [--ccn-cmd lizard]
Defaults to the current directory; discovers nested git repos (maxdepth 4).
"""
import json
import os
import re
import subprocess
import sys

MAXGAP = 120 * 60      # gap (s) that starts a new session — calibratable default
FIRST = 45 * 60        # credited per session for pre-first-commit work — calibratable
BOT_RE = re.compile(r"auto.?sync|dependabot|renovate|\[bot\]|\bbot\b", re.I)
SRC_RE = re.compile(r"\.(ts|tsx|js|jsx|py|go|rs|java|kt|cs|dart|rb|php|sol|sql)$")
GEN_RE = re.compile(r"(^|/)(node_modules|dist|build|vendor)/|"
                    r"(\.Designer\.cs|ModelSnapshot\.cs|\.g\.dart|\.freezed\.dart)$")


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True,
                          text=True).stdout


def discover(root):
    out = []
    for dirpath, dirs, _ in os.walk(root):
        if dirpath.count(os.sep) - root.count(os.sep) > 4:
            dirs[:] = []
            continue
        if ".git" in dirs:
            out.append(dirpath)
            dirs.remove(".git")
    return out or [root]


def velocity(repo):
    """Cluster commit timestamps into sessions, excluding merge/automated commits."""
    raw = git(repo, "log", "--no-merges", "--format=%at\t%an\t%s").splitlines()
    ts = sorted(int(l.split("\t", 1)[0]) for l in raw
                if l and not BOT_RE.search(l.split("\t", 1)[1] if "\t" in l else ""))
    if not ts:
        return 0.0, 0
    total, sessions = FIRST, 1
    for i in range(1, len(ts)):
        gap = ts[i] - ts[i - 1]
        total += gap if gap <= MAXGAP else FIRST
        sessions += 0 if gap <= MAXGAP else 1
    return round(total / 3600, 1), sessions


def loc(repo):
    files = [f for f in git(repo, "ls-files").splitlines()
             if SRC_RE.search(f) and not GEN_RE.search(f)]
    n = 0
    for f in files:
        p = os.path.join(repo, f)
        try:
            with open(p, "rb") as fh:
                n += sum(1 for _ in fh)
        except OSError:
            pass
    return n


def decisions(repo):
    out = git(repo, "ls-files").splitlines()
    return sum(1 for f in out
               if re.match(r"(^|.*/)(DEC|DR)-.*\.md$", f) and "node_modules" not in f)


def code_axis(repo):
    """Code axis via lizard (one reference CCN tool; the metric is canonical, not it)."""
    try:
        import lizard
    except ImportError:
        return {"ccn_avg": None, "pct_over_10": None, "nloc": None, "score": None,
                "note": "no CCN tool available — score Code by manual read (README §3)"}
    src = [os.path.join(repo, d) for d in ("src", "app", "lib", "functions", "pkg",
                                           "internal", "cmd") if os.path.isdir(os.path.join(repo, d))]
    src = src or [repo]
    ccns, nloc = [], 0
    for fi in lizard.analyze(src):
        nloc += fi.nloc
        ccns += [fn.cyclomatic_complexity for fn in fi.function_list]
    if not ccns:
        return {"ccn_avg": 0.0, "pct_over_10": 0.0, "nloc": nloc, "score": 0}
    avg = round(sum(ccns) / len(ccns), 1)
    pct = round(100 * sum(1 for c in ccns if c > 10) / len(ccns), 1)
    if avg < 3 and pct < 5:
        score = 1
    elif avg <= 5 or pct <= 15:
        score = 2
    elif avg <= 8 or pct <= 30:
        score = 3
    else:
        score = 4
    return {"ccn_avg": avg, "pct_over_10": pct, "nloc": nloc, "score": score,
            "note": "lizard undercounts JSX/TSX/Dart — verify by manual read where dominant"}


def measure(repo):
    first = (git(repo, "log", "--reverse", "--format=%ad", "--date=short")
             .splitlines() or [""])[0]
    last = git(repo, "log", "-1", "--format=%ad", "--date=short").strip()
    commits = git(repo, "rev-list", "--count", "HEAD").strip()
    tag = git(repo, "tag", "--sort=creatordate",
              "--format=%(creatordate:short) %(refname:short)").splitlines()
    hours, sessions = velocity(repo)
    code = code_axis(repo)
    return {
        "name": os.path.basename(os.path.abspath(repo)),
        "first_commit": first, "last_commit": last,
        "launch": (tag[0].split()[0] if tag else None),
        "commits": int(commits or 0), "sessions": sessions,
        "commit_active_hours": hours, "loc": loc(repo), "decisions": decisions(repo),
        "complexity": {"state": None, "concurrency": None, "integrations": None,
                       "trust": None, "intelligence": None, "code": code["score"]},
        "code_axis": code,
        "axis_note": "state/concurrency/integrations/trust/intelligence: score 0-4 by "
                     "hand from README.md §2 against repo evidence; discard false positives.",
    }


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    roots = args or ["."]
    repos = []
    for r in roots:
        repos += discover(r)
    out = [measure(r) for r in sorted(set(repos))]
    print(json.dumps(out if len(out) > 1 else out[0], indent=2))
