.PHONY: run push

run:
	uvicorn main:app --host 0.0.0.0 --port 10000 --reload

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

push:
	git add .
	git commit -m "Auto Push"
	git push origin main