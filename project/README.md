
### 2. **Subir a GitHub**

Para subir el proyecto a GitHub, sigue estos pasos:

#### **Pasos para crear y subir un repositorio en GitHub:**

1. **Crea un repositorio en GitHub**:
   - Ve a tu cuenta de GitHub.
   - Haz clic en el botón **New** para crear un nuevo repositorio.
   - Asigna un nombre al repositorio, por ejemplo, `ajedrez-peones`.
   - Elige si el repositorio será público o privado.
   - Haz clic en **Create repository**.

2. **Inicializa Git en tu carpeta del proyecto**:
   - Ve a la carpeta donde tienes tu código en tu máquina local.
   - Abre la terminal y escribe:
     ```bash
     git init
     ```

3. **Añadir los archivos al repositorio**:
   - Asegúrate de que el archivo `README.md` y el código estén en la carpeta.
   - Añade todos los archivos al repositorio:
     ```bash
     git add .
     ```

4. **Realiza un commit**:
   - Guarda los cambios con un commit:
     ```bash
     git commit -m "Primera versión del validador de movimiento de peones"
     ```

5. **Conecta tu proyecto local al repositorio remoto**:
   - Vuelve a GitHub y copia la URL de tu nuevo repositorio (ejemplo: `https://github.com/tu_usuario/ajedrez-peones.git`).
   - Conecta el repositorio local con el remoto:
     ```bash
     git remote add origin https://github.com/tu_usuario/ajedrez-peones.git
     ```

6. **Sube tu proyecto a GitHub**:
   - Empuja (push) tus cambios al repositorio en GitHub:
     ```bash
     git push -u origin master
     ```

¡Y listo! Ahora tu proyecto está en GitHub con un archivo **README.md** y todo el código necesario.
