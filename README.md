# EDSML Preparation

Preparation workspace for Imperial's Environmental Data Science and Machine
Learning programme.

## Week 1: Foundations and Tooling

**Goal:** complete the Python, Git, and mathematics preparation, then leave a
reproducible repository that is ready for the later numerical and ML projects.

### Start here

1. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

2. Verify the toolchain:

   ```powershell
   python --version
   git --version
   jupyter lab
   ```

3. Work through the checklist in
   [`week01-foundations/README.md`](week01-foundations/README.md).

Later projects use a few additional scientific packages. Install them when
starting Week 2 with `python -m pip install -r requirements-projects.txt`.

The complete eight-week sequence and deliverables are tracked in
[`ROADMAP.md`](ROADMAP.md).

## Repository structure

```text
.
|-- week01-foundations/   # Python, Git, maths, and environment checks
|-- week02-environmental-data/
|-- week03-numerical-methods/
|-- week04-heat-equation/
|-- week05-inverse-problem/
|-- week06-environmental-ml/
|-- week07-scientific-ml/
|-- week08-portfolio/
|-- notebooks/            # Reusable exploratory notebooks
|-- src/                  # Reusable Python modules
|-- tests/                # Automated checks
|-- requirements.txt
|-- requirements-projects.txt
|-- ROADMAP.md
`-- README.md
```

Later weekly projects should receive their own directory and document their
data sources, environment, commands, results, and limitations.

## Working conventions

- Use small, descriptive commits.
- Keep generated data, virtual environments, and notebook checkpoints out of
  Git.
- Put reusable logic in `src/`; use notebooks for exploration and explanation.
- Record dependencies in `requirements.txt`.
- Run `python -m pytest` before considering a deliverable complete.
