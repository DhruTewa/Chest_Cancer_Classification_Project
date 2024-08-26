# Chest-Disease-Classification-from-Chest-CT-Scan-Image


## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml 



## Live matarials docs

[link](https://docs.google.com/document/d/1UFiHnyKRqgx8Lodsvdzu58LbVjdWHNf-uab2WmhE0A4/edit?usp=sharing)


## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

## How to run?

```bash
conda create -n deeplearning python=3.10 -y
```

```bash
conda activate deeplearning
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

### MLflow dagshub connection url
``` bash
MLFLOW_TRACKING_URI=https://dagshub.com/DhruTewa/Chest_Cancer_Classification_Project.mlflow \
MLFLOW_TRACKING_USERNAME=dhrutewa \
MLFLOW_TRACKING_PASSWORD=6dd20d48b986987406f9d2c820406d539cde2a85a \
python script.py
dd20d48b986987406f9d2c820406d539cde2a85a
```

### RUN from bash terminal
export MLFLOW_TRACKING_URI=https://dagshub.com/DhruTewa/Chest_Cancer_Classification_Project.mlflow

export MLFLOW_TRACKING_USERNAME=dhrutewa 

export MLFLOW_TRACKING_PASSWORD=dd20d48b986987406f9d2c820406d539cde2a85a
