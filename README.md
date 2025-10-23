📘 DOCUMENTO TÉCNICO — HABITAI TRACKER
🧭 1. Visión General

Nombre del Proyecto: HabitAI Tracker
Descripción breve:
Aplicación web inteligente para crear, monitorear y mejorar hábitos personales mediante análisis de comportamiento y retroalimentación automatizada.

Propósito:
Ayudar a los usuarios a formar hábitos sostenibles, identificando patrones de cumplimiento y ofreciendo sugerencias basadas en sus datos.

🎯 2. Objetivos del Proyecto

Desarrollar una aplicación web fullstack con arquitectura limpia y escalable.

Permitir registro, autenticación y gestión de usuarios mediante JWT.

Ofrecer funcionalidades de seguimiento diario de hábitos.

Implementar un sistema de estadísticas y sugerencias inteligentes.

Mantener un código profesional, modular y documentado, aplicando principios SOLID y Clean Architecture.

🧩 3. Funcionalidades MVP
🧑‍💻 Usuarios

Registro y login mediante JWT.

Edición básica de perfil.

Roles: usuario y administrador.

📆 Hábitos

CRUD de hábitos (crear, ver, editar, eliminar).

Registro diario de cumplimiento (habit tracking).

Estadísticas de progreso (porcentaje, rachas, fallos).

🧠 Inteligencia

Análisis de patrones de cumplimiento (por día y categoría).

Recomendaciones personalizadas simples.

🏗️ 4. Arquitectura del Sistema
🔹 Enfoque: Clean Architecture + API REST

Separación clara entre dominio, infraestructura, presentación y servicios.

habit-tracker/
│
├── backend/
│   ├── core/                # Configuración global Django (infraestructura)
│   ├── users/               # Dominio usuarios
│   ├── habits/              # Dominio hábitos
│   ├── utils/               # Servicios comunes, repositorios y helpers
│   └── manage.py
│
├── frontend/
│   ├── src/
│   │   ├── components/      # UI reutilizable
│   │   ├── pages/           # Páginas principales (Login, Dashboard)
│   │   ├── services/        # Comunicación con API (axios/fetch)
│   │   ├── store/           # Estado global (Zustand o Redux)
│   │   └── main.jsx
│   ├── index.html
│
└── README.md

⚙️ 5. Stack Tecnológico
Área	Tecnología	Descripción
Backend	Django + Django REST Framework	API REST robusta y mantenible
Autenticación	SimpleJWT	Tokens seguros
Frontend	React + Vite	SPA moderna y rápida
Estilos	Tailwind CSS v3	Diseño limpio y modular
Estado	Zustand / Redux Toolkit	Gestión eficiente del estado
Base de datos	SQLite (local) → PostgreSQL (producción)	Almacenamiento relacional
No relacional (futuro)	MongoDB / Firebase	Análisis flexible
Despliegue (futuro)	Render / AWS / Docker	Entorno cloud
🧱 6. Modelado inicial de datos
User
Campo	Tipo	Descripción
id	Auto	Identificador único
username	CharField	Nombre de usuario
email	EmailField	Correo único
date_of_birth	DateField	Fecha de nacimiento
password	CharField	Encriptada
Habit
Campo	Tipo	Descripción
id	Auto	Identificador
user	ForeignKey(User)	Usuario dueño
name	CharField	Nombre del hábito
description	TextField	Descripción opcional
category	CharField	Salud, Productividad, etc.
created_at	DateTime	Fecha de creación
HabitCompletion
Campo	Tipo	Descripción
id	Auto	Identificador
habit	ForeignKey(Habit)	Hábito asociado
date	Date	Día completado
completed	Boolean	Estado de cumplimiento
🧠 7. Patrones y Principios
Enfoque	Aplicación
Clean Code	Código legible, modular y con responsabilidades únicas
SOLID	Clases desacopladas, fácil extensión
Repository Pattern	Lógica de acceso a datos separada del dominio
Service Layer	Reglas de negocio fuera de vistas y modelos
DRY / KISS	Evitar duplicidad, mantenerlo simple
Dependency Injection (básico)	Servicios y repositorios desacoplados
🧰 8. Endpoints principales (fase 1)
Método	Ruta	Descripción
POST	/api/users/register/	Registro de usuario
POST	/api/token/	Obtener JWT
GET	/api/habits/	Listar hábitos
POST	/api/habits/	Crear hábito
PATCH	/api/habits/:id/	Actualizar hábito
POST	/api/habits/:id/complete/	Registrar cumplimiento
🧭 9. Flujo del usuario

Registro / Login: el usuario se autentica con JWT.

Dashboard: ve sus hábitos y progreso diario.

Tracking: marca hábitos como completados.

Análisis: el sistema genera estadísticas simples y sugerencias.

Feedback: el usuario ajusta su rutina.

🔮 10. Roadmap Futuro
Etapa	Mejora
Fase 2	Integrar IA ligera para detección de patrones
Fase 3	Notificaciones automáticas vía correo / push
Fase 4	Integración con Google Calendar / Notion API
Fase 5	Migración a nube (Docker + AWS + CI/CD)
🧩 11. Guía de instalación (para desarrolladores)
# Clonar repositorio
git clone https://github.com/usuario/habitai-tracker.git
cd habitai-tracker

# Backend
cd backend
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend
cd ../frontend
npm install
npm run dev

🧑‍💻 12. Equipo y roles (simulado para portafolio)
Rol	Nombre	Responsabilidad
Product Owner	—	Define visión y backlog
Fullstack Developer	Luis Eduardo Huancas Montero	Arquitectura, backend, frontend y despliegue
QA / Tester	—	Pruebas unitarias y API
UX Designer	—	Diseño de interfaz y experiencia
