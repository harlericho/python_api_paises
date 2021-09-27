# API RESTFUL HECHO EN PYTHON CON MYSQL
> Creación de una api restful para registrar los nombres de los paises con su continentes.

![](https://www.anychart.com/_design/img/upload/integration/python-flask-mysql-sample.png)

[![Visual Studio](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://visualstudio.microsoft.com)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/harlericho)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://www.microsoft.com/es-es/windows)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Twitter](https://badgen.net/badge/icon/twitter?icon=twitter&label)](https://twitter.com/harlericho)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/Naereen/badges)
[![Website myfakewebsitethatshouldnotexist.at.least.i.hope](https://img.shields.io/website-up-down-green-red/http/myfakewebsitethatshouldnotexist.at.least.i.hope.svg)](https://harlericho.github.io/portafolio/)
[![Python](https://badgen.net/pypi/python/black)](https://www.python.org/downloads/)


# Instalación:
- Tener instalado python 3.x o superior.
- Tener pip instalado.
- Tener virtualenv o venv instalado.
- Crear un entorno virtual con virtualenv o venv.
- Ejecutar requirements.txt dentro del entorno virtual:  
   > pip install -r requirements.txt
- Importar el script de la base de datos y cambiar la configuracion de la conexión.
    ```sh
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'nombre_basedatos'
    ```

## Iniciar el sistema:
- Ejecutar el entorno virtualenv o venv
  > windows: env\Script\activate

  > linux: source env/bin/activate

- Dentro del entorno virtual ejecutar el archivo app.py:
   > windows: python .\src\app.py

   > linux: python3 .\src\app.py

## _Realizado por:_
![](https://avatars.githubusercontent.com/u/42042270?s=48&v=4)

# Github: @harlericho

> The MIT License (MIT)

### Este programa o sistema puede ser tomado como guia o enseñanza para sus futuros  proyectos.
> Copyright (c) 2021 harlericho