# **Avance 2 - Herramientas de Desarrollo - Mininet y GitHub**

Esta actividad involucra el uso de diversas herramientas y/o plataformas: Máquinas virtuales, 
Github, Programación en Python, Comandos Linux, etc.
Se tiene como finalidad ejecutar y documentar diferentes topologías de red usando el entorno **Mininet**, así como gestionar versiones y colaboración a través de **GitHub**.

---

## 📌 Objetivos del Proyecto

- Explorar el uso del simulador de redes **Mininet**.
- Implementar diferentes topologías de red (árbol, lineal, torus).
- Documentar resultados visuales (topologías generadas).
- Aplicar buenas prácticas de **control de versiones** usando Git y GitHub.
- Fomentar el trabajo colaborativo en ramas y gestión de *pull requests*.

---

## ⚙️ Requisitos previos

-  Máquina virtual Ubuntu instalada y configurada.
-  Mininet instalado (`sudo apt install mininet`).
-  Cuenta en GitHub activa.
-  Git instalado en Ubuntu (`sudo apt install git`).

---

## 🖥️ Comandos ejecutados en Mininet

### 🌳 1. Topología Árbol

Se genera una topología jerárquica con 4 niveles de profundidad y un fanout de 3. En el cual cada switch se conecta a 3 nodos hijos.
> Switches: 40
> Hosts: 81
> Enlaces: 120

```bash
sudo mn --topo tree,4,3
```

📸 Simulación grafica de la topología:

![Sin título](https://github.com/user-attachments/assets/985dfb14-06b1-4dec-9f01-3114955dd541)

### 📏​ 2. Topología Lineal

Se genera una cadena lineal de 5 switches, donde cada uno tiene 4 hosts conectados.
> Switches: 5
> Hosts: 20
> Enlaces: 24

```bash
sudo mn --topo linear,5,4
```

📸 Simulación grafica de la topología:

![linear-v0](https://github.com/user-attachments/assets/b46d9fc5-453d-49ae-88e7-58604b615f6c)

### 🧊 3. Topología Torus

Se genera una topologia tridimensional tipo torus con dimensiones 3x4x5. En el cual se conectas switches en un espacio de malla.
> Switches: 12
> Hosts: 60
> Enlaces: 94

```bash
sudo mn --topo torus,3,4,5
```

📸 Simulación grafica de la topología:
![torus-v0](https://github.com/user-attachments/assets/93222dba-de5b-4d27-96bc-3a46ac545241)

### 🔀 Control de versiones y ramas

> - main: Rama principal (versión base del proyecto).

> - rama-gonzalo: Rama para pruebas y documentación de la topología torus.

> - rama-antony: Rama para pruebas y documentación de la topología arbol.

### ✔️ Pull Request

Se creó un pull request desde la rama rama-gonzalo hacia main.


### 👥 Integrantes del Equipo

| Nombre completo  | Usuario | 
| ---------------- | -------------- | 
| Cabrera Luey, Leslie Liliana | [@lesssC](https://github.com/lesssC)  |
| Quispe Ponte, Antony Luis     | [@tony270604](https://github.com/tony270604) |
| Lozano Santos, Gonzalo    | [@Gonzalx-L](https://github.com/Gonzalx-L) |
