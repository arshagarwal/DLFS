# downloads packages and sets environment for testing
# This file has bugs and requires fixing 
# Refer dlfs official colab notebook for setting up env
pip install gdown
pip install -r requirements.txt
python download_models.py
gdown https://drive.google.com/u/0/uc?id=1pB4mufFtzbJSxxv_2iFrBPD3vp_Ef-n3&export=download
unzip /content/DLFS/males_model.zip -d checkpoints