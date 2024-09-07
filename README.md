# EL CERRABOT 3000

Este script permite cerrar issues en gitlab que compartan un mismo label, reemplazandolo por uno nuevo.

# Instalación

## Requerimientos

- python 3.6 o superior
- Obtener un token de acceso de administracion de proyecto en gitlab.

## Pasos

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
# editar el script y reemplazar tokens y labels por los valores necesarios
vim replace_labels_for_issues.py
python3 replace_labels_for_issues.py
```
