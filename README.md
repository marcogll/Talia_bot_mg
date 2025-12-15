# Talía — Asistente Ejecutiva Inteligente

Talía es una asistente ejecutiva digital diseñada para centralizar, ordenar y coordinar la agenda, solicitudes y actividades de Marco. Funciona como un **punto único de entrada** para clientes, equipo y administradores, asegurando que cada solicitud se procese con contexto, validación y respeto por el tiempo disponible.

Talía no improvisa ni asume. **Consulta, valida, confirma y ejecuta.**

---

## 🎯 Propósito del Sistema

Talía existe para eliminar fricción operativa y proteger el tiempo ejecutivo. El sistema está diseñado para:

* Centralizar todas las solicitudes de agenda, citas y actividades
* Validar disponibilidad real antes de comprometer tiempo
* Priorizar clientes sin romper compromisos existentes
* Delegar reglas de negocio y disponibilidad a flujos en n8n
* Mantener trazabilidad completa mediante eventos webhook
* Escalar de forma modular sin romper flujos existentes

---

## 🧠 Personalidad, Actitud y Voz

Talía se comporta como una asistente ejecutiva profesional:

* Educada, clara y precisa en cada respuesta
* Proactiva, pero nunca invasiva
* Siempre confirma antes de agendar o ejecutar acciones
* No improvisa horarios ni decisiones
* Comunica decisiones con calma, orden y neutralidad

Talía no es informal, no es robótica y no utiliza sarcasmo. Su función es **ordenar el día, no interrumpirlo**.

---

## 👥 Roles y Niveles de Acceso

### Marco (Owner)

* Consulta agenda, pendientes y solicitudes activas
* Recibe resumen diario automático a las 7:00 AM
* Aprueba o rechaza solicitudes del equipo
* Puede interactuar desde su número privado
* Tiene prioridad absoluta sobre cualquier decisión

### Clientes

* Solicitan citas de duración fija (30 minutos)
* Visualizan únicamente horarios disponibles
* No tienen acceso a la agenda completa

### Equipo Autorizado

* Puede proponer actividades de mayor duración (ej. grabaciones)
* Puede solicitar acciones operativas
* Toda actividad que consuma tiempo requiere aprobación

### Administradores

* Ejecutan acciones sensibles
* Requieren validación adicional
* Acceden a flujos administrativos restringidos

---

## 🏗️ Arquitectura del Sistema

Talía está construida en capas desacopladas que se comunican por eventos:

1. **Interfaz Conversacional** – Telegram / WhatsApp
2. **Cerebro Central** – Python
3. **Automatización y Reglas** – n8n
4. **Servicios Externos** – Google Calendar, IA, APIs

Cada capa es independiente y puede evolucionar sin afectar a las demás.

---

## 📁 Estructura del Proyecto

```text
talia-bot/
├── docker-compose.yml        # Orquestación de contenedores
├── Dockerfile               # Imagen del bot
├── .env.example             # Variables de entorno
├── README.md                # Documentación
└── app/
    ├── main.py              # Cerebro del bot
    ├── config.py            # Configuración y credenciales
    ├── permissions.py       # Roles y validaciones
    ├── scheduler.py         # Resumen diario y recordatorios
    ├── webhook_client.py    # Comunicación con n8n
    ├── calendar.py          # Integración Google Calendar
    ├── llm.py               # Respuestas inteligentes (IA)
    └── modules/
        ├── onboarding.py    # Bienvenida y menú inicial
        ├── agenda.py        # Consulta de agenda
        ├── citas.py         # Citas con clientes
        ├── equipo.py        # Solicitudes del equipo
        ├── aprobaciones.py  # Aprobaciones del owner
        ├── servicios.py     # Servicios y cotizaciones
        └── admin.py         # Acciones administrativas
```

---

## 🧠 Cerebro del Sistema (`main.py`)

`main.py` actúa como **orquestador central**. No contiene reglas de negocio complejas. Sus funciones son:

* Recibir mensajes y callbacks
* Identificar usuario y rol
* Mantener contexto conversacional
* Delegar acciones a módulos
* Emitir y recibir eventos vía webhook

Toda decisión importante se valida externamente.

---

## 🧩 Módulos Funcionales

Cada módulo cumple una responsabilidad única:

* **onboarding.py**: inicio de conversación y opciones
* **agenda.py**: consulta de agenda y pendientes
* **citas.py**: flujo de citas con clientes
* **equipo.py**: solicitudes internas del equipo
* **aprobaciones.py**: aceptar o rechazar solicitudes
* **servicios.py**: información y cotización de proyectos
* **admin.py**: acciones administrativas

---

## 🔁 Flujo General de Ejecución

1. Usuario envía mensaje o interactúa con botones
2. Talía valida identidad y permisos
3. Se ejecuta el módulo correspondiente
4. Si se requiere lógica externa, se envía evento a n8n
5. n8n evalúa reglas y responde
6. Talía comunica el resultado
7. Si aplica, se agenda en Google Calendar

---

## 📆 Gestión de Agenda

### Citas con Clientes

* Duración fija: 30 minutos
* Disponibilidad definida exclusivamente por n8n
* Confirmación explícita antes de agendar

### Actividades del Equipo

* Duración flexible
* Requieren aprobación del owner
* Solo usuarios autorizados pueden solicitarlas

---

## ⏰ Resumen Diario

Todos los días a las **7:00 AM**, Talía envía a Marco:

* Agenda del día
* Pendientes activos
* Recordatorios importantes

---

## 🔌 Webhooks

Toda acción relevante genera o responde un evento webhook.

Ejemplo:

```json
{
  "event": "request_activity",
  "from": "team",
  "duration_hours": 4,
  "description": "Grabación de proyecto"
}
```

---

## 🔐 Variables de Entorno

```env
TELEGRAM_BOT_TOKEN=
OWNER_CHAT_ID=
ADMIN_CHAT_IDS=
TEAM_CHAT_IDS=
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REFRESH_TOKEN=
N8N_WEBHOOK_URL=
OPENAI_API_KEY=
TIMEZONE=America/Mexico_City
```

---

## 🐳 Despliegue con Docker Compose

```yaml
version: "3.9"
services:
  talia-bot:
    build: .
    container_name: talia-bot
    env_file:
      - .env
    restart: unless-stopped
```

---

## 🛠️ Guía de Desarrollo

1. Clonar el repositorio
2. Crear archivo `.env`
3. Configurar bot de Telegram
4. Configurar flujos y reglas en n8n
5. Conectar Google Calendar
6. Levantar servicios con Docker Compose

---

## ✨ Principio Rector

Talía no es un bot que responde mensajes.
Es un sistema de criterio, orden y protección del tiempo.

Si algo no está claro, pregunta.
Si algo invade la agenda, protege.
Si algo es importante, lo prioriza.
