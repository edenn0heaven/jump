#!/usr/bin/env bash
set -e

echo "=== Jump ==="

# Versions de Python pour lesquelles Pygame fournit des wheels précompilés
CANDIDATES=("python3.12" "python3.11" "python3.13" "python3.10")

PYTHON_BIN=""

# 1. Cherche une version déjà installée sur le système
for bin in "${CANDIDATES[@]}"; do
    if command -v "$bin" >/dev/null 2>&1; then
        PYTHON_BIN="$bin"
        break
    fi
done

# 2. Si aucune n'est trouvée, tente d'installer python3.12 via apt
if [ -z "$PYTHON_BIN" ]; then
    echo "Aucune version compatible trouvée. Installation de python3.12..."
    sudo apt update
    if sudo apt install -y python3.12 python3.12-venv; then
        PYTHON_BIN="python3.12"
    else
        echo ""
        echo "python3.12 n'est pas disponible dans tes dépôts apt."
        echo "Ajout du PPA deadsnakes pour récupérer une version compatible..."
        sudo apt install -y software-properties-common
        sudo add-apt-repository -y ppa:deadsnakes/ppa
        sudo apt update
        sudo apt install -y python3.12 python3.12-venv
        PYTHON_BIN="python3.12"
    fi
fi

echo "Utilisation de : $PYTHON_BIN ($($PYTHON_BIN --version))"

# Crée l'environnement virtuel avec la bonne version s'il n'existe pas déjà,
# ou s'il a été créé avec une version différente
if [ ! -d ".venv" ] || ! .venv/bin/python --version 2>/dev/null | grep -q "$($PYTHON_BIN --version | awk '{print $2}' | cut -d. -f1,2)"; then
    rm -rf .venv
    "$PYTHON_BIN" -m venv .venv
fi

# Active l'environnement virtuel
source .venv/bin/activate

# Installe/actualise pip et pygame
pip install --upgrade pip
pip install pygame

# Lance le script principal
python main.py