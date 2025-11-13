Demo Script – Secure CI/CD Pipeline (Use Case #2)

1. Open the repo in VS Code or another editor.
2. Show:
   - app.py
   - tests/test_app.py
   - infra/main.tf
   - .github/workflows/ci.yml

3. In a terminal at the repo root, run:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pip install checkov
   bandit -r .
   pytest -q
   safety check
   docker build -t secure-ci-demo .
   trivy image secure-ci-demo      # if installed
   checkov -d infra

4. Narrate briefly how each step represents a security/quality gate.
5. Optionally show the same steps in GitHub Actions after pushing the repo.
