install:
	python -m pip install -r requirements.txt

job:
	python -m scrapping.the_hub
	python -m scrapping.HF
