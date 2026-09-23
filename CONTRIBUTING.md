# Contributing to rangemap-tayra

Thank you for your interest in contributing to `rangemap-tayra`! We welcome contributions from everyone.

## Getting Started

1. Fork the repository and clone your fork locally.
2. Ensure there is a corresponding **Issue** or **Discussion** for your intended changes before you begin (see [Issue & Discussion Linkage](#issue--discussion-linkage-mandatory) below).
3. Create a new branch for your changes following the [Branch Naming Rules](#branch-naming-rules).
4. Make your changes and ensure they adhere to the project's standards.
5. Submit a Pull Request (PR) linking your issue or discussion.

---

## Issue & Discussion Linkage (Mandatory)

To maintain clarity and ensure all changes are properly discussed and tracked:

* **Every Pull Request must be explicitly linked to an existing Issue or Discussion.**
* If you are planning a new feature, a significant refactoring, or a major change, please start a Discussion or open an Issue first to gather feedback and reach a consensus.
* For minor bug fixes or documentation updates, opening an Issue to track the task before submitting the PR is required.

---

## Branch Naming Rules

To keep our git history clean and make tracking contributions easier, please follow these naming conventions for your branches.

### 1. Standard Contributions (Manual Work)

If you are implementing changes manually without using an AI coding assistant, use the following format:

```text
<type>/<description>

```

* **Types:**
* `feat`: A new feature
* `fix`: A bug fix
* `docs`: Documentation only changes
* `refactor`: A code change that neither fixes a bug nor adds a feature
* `test`: Adding missing tests or correcting existing tests
* `chore`: Changes to the build process or auxiliary tools/libraries


* **Description:** Short, descriptive summary of the change in **kebab-case** (e.g., `fix/range-boundary-bug`).

---

### 2. AI-Assisted Contributions

If you use an AI coding assistant (such as Gemini, Claude, etc.) to help write or refactor code for your contribution, please use a double-prefix format to ensure transparency:

```text
<type>/<ai-agent-name>/<description>

```

* **Examples:**
* `feat/gemini/add-custom-range-parser`
* `refactor/claude/optimize-mapping-logic`



---

## Pull Request Process

1. Reference the related Issue or Discussion in your Pull Request description (e.g., `Closes #123`).
2. Update the documentation if your changes require it.
3. Ensure that any relevant tests pass successfully.
4. Open a Pull Request with a clear description of the problem and solution.

Thank you for helping improve `rangemap-tayra`!