init:
	if [[ -d ./venv ]]; then rm -rf venv; fi \
	&& python3.6 -m venv venv \
	&& . venv/bin/activate \
	&& pip install --upgrade pip setuptools wheel \
	&& pip install -r requirements.txt

test:
	. venv/bin/activate \
	&& python -m pytest tests
	# make lint

lint:
	. venv/bin/activate \
	&& python -m flake8 ./aws_lambda_package ./tests
