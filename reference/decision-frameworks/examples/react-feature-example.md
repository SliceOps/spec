# Example - React Feature Technical Decision Analysis

Scenario: add a filter panel to a decision list page.

## Technical decision analysis

### Relevant decisions loaded

- `ARC-current-frontend-state` - local UI state is default; server state is owned by the data-fetching layer.
- `UX-accessibility-baseline` - interactive controls must be keyboard usable and labeled.
- `TEST-frontend-baseline` - user-visible behavior requires component or flow evidence.

### Relationship to existing decisions

Classification: `conforms`

Rationale:

The feature adds local filtering controls and query parameters inside an existing route. It does not introduce global client state, a new UI framework, or a new API boundary.

### Analysis depth and materiality

Analysis depth: `focused`

| Dimension | Level | Rationale | Evidence or decision action |
|---|---|---|---|
| User interaction | material | User filters visible decisions | Behavior test |
| Usability and accessibility | material | Panel adds controls and focus order | Keyboard/label evidence |
| State ownership | material | Filter state must be local or URL-owned | Component test and route behavior |
| Boundary and contract | low | Existing API supports query params | Type check or API fixture |
| Compatibility and versioning | low | Existing route remains valid | Smoke/user-visible test |
| Performance and scale | low | List size is bounded by existing paging | Normal review |
| DEC-required | N/A | No accepted frontend decision changes | No DEC |

### Forces and constraints

- Business capability: decision discovery.
- User interaction: human UI.
- Usability/accessibility: labeled controls, keyboard navigation, no hidden state traps.
- Localization/time/region: N/A unless filter labels are translated by adopter.
- State ownership: local state for draft controls; URL query for shareable applied filters.
- Boundary/contract: existing decision list query.
- Error/recovery model: preserve loading/error/empty states.
- Feedback strategy: behavior-first component test.
- Maintainability/complexity: no global store for route-local state.

### Universal-to-specific routing

Material universal dimensions:

- User interaction -> load frontend behavior testing guidance.
- State ownership -> load frontend state pack.
- Usability/accessibility -> load accessibility checklist.

Stack Pattern Packs loaded after generic analysis:

- `<react-pack>` -> state placement, controls, API states.
- `<testing-pack>` -> visible behavior evidence.

### Selected path

Selected pattern/approach:

- Keep draft filter state local to the panel.
- Persist applied filters to the URL query string.
- Reuse existing data-fetching layer for server state.
- Preserve loading, error, empty, and permission states.

Why this is adequate now:

The state is route-local and user-driven. A global store would add coupling without cross-route reuse evidence.

### Rejected alternatives

| Alternative | Why rejected now | Revisit trigger |
|---|---|---|
| Global client store | No cross-route ownership need | Filters are reused across multiple routes/workflows |
| New API endpoint | Existing query can express filters | Query shape becomes slow or semantically wrong |
| Pure client-side filtering | Data set is server-paged | Product accepts bounded local-only list |

### Evidence required

- [ ] Feedback loop: component behavior test for selecting, applying, clearing filters.
- [ ] Functional: URL updates and existing loading/error/empty states still work.
- [ ] Compatibility/accessibility/compliance: labeled controls and keyboard path evidence.
- [ ] Decision: no DEC required; conforms to accepted decisions.

### Revisit triggers

- Filter state becomes shared across routes.
- Query performance degrades.
- Accessibility regression is found.

### HITL disposition

- [x] No new human decision required; conforms to accepted decisions.

