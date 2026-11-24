# llm-reply-reviewer

[![CI](https://github.com/cinarcem/llm-reply-reviewer/actions/workflows/ci.yml/badge.svg)](https://github.com/cinarcem/llm-reply-reviewer/actions/workflows/ci.yml)

LLM-powered review of customer-service replies, before they are sent.

> **Status:** Early development (Phase 0: foundations). All data in this repository is synthetic.

## What it does

An agent drafts a reply to a customer's request, complaint, objection or question. Before sending it, the agent submits the draft for review. The review covers:

- **Request coverage:** Does the reply address every request the customer made?
- **Spelling and grammar:** Spelling, suffixes and punctuation.
- **Clarity:** Sentence structure, ambiguity, unexplained jargon.
- **Tone:** Professional, respectful, not evasive.
- **Risk:** Requests for sensitive data, unconditional commitments, template leftovers.

The result contains findings with exact quotes from the draft, a score, a verdict and a corrected version of the draft.

<!-- TODO: Add a short example input and output. -->

<!-- TODO : Add an architecture section. -->

## Design decisions

- **Precision over recall.** The reviewer reports only what it is confident about. A false finding costs more than a missed one, because it teaches users to ignore the tool.
- **Domain-agnostic core, pluggable domain profiles.** Domain-specific rules (conventions, sensitive data types, masking formats, examples) come from a profile, not from the prompt or the code. One code base serves every domain, and a real organization's rules stay in its own environment. This repository ships synthetic profiles only.
- **One source for every tool version.** Python tools are pinned in `uv.lock` and run through `uv run --locked`, both in pre-commit hooks and in CI. The uv version itself is pinned in `pyproject.toml`. Local checks and CI cannot drift apart.
- **Trunk-based development.** Changes reach `main` only through pull requests with passing checks, merged as a single squashed commit. Environments are not branches: later, one image built from `main` is promoted to each environment by configuration.

## Getting started

Prerequisite: [uv](https://docs.astral.sh/uv/) 0.9.17. uv installs Python 3.13 if it is missing.

```bash
uv sync
uv run pre-commit install
uv run pytest
uv run uvicorn llm_reply_reviewer.api.main:app --reload
```

The API then answers at `http://127.0.0.1:8000/health`.

## Roadmap

| Phase              | Goal                                                | Status      |
| ------------------ | --------------------------------------------------- | ----------- |
| 0. Foundations     | Repository, tooling, CI, README                     | In progress |
| 1. Core            | End-to-end evaluation service, running locally      | Planned     |
| 2. LLM engineering | Tracing, eval regression gate, model comparison, UI | Planned     |
| 3. Kubernetes      | Local cluster, GitOps, queue-based autoscaling      | Planned     |
| 4. Cloud           | Terraform and EKS, created and destroyed on demand  | Planned     |

## License

[MIT](LICENSE)
