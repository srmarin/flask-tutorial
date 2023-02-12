build:
	docker build -t flask-smorest-api .
run:
	docker run -dp 10000:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flash run --host 0.0.0.0"