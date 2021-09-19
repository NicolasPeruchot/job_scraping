install:
	python -m pip install -r requirements.txt
	pre-commit install

job:
	streamlit run Offers.py
