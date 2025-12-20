# 🤖 Talia Bot: Asistente Personal & Orquestador de Negocio

Talia no es un simple chatbot; es un Middleware de Inteligencia Artificial que orquesta las operaciones diarias de administración, logística y ventas. Actúa como el puente central entre usuarios en Telegram y servicios críticos como Vikunja (Gestión de Proyectos), Google Calendar y Hardware de Impresión remota.

---

## 🚀 Conceptos Centrales

### 1. Enrutamiento por Identidad

La característica core de Talia es su capacidad de cambiar de personalidad y permisos dinámicamente basándose en el Telegram ID del usuario:

| Rol     | Icono | Descripción         | Permisos                                                                          |
| :------ | :---: | :------------------ | :-------------------------------------------------------------------------------- |
| **Admin** |  👑   | Dueño / Gerente     | God Mode: Gestión total de proyectos, bloqueos de calendario, generación de identidad NFC e impresión. |
| **Crew**  |  👷   | Equipo Operativo    | Limitado: Solicitud de agenda (validada), asignación de tareas, impresión de documentos. |
| **Cliente** |  👤   | Usuario Público     | Ventas: Embudo de captación, consulta de servicios (RAG) y agendamiento comercial. |

### 2. Motor de Flujos Conversacionales

Toda la lógica de conversación del bot es impulsada por un motor de flujos genérico. En lugar de tener conversaciones codificadas, el bot interpreta definiciones de un archivo central `flows.json`.

*   **`main.py`**: Contiene un `universal_handler` que captura todas las interacciones del usuario.
*   **`flow_engine.py`**: Es el cerebro. Consulta el estado actual del usuario en la base de datos, lee el `flows.json` para determinar el siguiente paso y maneja la lógica de la conversación.
*   **`flows.json`**: Un archivo JSON que define cada pregunta, botón y acción para todos los flujos de conversación, separados por rol. Esto permite modificar o añadir nuevas conversaciones sin cambiar el código principal.

---

## 🛠️ Arquitectura Técnica

El sistema sigue un flujo modular:

1.  **Input**: Telegram (Texto, Audio, Documentos, Botones).
2.  **Transcripción**: `transcription.py` (Whisper) convierte voz a texto.
3.  **Router**: `universal_handler` en `main.py` enruta la entrada al `FlowEngine`.
4.  **Estado**: El `FlowEngine` consulta la tabla `conversations` en la base de datos para saber si el usuario está en medio de un flujo.
5.  **Lógica**: El `FlowEngine` utiliza `flows.json` para procesar la entrada, recoger datos y determinar el siguiente paso.
6.  **Resolución**: Una vez que un flujo se completa, `main.py` ejecuta la acción final (la "resolución") llamando al módulo correspondiente.
7.  **Módulos de Acción (Tools)**:
    *   **`vikunja.py`**: API asíncrona para leer/escribir tareas y proyectos.
    *   **`calendar.py`**: API para crear eventos en Google Calendar.
    *   **`mailer.py`**: Envío de correos (SMTP) para el flujo de impresión.
    *   **`llm_engine.py`**: Análisis RAG para el embudo de ventas.

---

## ⚙️ Instalación y Configuración

### Prerrequisitos

*   Python 3.9+
*   Docker y Docker Compose (recomendado)
*   Cuenta de Telegram Bot (@BotFather)
*   Instancia de Vikunja (Self-hosted)
*   Cuenta de Servicio Google Cloud (Calendar API)
*   Servidor de Correo (SMTP/IMAP)

### 1. Clonar y Entorno

```bash
git clone https://github.com/marcogll/talia_bot_mg.git
cd talia_bot_mg
```

### 2. Variables de Entorno (`.env`)

Crea un archivo `.env` en la raíz del proyecto a partir de `.env.example` y rellena las siguientes variables:

```env
# --- TELEGRAM & SECURITY ---
TELEGRAM_BOT_TOKEN=tu_token_telegram
ADMIN_ID=tu_telegram_id

# --- AI CORE ---
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-3.5-turbo

# --- INTEGRACIONES ---
VIKUNJA_BASE_URL=https://tu_vikunja.com/api/v1
VIKUNJA_TOKEN=tu_token_vikunja
VIKUNJA_INBOX_PROJECT_ID=el_id_de_tu_proyecto_bandeja_de_entrada
GOOGLE_SERVICE_ACCOUNT_FILE=google_key.json
CALENDAR_ID=tu_id_de_google_calendar

# --- PRINT SERVICE ---
SMTP_SERVER=smtp.tuservidor.com
SMTP_PORT=587
SMTP_USER=tu_usuario_smtp
SMTP_PASSWORD=tu_password_smtp
IMAP_SERVER=imap.tuservidor.com
IMAP_USER=tu_usuario_imap
IMAP_PASSWORD=tu_password_imap
PRINTER_EMAIL=el_email_de_la_impresora
```

### 3. Ejecutar con Docker

La forma más sencilla de levantar el bot es con Docker Compose:

```bash
docker-compose up --build
```

---

## 📂 Estructura del Proyecto

```text
talia_bot_mg/
├── talia_bot/
│   ├── main.py              # Entry Point y Universal Handler
│   ├── db.py                # Gestión de la base de datos (SQLite)
│   ├── config.py            # Carga de variables de entorno
│   ├── modules/
│   │   ├── flow_engine.py   # El cerebro que procesa los flujos
│   │   ├── vikunja.py       # API Manager asíncrono para Tareas
│   │   ├── calendar.py      # Lógica de Google Calendar
│   │   ├── llm_engine.py    # Cliente OpenAI (Whisper y GPT)
│   │   ├── transcription.py # Lógica de transcripción de audio
│   │   ├── mailer.py        # Módulo para envío de correos (SMTP)
│   │   └── ...              # Otros módulos de soporte
│   └── data/
│       ├── flows.json       # ¡IMPORTANTE! Define todas las conversaciones
│       ├── services.json    # Base de conocimiento para ventas
│       └── users.db         # Base de datos de usuarios
├── .env                     # Tus variables de entorno (NO subir a Git)
├── .env.example             # Plantilla de variables de entorno
├── requirements.txt         # Dependencias de Python
├── Dockerfile               # Configuración del contenedor
└── docker-compose.yml       # Orquestador de Docker
```

---

## 🗓️ Roadmap

- [x] **Implementado el Motor de Flujos Conversacionales.**
- [x] **Integración completa de Vikunja, OpenAI y Google Calendar.**
- [ ] Implementar el loop de confirmación de impresión (IMAP Listener).
- [ ] Mejorar el parsing de fechas y horas con lenguaje natural más avanzado.
- [ ] Migrar de OpenAI a Google Gemini 1.5 Pro.

---

Desarrollado por: Marco G.
Asistente Personalizado v2.0 (Arquitectura de Flujos)
