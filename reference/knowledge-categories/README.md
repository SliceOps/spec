# Knowledge Categories — Capa B.1 Reference Taxonomy v1.0

The canonical SliceOps™ knowledge-layer taxonomy: **27 universal categories**. SliceOps IP (Capa B.1); documentation under CC BY 4.0 (final terms pending IP/Legal — see `../../governance/IPR_POLICY.md`).

This taxonomy classifies the *knowledge layer* of a SliceOps-compliant corpus (the data a brain holds), distinct from the *cognitive entities* (`../entity-catalog/`, the reasoning artifacts). It is a **reference** taxonomy — like a library classification scheme: the category structure is universal and shared; the contents are the adopter's own and never part of this spec.

## The 27 categories

Numbers are stable identifiers (gaps are intentional — reserved/retired slots are not recycled, mirroring sub-numbering discipline). Each: purpose · typical content type · sensitivity default (from the canonical set `public | internal | restricted | sensitive`; adopters override per their audience policy and applicable law).

| # | Category | Purpose | Typical content | Sensitivity default |
|---|---|---|---|---|
| 01 | financial | Financial position, accounts, money flows | statements, budgets, ledgers | sensitive |
| 02 | contact | Contactable parties and channels | contact records, directories | restricted |
| 03 | health | Health status, records, care | medical records, care notes | sensitive |
| 04 | documents | Canonical documents of record | scans, official docs | restricted |
| 05 | ai-agent-context | Operating context for AI agents | agent instructions, context packs | internal |
| 06 | compliance-declarations | Compliance attestations and declarations | control mappings, attestations | internal |
| 07 | identity | Identity attributes and credentials | IDs, biometrics references | sensitive |
| 08 | network | Networks, infrastructure topology, connectivity | network maps, access topology | restricted |
| 09 | relational-graph | Relationships among people/orgs/entities | relationship edges, org graphs | restricted |
| 10 | products | Products owned or built | product records, specs | internal |
| 11 | home-interaction | Home environment interaction surfaces | smart-home, interaction logs | restricted |
| 12 | work-employment | Work, employment, professional engagements | roles, agreements, history | restricted |
| 13 | tax | Tax position and filings | filings, tax records | sensitive |
| 14 | education | Education, learning, credentials | courses, certifications | internal |
| 15 | lifestyle-interests | Lifestyle context and interests | preferences, interests | internal |
| 16 | legal-contracts | Legal agreements and contractual status | contracts, legal docs | sensitive |
| 17 | travel-mobility | Travel and mobility | itineraries, mobility records | restricted |
| 18 | real-estate | Real-estate holdings and property | property records, deeds | restricted |
| 19 | vehicles | Vehicles owned/operated | vehicle records, maintenance | internal |
| 20 | insurance | Insurance coverage and policies | policies, claims | restricted |
| 21 | subscriptions | Recurring subscriptions and services | subscription inventory | internal |
| 22 | devices | Devices and hardware inventory | device inventory, configs | restricted |
| 23 | home-management | Home operations and management | maintenance, household ops | internal |
| 24 | pets | Pets and animal care | pet records, care | internal |
| 25 | hobbies-gear | Hobbies and associated gear | gear inventory, hobby notes | internal |
| 26 | business | Business operations and ventures | venture records, ops | restricted |
| 29 | knowledge | General knowledge corpus and notes | reference notes, research | internal |

## Universal vs personal-flavored

Most categories are universal across adopter types (e.g., `16-legal-contracts`, `26-business`, `06-compliance-declarations`). Some are personal-flavored (e.g., `03-health`, `13-tax`, `24-pets`). A future taxonomy v2.0 may abstract personal-flavored categories into **vertical packs** (Personal Pack, Enterprise Pack, etc.) so an enterprise adopter loads only the relevant subset. v1.0 keeps the full canonical set; selection is an adopter concern.

## Sensitivity defaults are defaults

The sensitivity column is a **starting default**, not a mandate. Adopters set actual sensitivity per their audience policy, jurisdiction, and applicable regulation (R11). Categories defaulting to `sensitive` are the ones most likely to require restricted-access handling — adopters should treat those as load-on-demand, never bulk-loaded into agent context (a privacy-by-default posture).

## Adopter customization rules

Adopters **may**: use the taxonomy as-is (recommended — preserves cross-adopter interoperability); add adopter-specific categories (in their own brain, numbered in a reserved range, not here); restrict the loaded subset to relevant categories. Adopters **may not**: redefine a canonical category's semantics; recycle a retired number; claim SliceOps-compliance while conflicting canonical category meanings.

## Relationship to cognitive entities

Knowledge categories classify *what the corpus knows* (the data layer). Cognitive entities (`../entity-catalog/`) classify *how the corpus reasons and decides* (DECs, Insights, etc.). A DecisionRecord about a financial policy is a cognitive entity (DecisionRecord) that *references* knowledge in category `01-financial` — the two layers are orthogonal and cross-reference, never merge.
