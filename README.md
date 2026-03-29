# agentic-ai-system

## Overview
AutoFlow AI is a multi-agent system that autonomously manages enterprise workflows such as employee onboarding. The system detects failures, self-corrects, and maintains an auditable log of all decisions and actions.

## Features
- Multi-agent collaboration
- Autonomous decision making
- Error detection and self-recovery
- SLA monitoring
- Audit trail logging

## Agents
1. Orchestrator Agent – Controls workflow
2. Planner Agent – Breaks tasks into steps
3. Data Agent – Retrieves data
4. Decision Agent – Makes decisions
5. Action Agent – Executes actions
6. Verification Agent – Verifies task completion
7. Audit Agent – Logs all actions

## Setup Instructions
```bash
pip install -r requirements.txt
python main.py
