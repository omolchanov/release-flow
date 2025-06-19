"""
Release Flow — Compact Summary
Purpose: Manages versioned releases with support for hotfixes and stabilization.

Key Branches:
- main – stable production code
- release/x.x – pre-release stabilization
- hotfix/x.x.x – urgent post-release fixes
- feature/* – new features or changes

Flow:
- Develop features → feature/* branches
- Prepare release → create release/x.x from main
- Finalize release → bugfixes, tests on release/x.x
- Release → merge release/x.x to main, tag
- Hotfix → branch hotfix/x.x.x from main, merge back after fix

Best For:
SDKs, libraries, or apps with versioned/LTS releases.

When to Run Tests in Release Flow
- Unit Tests
-- On every commit/push (feature, release, hotfix)
-- Fast checks of isolated code

- Integration Tests
-- On merge to release/x.x or main
-- Verifies components work together

- Acceptance Tests
-- Before merging release/x.x to main
-- Simulates real user behavior (end-to-end)
"""


from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify(message="Hello, World!"), 200


@app.route('/feature-1')
def featurer_1():
    return jsonify(message="Feature 1"), 200


@app.route('/email')
def feature_email():
    return jsonify(message="Emails have been sent"), 200


if __name__ == '__main__':
    app.run()

