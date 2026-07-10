<!--
OutcomeRecord template (Layer B.1). Naming: OUTC-<id>-<slug>.md
(id = NNN counter-based repos, YYYY-MM-DD vaults — spec/v1.2.0/naming.md).
kind: is mandatory — retrospective (Block Retrospective) | postmortem | result.
A closed OutcomeRecord is immutable; corrections append a new record. Replace all <…>.
-->
---
entity: OutcomeRecord
status: open                # open → closed (closed = immutable)
kind: result                # retrospective | postmortem | result
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable party>
sensitivity: internal       # public | internal | restricted | sensitive
scope: slice                # slice | block
ref: <BL-XX.SEC-XX.SL-XXX | BL-XX>
forecast: { token_band: <XS|S|M|L|XL>, estimate: <value> }
actual: { value: <value>, drift_pct: <number> }
evidence: []                # [functional, quality, security, decision, provenance]
related-decs: []
---

# OUTC-<id> — <what happened, in one line>

## Shipped scope
<What was actually produced/delivered.>

## Forecast vs actual
<The drift narrative: what was estimated, what it took, why.>

## Evidence
<Links per category: functional · quality · security · decision · provenance. Machine form: an evidence.v1 record (reference/evidence/).>

## Carry-forward
<What feeds the next Block / velocity recalibration / InsightRecords emitted.>
