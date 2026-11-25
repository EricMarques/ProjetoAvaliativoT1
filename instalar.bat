@echo off
rem Cria o ambiente virtual e instala as dependencias do projeto

if not exist venv (
    echo Criando ambiente virtual...
    python -m venv venv
    if errorlevel 1 (
        echo Nao foi possivel criar o ambiente virtual. Verifique se o Python esta instalado.
        pause
        exit /b 1
    )
)

call venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo Erro ao instalar as dependencias.
    pause
    exit /b 1
)

echo.
echo Ambiente pronto. Para ativar, use: venv\Scripts\activate
pause