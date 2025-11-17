# Secure CI/CD Pipeline Demo (Use Case #2)

ADD COMMENTS 
**Goal:** Demonstrate a modern DevSecOps pipeline with security and quality gates, using a tiny Flask app, Docker, and scanners — all runnable locally or via GitHub Actions with **zero cloud cost**.

## What this repo shows

- Simple Python/Flask API (`app.py`) with a health endpoint.
- Unit tests with `pytest` (`tests/test_app.py`).
- Static application security testing (SAST) with **Bandit**.
- Dependency vulnerability scanning with **Safety**.
- Container image scanning with **Trivy**.
- Infrastructure-as-Code scanning with **Checkov** on a minimal Terraform file.
- A complete **GitHub Actions** workflow (`.github/workflows/ci.yml`) that wires all of this together.

This is a concrete implementation of:

> **Use Case #2 – Secure CI/CD with Quality Gates**  
> *“Nothing reaches production unless code, dependencies, image, and IaC all pass security and quality checks.”*

---

## 1. Run the demo locally on macOS

### 1.1. One-time setup

```bash
# From the repo root
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install checkov

# (Optional) Install Trivy via Homebrew for local image scan
brew install aquasecurity/trivy/trivy
```

### 1.2. Run tests and scans locally

```bash
# Static analysis
bandit -r .

# Unit tests
pytest -q

# Dependency vulnerabilities
safety check

# Build container image
docker build -t secure-ci-demo .

# Container scan (if Trivy installed)
trivy image secure-ci-demo

# IaC scan (infra/ directory)
checkov -d infra
```

You now have a **full DevSecOps-style pipeline** running locally with no cloud resources.

---

## 2. GitHub Actions CI/CD pipeline

The workflow is defined in `.github/workflows/ci.yml` and runs on:

- `push` to `main`/`master`
- Any `pull_request`

It performs, in order:

1. **Checkout source**  
2. **Install Python + dependencies**  
3. **Bandit** – static security scan  
4. **pytest** – unit tests  
5. **Safety** – dependency vulnerability scan  
6. **Docker build** – build `secure-ci-demo` image  
7. **Trivy** – container image security scan  
8. **Checkov** – IaC scan against the `infra/` folder

You can describe this to interviewers as:

> “This pipeline ensures that application code, dependencies, container image, and infrastructure all pass automated security and quality gates before deployment. It’s a practical DevSecOps implementation that can be extended to any enterprise stack.”

---

## 3. Suggested 45–60 second demo script

1. Open `README.md` and summarize the goal in one sentence.  
2. Quickly show `app.py`, `tests/test_app.py`, and `infra/main.tf`.  
3. In a terminal, run:
   ```bash
   bandit -r .
   pytest -q
   safety check
   docker build -t secure-ci-demo .
   trivy image secure-ci-demo   # if installed
   checkov -d infra
   ```
4. Open `.github/workflows/ci.yml` and say:  
   > “These same steps run automatically on every PR in GitHub Actions, so developers get immediate feedback and we prevent insecure changes from being merged.”

Record this as a short screen capture and send it along with your Platform Engineering cheat sheet.

---

## 4. Mapping to the interview story

You can describe this as:

- **Situation:** No automated security/quality gates in the pipeline.  
- **Task:** Implement a secure CI/CD workflow.  
- **Action:** Built a pipeline with SAST, tests, dependency scanning, container and IaC scanning using open-source tools and GitHub Actions.  
- **Result:** Security issues are caught before merge; developers get fast feedback; releases are safer and auditable.

This aligns perfectly with **Platform Engineering / DevSecOps** expectations.
