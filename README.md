# KPI Backend - Project & KPI Management System

A Django REST API for managing projects and tracking Key Performance Indicators (KPIs) with flexible, database-driven KPI definitions.

## Table of Contents
- [Objective](#objective)
- [Scope](#scope)
- [Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Assumptions](#assumptions)
- [Key Design Decisions](#key-design-decisions)
- [Trade-offs](#trade-offs)
- [Future Improvements](#future-improvements)

---

## Objective

Build a simple system to manage projects and track KPIs with the ability to flexibly define and monitor performance metrics across projects.

---

## Scope

### Core Features
1. **Create and list projects** with metadata (name, description, owner)
2. **Add KPIs to projects** with flexible definition
3. **KPIs must be flexible** - not hardcoded, fully customizable
4. **View projects with KPI summary** - see all KPIs for a project at once
5. **View and update KPIs** within a project context

---

## Features

✅ **Project Management**
- Create, read, update, delete projects
- Track project metadata (name, description, owner, creation date)
- View all KPIs associated with a project

✅ **KPI Management**
- Create, read, update, delete KPIs
- Flexible KPI definition (name, target value, actual value, status)
- KPI status tracking (ON_TRACK, AT_RISK, OFF_TRACK)
- Link KPIs to specific projects

✅ **API Documentation**
- Swagger UI for interactive API exploration
- ReDoc for alternative documentation view
- OpenAPI 3.0 schema support

---

## Installation

### Prerequisites
- Python 3.8+
- Django 4.2+
- Django REST Framework
- drf-spectacular (for Swagger)



## Run with Docker

### Start Application

```bash
docker compose up --build

After this command, the API will be available at http://localhost:8000/ and the Swagger UI documentation at http://localhost:8000/.


