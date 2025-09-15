# 🛒 Pipeline de Ventas con Fake Store API → PostgreSQL + Visualización

Este proyecto implementa un pipeline **ETL completo** que extrae datos de la [Fake Store API](https://fakestoreapi.com/), 
los transforma y los carga en una base de datos PostgreSQL. 
Finalmente, se generan **dashboards interactivos en Power BI/Tableau** con KPIs de negocio.

## 🎯 Objetivos
- Construir un pipeline ETL reproducible y automatizable.
- Estructurar los datos en un esquema estrella (fact_sales, dim_customers, dim_products).
- Proveer dashboards con KPIs clave de negocio: ingresos, ticket medio, top clientes y productos.

## ⚙️ Arquitectura
![ETL Pipeline](docs/arquitectura.png)

## 📊 Ejemplo de KPIs
- Ventas totales por mes
- Ticket medio por cliente
- Top 5 productos más vendidos
- Distribución de ventas por categoría
