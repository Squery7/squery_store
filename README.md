<!-- # squery_store -->
<!-- Creación de una tienda utilizando el framework django -->
Squery Store
============

> # Hola 
> 
> - Consultas SQL 
>
> *Everything* is "***possible***".

<!-- Centrar una tabla con lenguaje markdown -->

| Nombre      | Apellido    |
|:-----------:|:-----------:|
| Diego       | Robles      |

# Consultas SQL

### En vez de hacer esto:

```sql
SELECT DISTINCT CITY FROM STATION
WHERE 
LOWER(CITY) LIKE 'a%' OR 
LOWER(CITY) LIKE 'e%' OR 
LOWER(CITY) LIKE 'i%' OR
LOWER(CITY) LIKE 'o%' OR 
LOWER(CITY) LIKE 'u%';
```

### Haz esto:
```sql
SELECT DISTINCT CITY FROM STATION
WHERE LOWER(CITY) REGEXP '^[aeiou]';
```

### Y en vez de hacer esto:
```sql
SELECT DISTINCT first_name FROM actor
WHERE 
LOWER(first_name) LIKE '%a' OR 
LOWER(first_name) LIKE '%e' OR 
LOWER(first_name) LIKE '%i' OR
LOWER(first_name) LIKE '%o' OR 
LOWER(first_name) LIKE '%u';
```

### Haz esto: 
```sql
SELECT DISTINCT CITY FROM STATION
WHERE LOWER(CITY) REGEXP '[aeiou]$';
```