# Makefile for tap-chat dev environment

.PHONY: backend frontend dev

backend:
	poetry run uvicorn tap_chat.backend.main:app --reload --port 8000 --app-dir src

frontend:
	poetry run streamlit run src/tap_chat/frontend/app.py --server.port 8501

dev:
	@echo "Starting tap-chat backend and frontend..."
	# Start backend and frontend concurrently
	poetry run uvicorn tap_chat.backend.main:app --reload --port 8000 --app-dir src & \
	sleep 2 && \
	poetry run streamlit run src/tap_chat/frontend/app.py --server.port 8501
