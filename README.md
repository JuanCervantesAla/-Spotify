# Spotify with Docker

## Description

This project is a simplified version of Spotify containerized with Docker. It allows users to:
- Play songs from a database

Built as a lightweight music player, it focuses on core functionalities while leveraging Docker for easy deployment and scalability.

### Technical Overview
- **Backend**: FastAPI for API management
- **Database**: MongoDB for storing song metadata and playlists
- **Frontend**: Web-based interface (HTML, CSS, JavaScript) for browsing and playback

## Features

- **Music Playback**: Stream songs from a predefined collection
- **Playlist Management**: Create, edit, and manage playlists
- **Dockerized**: Fully containerized for seamless setup

## Tools & Technologies

| Component         | Technology       |
|-------------------|------------------|
| Backend          | FastAPI          |
| Database         | MongoDB          |
| Containerization | Docker, Docker Compose |
| Frontend         | HTML, CSS, JavaScript |

## Prerequisites

Ensure the following are installed:
- Docker
- Docker Compose

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spotify-with-docker.git
   cd spotify-with-docker
docker-compose up --build


## Project Structure 
spotify-with-docker/
├── backend/          # FastAPI application
├── frontend/        # Static web interface
├── docker-compose.yml  # Container orchestration
└── Dockerfile       # Backend container configuration

##Images
![image](https://github.com/user-attachments/assets/d007f5f5-f479-4428-8ee1-9cb94d1a2251)
