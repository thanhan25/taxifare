.PHONY: run-api

# Command to run the API
run-api:
	uv run uvicorn api.fast:app --reload --host 0.0.0.0 --port 8000
