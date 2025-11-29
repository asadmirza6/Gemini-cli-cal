<!--
Sync Impact Report
Version change: 1.0.0 -> 1.1.0
Modified principles:
  - II. Technical Stack (added Configuration Management, Dependency Management)
  - III. Quality Requirements (added Error Handling, Logging Standards, Deployment & Application Versioning, Scalability)
Added sections:
  - II. Technical Stack (Configuration Management, Dependency Management)
  - III. Quality Requirements (Error Handling, Logging Standards, Deployment & Application Versioning, Scalability)
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated (no changes needed, structure aligns)
  - .specify/templates/spec-template.md: ✅ updated (no changes needed, structure aligns)
  - .specify/templates/tasks-template.md: ✅ updated (no changes needed, structure aligns)
  - .gemini/commands/sp.adr.toml: ✅ updated (no changes needed)
  - .gemini/commands/sp.analyze.toml: ✅ updated (no changes needed)
  - .gemini/commands/sp.checklist.toml: ✅ updated (no changes needed)
  - .gemini/commands/sp.clarify.toml: ✅ updated (no changes needed)
  - .gemini/commands/sp.constitution.toml: ✅ updated (no changes needed)
  - .gemini/commands/sp.git.commit_pr.toml: ✅ updated (no changes needed)
  - .gemini/commands/sp.implement.toml: ✅ updated (no changes needed)
  - .gemini/commands/sp.phr.toml: ✅ updated (no changes needed)
  - .gemini/commands/sp.plan.toml: ✅ updated (no changes needed)
  - .gemini/commands/sp.specify.toml: ✅ updated (no changes needed)
  - .gemini/commands/sp.tasks.toml: ✅ updated (no changes needed)
Follow-up TODOs: None
-->
# Calculator CLI Project Constitution

## Core Principles

### I. Project Principles & Standards
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

### II. Technical Stack
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
- **Configuration Management**:
  - All configurations MUST be externalized (e.g., environment variables, `.env` files).
  - NO hardcoded secrets or sensitive information.
  - Use a dedicated configuration library (e.g., `python-dotenv`, `Dynaconf`) for structured access.
- **Dependency Management**:
  - Use `pip` with `requirements.txt` for explicit dependency declaration.
  - Pin exact versions of direct dependencies to ensure reproducibility.
  - Regularly review and update dependencies to address security vulnerabilities.

### III. Quality Requirements
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
- **Error Handling**:
  - All functions MUST handle expected errors gracefully, providing informative messages.
  - Custom exceptions should be used for application-specific error conditions.
  - Errors should be logged with appropriate severity levels.
- **Logging Standards**:
  - Use Python's built-in `logging` module.
  - Log messages MUST be structured (e.g., JSON format) for easier analysis.
  - Define clear logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) for different event types.
- **Deployment & Application Versioning**:
  - Application versions MUST follow Semantic Versioning (MAJOR.MINOR.PATCH).
  - Deployment process MUST be automated (e.g., CI/CD pipeline).
  - Backward compatibility MUST be maintained for MINOR and PATCH versions.
- **Scalability**:
  - Design choices SHOULD consider future scaling requirements for concurrent operations.
  - Avoid global state where possible; prefer stateless function design.
  - Operations handling large inputs MUST be optimized for performance.

### IV. Agent Behavior
- **Full autonomy** in managing calculator project, **but always confirm destructive actions** (like removing files or reinitializing git)
- Generate clean, professional code using **TDD and Python best practices**
- Keep track of project state, files, and modules
- Before using MCP servers, describe actions and request confirmation if required
- Output only **code or instructions** when needed; avoid unnecessary explanations
- Ensure that **all generated code passes tests** before marking a feature as complete

### V. Forbidden Actions
- No destructive shell commands (`rm -rf`, `format disk`, etc.)
- No modification of OS-level files or credentials
- Do not push to GitHub or GDrive without explicit confirmation
- No installation of untrusted packages
- No assumptions about user secrets or tokens

### VI. Deliverables per Feature
- Fully implemented calculator functions:
  - `add`, `subtract`, `multiply`, `divide`, `power`, `sqrt`, `percent`
- Unit tests for each function
- CLI interface for user input
- Optional logging and result storage
- Documentation updates

**Always follow these standards and quality guidelines for every code, test, or documentation generation task. Maintain professional, clean, and Pythonic code at all times.**

## Governance
All PRs/reviews must verify compliance; Complexity must be justified; Use `.specify/memory/constitution.md` for runtime development guidance

**Version**: 1.1.0 | **Ratified**: 2025-11-29 | **Last Amended**: 2025-11-29