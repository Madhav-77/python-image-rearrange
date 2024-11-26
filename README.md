# Starlette Python Rearrange app API

A Python backend built using Starlette to manage image data and positions, with PostgreSQL as the database. This API supports retrieving and updating image data with middleware for handling unknown routes and CORS.

## Table of Contents
- [Project Overview](#project-overview)
- [Project setup](#setting-up-the-project)
- [API Endpoints](#api-endpoints)
- [Database Information](#database-information)
- [Contributors](#contributors)

## Project Overview

This project is a RESTful API backend built with Python's Starlette framework. It connects to a PostgreSQL database to retrieve and update image data, handling features like image positioning. The API includes robust middleware for handling unknown routes and CORS-related requests, ensuring smooth integration with frontend applications.

[![Version](https://img.shields.io/badge/version-1.0.0.alpha.1-blue.svg)](https://semver.org)

### Key Features:
- Retrieve image data from the database.
- Update and save image positions in PostgreSQL.
- Middleware for:
    - Handling unknown routes with custom 404 responses.
    - CORS (Cross-Origin Resource Sharing) to allow cross-origin API requests.
- Scalable and lightweight

---

## Setting Up the Project

### Tech stack
- **Backend Framework**: Starlette
- **Database**: PostgreSQL
- **Language**: Python
- **Middleware**: Custom middlewares for 404 handling and CORS.
- **Deployment**: Vercel

### Installation
**Prerequisites**:
- Python 3.9+
- PostgreSQL installed and running (17.2)

**Clone the repository**:

    git clone https://github.com/Madhav-77/python-image-rearrange.git
    
**Create a Virtual Environment**:
    
    python3 -m venv venv
    use venv\Scripts\activate # For Windows
    
**Install Dependencies**:

    pip install -r requirements.txt

**Set up the PostgreSQL database and configure the connection string.**

**Environment Variables**:

Create a .env file in the root directory and define the following:

    DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database_name>

**Run the Development Server**:

    uvicorn app.main:app --reload

---
## API Endpoints

| Method | Endpoint                                     | Description                                    | Example Request                           |
|--------|----------------------------------------------|------------------------------------------------|------------------------------------------|
| GET    | `/api/images/get`                            | Retrieve all images                            | `GET /api/images/get`                    |
| PATCH  | `/api/images/update`                         | Updates the position of images                 | `PATCH /api/images/update`               |

### Request and Response Details

#### 1. Retrieve All Image data (GET `/api/images/get`)
- **Request Example**:
    ```bash
    GET /api/images/get
    ```
- **Response Example**:
    ```json
    [
      {
        "id": 1,
        "type": "bank-draft",
        "title": "Bank Draft",
        "position": 0
      },
      {
        "id": 2,
        "type": "bill-of-lading",
        "title": "Bill of Lading",
        "position": 1
      }
    ]
    ```

#### 2. Update image positions (PATCH `/api/images/update`)
- **Request Example**:
    ```bash
    PATCH /api/images/update
    Content-Type: application/json

    [
      {
        "id": 1,
        "type": "bank-draft",
        "title": "Bank Draft",
        "position": 1
      },
      {
        "id": 2,
        "type": "bill-of-lading",
        "title": "Bill of Lading",
        "position": 0
      }
    ]
    ```
- **Response Example**:
    ```json
    [
      {
        "id": 1,
        "type": "bank-draft",
        "title": "Bank Draft",
        "position": 1
      },
      {
        "id": 2,
        "type": "bill-of-lading",
        "title": "Bill of Lading",
        "position": 0
      }
    ]
    ```
---

## Database Information

### Database Schema

The following table is defined in the database schema for the Rearrange application:

- **image_data**: Stores image data and positions.
    - `id` (SERIAL, Primary Key): Unique identifier for each image.
    - `type` (TEXT): The name of the file.
    - `title` (TEXT): The display name of the image.
    - `position` (INTEGER): The position of the image in the grid.

## Contributors

- [@madhavtrivedi](https://www.madhavtrivedi.com/)