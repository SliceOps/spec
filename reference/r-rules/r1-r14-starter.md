# R1–R14 — Canonical Starter Rules (Layer B.1)

Vendor-neutral, stack-agnostic merge gates. Each is a **hard gate**. The check patterns are abstract; adopters bind them to their stack (Layer C.2). Allowlist marker convention: an inline comment `<!-- r<N>-allowlist: <reason ≥10 non-hyphen chars> -->` documents an audited exception.

---

### R1 — No secrets in markdown/YAML
- **Statement**: No API keys, connection strings, passwords, tokens, OAuth credentials, private keys, or credential-bearing URLs in `.md`/`.yaml`/frontmatter.
- **Principle**: P6 (Security-by-Construction).
- **Check**: scan for `password|secret|apikey|bearer <token>|-----BEGIN .*PRIVATE KEY-----` and `scheme://user:pass@host`.
- **Allowlist**: explicit placeholder examples with `<!-- r1-allowlist: <reason> -->`.

### R2 — No broken cross-references
- **Statement**: Every internal link and every cross-reference (DEC id, spec path, slice id, source provenance id) must resolve.
- **Principle**: P2, P10.
- **Check**: resolve every markdown link and every typed frontmatter reference against the repo.

### R3 — Frontmatter required and valid
- **Statement**: Every non-archive entity doc has valid frontmatter: the canonical `entity:` key (per the entity catalog), lifecycle `status`, dates, `owner`, `sensitivity`, plus Layer 1 consistency fields where the entity is a DecisionRecord.
- **Principle**: P2, P4, P10.
- **Check**: YAML schema validation against the entity catalog and Layer 1 fields spec.
- **Allowlist**: READMEs / archive snapshots exempt by path convention.

### R4 — Decision registry consistency
- **Statement**: Any inline `DEC <id>` reference must have a corresponding registry entry in the decisions folder. New inline DEC without a registry entry → BLOCK.
- **Principle**: P2, P4.
- **Check**: every referenced DEC id exists as an accepted/superseded/deprecated file.

### R5 — Lifecycle transitions atomic
- **Statement**: When a DEC moves accepted → superseded/deprecated, the same PR must: move the file, update `status`, set `superseded-by`/`replacement`, ensure the superseding DEC carries `supersedes`, and update any deprecation schedule.
- **Principle**: P2, P4.
- **Check**: lifecycle move and bidirectional edges present in one atomic change.

### R6 — No TODO/FIXME/HACK in frozen DECs/specs
- **Statement**: Ratified DECs and frozen (released) spec versions contain no `TODO|FIXME|HACK|XXX:` markers. Drafts/RFCs may.
- **Principle**: P5 (Evidence-by-Construction — frozen means complete).
- **Allowlist**: `<!-- r6-allowlist: <issue-link> -->`.

### R7 — External-source provenance preserved
- **Statement**: Any doc migrated from an external source must retain its source-provenance metadata in frontmatter; later refactors must not drop it (audit trail external → repo).
- **Principle**: P2, P4.
- **Check**: provenance field present and immutable for docs flagged as migrated. *(Generalizes the reference implementation's migration-provenance rule; the specific external source is adopter-defined.)*

### R8 — SemVer discipline and version coherence
- **Statement**: Versioned spec/plan directories follow SemVer 2.0.0. Coherence: paired plan/spec majors and minors move in lockstep; patch independent. Breaking change → new major directory, not edit-in-place of a frozen version.
- **Principle**: P2, P10.
- **Check**: SemVer validity and paired-artifact lockstep on any PR touching versioned dirs.

### R9 — Cross-repo agent-context sync
- **Statement**: When a doc that defines source-of-truth hierarchy (or how code repos interpret canon) changes, the PR includes a checklist of cross-repo sub-PRs to each affected agent-context file (the per-repo agent instructions file, whatever the platform names it — P8: not tied to one tool's filename).
- **Principle**: P8, P10.
- **Check**: source-of-truth doc touched → cross-repo sync checklist present.

### R10 — Archive immutability
- **Statement**: Archived files are immutable. PRs modifying archived content (except adding new files) → BLOCK. To "correct" an archived item, add a new timestamped file citing the original.
- **Principle**: P2 (audit trail integrity).
- **Check**: no removed/changed lines under the archive path in the diff.

### R11 — Confidentiality classification
- **Statement**: Every doc requiring frontmatter declares `sensitivity` from the canonical set. Classifications inappropriate to the repo's declared audience are prohibited (the prohibited set is adopter-defined per the repo's audience policy).
- **Principle**: P6, P9.
- **Check**: `sensitivity` present and within the repo's allowed set; body content consistent with the classification.

### R12 — Import scope policy
- **Statement**: Imports into the repo are restricted to an authorized source tree. Frontmatter referencing an out-of-scope or exclusion-listed source → BLOCK.
- **Principle**: P2, P6.
- **Check**: every migrated doc's source id is within the authorized tree. *(Generalizes the reference implementation's import-scope rule; the authorized tree is adopter-defined.)*

### R13 — Slice ledger update mandatory
- **Statement**: Every PR that closes a slice updates the slice-tracker and cost-ledger in the same commit. Exception: a documented skip marker with justification.
- **Principle**: P5, P12 (cost-ledger has token and infra/CI dimensions).
- **Check**: slice-closing PR diff modifies both ledgers, or carries `[skip-ledger-update]` and rationale.

### R14 — Scope boundary enforcement
- **Statement**: No PR adds content outside the repo's declared scope. Out-of-scope content lives in the appropriate domain's own brain. The specific out-of-scope categories are adopter-declared (e.g., a technical spec repo rejects commercial/HR/strategic content).
- **Principle**: P2, P10.
- **Check**: scope-boundary scan with adopter-defined category patterns; allowlist marker `<!-- r14-allowlist: <reason ≥10 non-hyphen chars> -->` for legitimate matches (glossary/archive/opaque cross-refs).

---

## Mapping to principles (retirement test)

Every rule traces to ≥1 principle (P2/P4/P5/P6/P8/P9/P10/P12 above). An R-rule that cannot be traced to a principle is a candidate for retirement (per P7 — the rule set itself is subject to recursive learning).

## Amendment

R-rule additions/changes require a DEC citing a LearningPattern as evidence (P7 and P9). Adopter-specific rules start at R15 and are Layer C.2 (the adopter's stack instantiation), not part of this canonical starter pack.
