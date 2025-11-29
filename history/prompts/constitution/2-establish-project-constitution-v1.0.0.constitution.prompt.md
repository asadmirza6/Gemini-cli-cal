---
id: 2
title: Establish Project Constitution v1.0.0
stage: constitution
date: 2025-11-29
surface: agent
model: gemini-1.5-pro
feature: none
branch: main
user: 
command: "/sp.constitution ## 1. Project Principles & Standards ..."
labels: ["constitution", "documentation", "project-setup"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml:
  - "N/A"
prompt_text: |
  ---
  description: Create or update the project constitution from interactive or provided principle inputs, ensuring all dependent templates stay in sync
  ---

  ## User Input

  ```text
  $ARGUMENTS
  ```

  You **MUST** consider the user input before proceeding (if not empty).

  ## Outline

  You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

  Follow this execution flow:

  1. Load the existing constitution template at `.specify/memory/constitution.md`.
     - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
     **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

  2. Collect/derive values for placeholders:
     - If user input (conversation) supplies a value, use it.
     - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
     - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
     - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
       - MAJOR: Backward incompatible governance/principle removals or redefinitions.
       - MINOR: New principle/section added or materially expanded guidance.
       - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
     - If version bump type ambiguous, propose reasoning before finalizing.

  3. Draft the updated constitution content:
     - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
     - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
     - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
     - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

  4. Consistency propagation checklist (convert prior checklist into active validations):
     - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
     - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
     - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
     - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
     - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

  5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
     - Version change: old → new
     - List of modified principles (old title → new title if renamed)
     - Added sections
     - Removed sections
     - Templates requiring updates (✅ updated / ⚠ pending) with file paths
     - Follow-up TODOs if any placeholders intentionally deferred.

  6. Validation before final output:
     - No remaining unexplained bracket tokens.
     - Version line matches report.
     - Dates ISO format YYYY-MM-DD.
     - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

  7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

  8. Output a final summary to the user with:
     - New version and bump rationale.
     - Any files flagged for manual follow-up.
     - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

  Formatting & Style Requirements:

  - Use Markdown headings exactly as in the template (do not demote/promote levels).
  - Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
  - Keep a single blank line between sections.
  - Avoid trailing whitespace.

  If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

  If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

  Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

  ---

  As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

  1) Determine Stage
     - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

  2) Generate Title and Determine Routing:
     - Generate Title: 3–7 words (slug for filename)
     - Route is automatically determined by stage:
       - `constitution` → `history/prompts/constitution/`
       - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
       - `general` → `history/prompts/general/`

  3) Create and Fill PHR (Shell first; fallback agent‑native)
     - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
     - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
     - If the script fails:
       - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
       - Allocate an ID; compute the output path based on stage from step 2; write the file
       - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

  4) Validate + report
     - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
     - On failure: warn, don't block. Skip only for `/sp.phr`.


  /sp.constitution ## 1. Project Principles & Standards

  - **Python Version**: Latest stable (>=3.11)
  - **Programming Approach**:
    - Use **type hints** everywhere (PEP 484)
    - Use **dataclasses** for structured data
    - Modular, reusable, and testable code
    - Clear and descriptive naming conventions
    - Proper **docstrings** and inline comments
    - Avoid hardcoding secrets, paths, or credentials
    - Code should be **readable, maintainable, and PEP8 compliant**
  - **Testing Approach**:
    - Follow **Test-Driven Development (TDD)** for all features
    - Write unit tests for each function and module
    - Use `pytest` or `unittest` framework
    - Maintain >90% test coverage for core calculator functions

  ---

  ## 2. Technical Stack

  - **Programming Language**: Python 3.11+
  - **Core Libraries**:
    - `dataclasses`
    - `math` / `decimal` for precise calculations
    - `typing` for type hints
    - `pytest` for testing
  - **Optional Enhancements**:
    - CLI: `argparse` or `click`
    - Logging: `logging` module
    - File handling: `json` or `pickle` for saving results
  - **MCP Servers**:
    - GitHub: version control, commits, branches, PRs
    - Google Drive: optional storage for user data
    - Shell: safe operations only (listing files, git init, etc.)

  ---

  ## 3. Quality Requirements

  - **Code Quality**:
    - Readable, maintainable, and modular
    - Consistent formatting (PEP8)
    - Type hints and docstrings mandatory
    - Use dataclasses for structured data
  - **Testing**:
    - TDD approach, automated test coverage >90% for core logic
    - Test edge cases (division by zero, invalid input, float precision)
  - **Security & Safety**:
    - Do not hardcode API tokens or sensitive data
    - Safe shell usage only
  - **Documentation**:
    - README.md with project description, installation, usage, and examples
    - CONTRIBUTING.md describing coding standards, testing, and branching strategy
  - **Version Control**:
    - Git workflow: feature branches, commits with descriptive messages, PR reviews
    - Avoid force pushes or destructive operations

  ---

  ## 4. Agent Behavior

  - **Full autonomy** in managing calculator project, **but always confirm destructive actions** (like removing files or reinitializing git)
  - Generate clean, professional code using **TDD and Python best practices**
  - Keep track of project state, files, and modules
  - Before using MCP servers, describe actions and request confirmation if required
  - Output only **code or instructions** when needed; avoid unnecessary explanations
  - Ensure that **all generated code passes tests** before marking a feature as complete

  ---

  ## 5. Forbidden Actions

  - No destructive shell commands (`rm -rf`, `format disk`, etc.)
  - No modification of OS-level files or credentials
  - Do not push to GitHub or GDrive without explicit confirmation
  - No installation of untrusted packages
  - No assumptions about user secrets or tokens

  ---

  ## 6. Deliverables per Feature

  - Fully implemented calculator functions:
    - `add`, `subtract`, `multiply`, `divide`, `power`, `sqrt`, `percent`
  - Unit tests for each function
  - CLI interface for user input
  - Optional logging and result storage
  - Documentation updates

  ---

  **Always follow these standards and quality guidelines for every code, test, or documentation generation task. Maintain professional, clean, and Pythonic code at all times.
response_text: |
  The constitution has been successfully updated to version 1.0.0. All dependent templates and command files were reviewed and found to be consistent. No manual follow-up is required.
outcome: |
  The project constitution was established, detailing principles, technical stack, quality requirements, agent behavior, forbidden actions, and deliverables. All dependent templates and command files were verified for consistency.
evaluation: |
  The task was completed successfully. The agent correctly identified the placeholders, populated them with the provided content, performed the consistency check across dependent files, and generated the sync impact report. The version was set to 1.0.0 as it's the initial establishment of the constitution.
---