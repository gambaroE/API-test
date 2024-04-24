# Gambaro_API

This project has its aim to create a simple python package that search for a table and say if it exist or not;\
or a similar function with GCS for searching for a file in a bucket.\
The project is based on Poetry and typer Library. You need to install Poetry to play with it.

1) Download the project inside a new folder
2) Using your shell, get inside the pyprojv2 folder
3) run shell command: `poetry install`
4) Try the command: `poetry run __main__.py`

The project was created using the poetry command: `poetry new --src <name_of_folder>`.\

### libraries ###
Here are the libraries implemented:
1) bqfinder:the script will ask for a table in the format project.dataset.table and will say if it exist or not
2) gcsfinder:the script will ask for a bucket if it exist ask if you want to download or upload a file

#### Poetry commands ###

1) `poetry install` (always do this to create the poetry env with the basic toml and then you can use poetry add command freely)
2) `poetry add \<package\>` -> you can add libraries directly into your .toml file
3) `poetry build` -> you can build you artifact

__N.B.__
GOOGLE CLOUD SDK has to be setted in the environment
download google sdk shell
- `gcloud config configurations create` crea configurazione 
- `gcloud config set` Imposta una proprietà di configurazione
- `gcloud auth login` esegue l'accesso a gcloud
- OBBLIGATORIO PER RUNNARE SCRIPT
- `gcloud auth application-default login` per settare le credenziali di default per runnare lo script