# Student Management System API

This is a simple **Student Management System** API built using FastAPI. It provides basic CRUD (Create, Read, Update, Delete) operations for managing student information.

## Features

- Get all student information
- Get information for a specific student by student ID
- Add new student information
- Modify existing student information
- Delete student information

## Table Schema

The student data is stored in a table named `stud` with the following schema:

```
## Table Schema

| Column  | Data Type | Description                      |
|---------|-----------|----------------------------------|
| id      | Integer   | Primary key, auto-incremented    |
| name    | String    | Student name, nullable           |
| email   | String    | Student email, nullable          |
| address | String    | Student address, nullable        |
| marks   | Float     | Student marks, nullable          |

```
