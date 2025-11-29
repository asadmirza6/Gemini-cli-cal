# Tasks: Basic Calculator Library

**Input**: Design documents from `specs/001-basic-calculator-spec/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/api.md

**Tests**: Tests are included as explicitly requested by the constitution's TDD mandate and >90% test coverage requirement.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure: `src/calculator/`, `tests/`
- [X] T002 Create `src/calculator/__init__.py`
- [X] T003 Create `src/calculator/exceptions.py` for custom exceptions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Define custom `InvalidInputError` in `src/calculator/exceptions.py`
- [X] T005 Setup `pytest` environment and `conftest.py` in `tests/`
- [X] T006 Create `tests/__init__.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: Implement core arithmetic operations with basic error handling.

**Independent Test**: Running unit tests for `add`, `subtract`, `multiply`, `divide` functions, including error handling for division by zero and invalid input types.

### Tests for User Story 1
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T007 [P] [US1] Unit test `add` function (positive, negative, zero, float) in `tests/test_operations.py`
- [X] T008 [P] [US1] Unit test `subtract` function (positive, negative, zero, float) in `tests/test_operations.py`
- [X] T009 [P] [US1] Unit test `multiply` function (positive, negative, zero, float) in `tests/test_operations.py`
- [X] T010 [P] [US1] Unit test `divide` function (positive, negative, zero, float) in `tests/test_operations.py`
- [X] T011 [P] [US1] Unit test `divide` by zero error handling in `tests/test_operations.py`
- [X] T012 [P] [US1] Unit test `add` with invalid input type (non-numeric) in `tests/test_operations.py`

### Implementation for User Story 1

- [X] T013 [US1] Implement `add` function in `src/calculator/operations.py`
- [ ] T014 [US1] Implement `subtract` function in `src/calculator/operations.py`
- [ ] T015 [US1] Implement `multiply` function in `src/calculator/operations.py`
- [ ] T016 [US1] Implement `divide` function in `src/calculator/operations.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Advanced Operations (Priority: P2)

**Goal**: Implement power, square root, and percentage operations with associated edge case handling.

**Independent Test**: Running unit tests for `power`, `sqrt`, `percent`, and `add_percent` functions, including error handling for negative square roots and `0^0` behavior.

### Tests for User Story 2
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T017 [P] [US2] Unit test `power` function (positive, negative exponent, `0^0` behavior) in `tests/test_operations.py`
- [X] T018 [P] [US2] Unit test `sqrt` function (positive, zero) in `tests/test_operations.py`
- [ ] T019 [P] [US2] Unit test `sqrt` of negative number error handling in `tests/test_operations.py`
- [X] T020 [P] [US2] Unit test `percent` function (direct conversion) in `tests/test_operations.py`
- [X] T021 [P] [US2] Unit test `add_percent` function in `tests/test_operations.py`

### Implementation for User Story 2
- [ ] T022 [US2] Implement `power` function in `src/calculator/operations.py`
- [ ] T023 [US2] Implement `sqrt` function in `src/calculator/operations.py`
- [ ] T024 [US2] Implement `percent` function in `src/calculator/operations.py`
- [X] T025 [US2] Implement `add_percent` function in `src/calculator/operations.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T026 Configure `requirements.txt` with `pytest` and other dependencies.
- [X] T027 Add type hints to all function signatures in `src/calculator/operations.py`.
- [X] T028 Add docstrings to all functions and modules.
- [X] T029 Implement logging for errors in `src/calculator/operations.py`.
- [X] T030 Ensure 90%+ test coverage for `src/calculator/operations.py`.
- [X] T031 Update `README.md` with installation and usage instructions.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks can run in parallel where independent.
- All Foundational tasks can run in parallel where independent.
- Once Foundational phase completes, User Stories 1 and 2 can start in parallel (if team capacity allows).
- All tests for a user story marked [P] can run in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Each story adds value without breaking previous stories

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
