# Study Planner AI - OpenEnv Environment

This repository contains the OpenEnv environment for the AI Study Planner project.

## Overview

This environment simulates a study planner where users can take actions like selecting subjects for study sessions. The environment provides rewards based on the selected actions.

## Structure

- `inference.py` - main entrypoint for OpenEnv; contains the `main()` function.
- `study_env.py` - the environment logic for the study planner.
- `Dockerfile` - builds the environment container for OpenEnv.
- `requirements.txt` - Python dependencies required to run the environment.
- `openenv.yaml` - OpenEnv configuration specifying endpoints and tasks.

## How to run locally

```bash
pip install -r requirements.txt
python inference.py
