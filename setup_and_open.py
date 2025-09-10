#!/usr/bin/env python3
"""
Configura ambiente Python isolado (.venv), instala FastAPI e Uvicorn
e abre o projeto no VS Code.
Uso:
    python3 setup_and_open.py main.py
"""

import sys
import subprocess
from pathlib import Path

def sh(cmd, **kw):
    print(">>", " ".join(cmd))
    subprocess.run(cmd, check=True, **kw)

def main():
    if len(sys.argv) < 2:
        print("Uso: python setup_and_open.py <arquivo.py>")
        sys.exit(1)

    script_path = Path(sys.argv[1]).resolve()
    if not script_path.exists():
        print(f"❌ Arquivo {script_path} não encontrado")
        sys.exit(1)

    env_dir = Path(".venv")
    env_python = env_dir / "bin" / "python"

    # 1) Criar venv se não existir
    if not env_dir.exists():
        sh([sys.executable, "-m", "venv", str(env_dir)])
    else:
        print(">> venv já existe")

    # 2) Atualizar pip/setuptools/wheel
    sh([str(env_python), "-m", "pip", "install", "--upgrade", "pip", "wheel", "setuptools"])

    # 3) Instalar pacotes FastAPI
    sh([str(env_python), "-m", "pip", "install", "fastapi", "uvicorn[standard]"])

    # 4) Abrir projeto no VS Code
    try:
        sh(["code", str(script_path)])
        print(f"✅ Projeto {script_path.name} aberto no VS Code.")
        print("👉 Para rodar: .venv/bin/python -m uvicorn main:app --reload")
    except FileNotFoundError:
        print("❌ VS Code não encontrado no PATH.")
        print("No VS Code: Ctrl+Shift+P → 'Shell Command: Install code command in PATH'.")

if __name__ == "__main__":
    main()
