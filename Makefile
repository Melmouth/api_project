.PHONY: run

run:
	uvicorn main:app --reload

install:
	pip install -r requirements.txt

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

local:
	@echo "Launching FastAPI server..."
	uvicorn main:app --reload & \
	sleep 2; \
	@echo "Launching Streamlit app..."; \
	streamlit run stream_launch.py