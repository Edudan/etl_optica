

📊 Proyecto ETL Óptica

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) sencillo para manejar datos de ventas de una óptica usando Python, Pandas y SQLite.
La idea es simular un flujo real de datos: extraer de un archivo CSV, transformar y limpiar la información, y cargarla en una base de datos relacional.

⸻

🚀 Estructura del proyecto

etl_optica/
│
├── etl/               # Módulos ETL
│   ├── extract.py     # Lectura de datos CSV
│   ├── transform.py   # Limpieza y transformaciones
│   ├── load.py        # Carga en SQLite
│   ├── config.py      # Configuración de rutas (CSV y DB)
│
├── data/              # Archivos de datos (ignorado en GitHub)
│   └── .gitkeep
│
├── main.py            # Orquestador ETL
├── requirements.txt   # Dependencias del proyecto
├── .gitignore         # Archivos y carpetas ignorados
└── README.md          # Documentación


⸻

⚙️ Requisitos
	•	Python 3.9+
	•	Pandas
	•	SQLite3 (ya viene instalado con Python)

Instalar dependencias:

pip install -r requirements.txt


⸻

▶️ Ejecución

Para correr el pipeline ETL completo:

python main.py

Flujo:
	1.	Extract → Lee el archivo CSV de ventas desde la ruta en config.py.
	2.	Transform → Limpia duplicados, rellena valores nulos, corrige tipos de datos, recalcula totales e IVA.
	3.	Load → Carga los datos procesados en una base de datos SQLite (optica.db) en la tabla ventas.

⸻

📂 Ejemplo de datos (CSV original)

id,cliente,producto,precio,cantidad,total
1,Juan,Lente A,500,2,1000
2,Ana,Armazón X,300,1,300
3,Carlos,Lente B,700,1,700


⸻

📂 Datos transformados (ya en SQLite)

id	cliente	producto	precio	cantidad	total	iva
1	Juan	Lente A	500	2	1000	160
2	Ana	Armazón X	300	1	300	48
3	Carlos	Lente B	700	1	700	112


⸻

🔎 Consultas útiles en SQLite

Una vez cargados los datos en optica.db, puedes abrir la BD en DB Browser o con sqlite3 y ejecutar:

Total de ventas por cliente

SELECT cliente, SUM(total) AS total_vendido
FROM ventas
GROUP BY cliente
ORDER BY total_vendido DESC;

Producto más vendido

SELECT producto, SUM(cantidad) AS cantidad_vendida
FROM ventas
GROUP BY producto
ORDER BY cantidad_vendida DESC;

Total de IVA generado

SELECT SUM(iva) AS iva_total FROM ventas;


⸻

✨ Próximos pasos
	•	Conectar este pipeline a datos reales (APIs o logs).
	•	Migrar de SQLite a PostgreSQL/MySQL para ambientes productivos.
	•	Automatizar la ejecución con cron jobs o Airflow.

