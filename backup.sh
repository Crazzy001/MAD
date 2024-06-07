#!/bin/bash

# Stopping Docker containers
docker-compose down

# Backing up Docker volumes
docker run --rm --volumes-from chatbot_backend_1 -v $(pwd):/backup ubuntu tar cvf /backup/backend_volume_backup.tar /app
docker run --rm --volumes-from chatbot_mad-dashboard_1 -v $(pwd):/backup ubuntu tar cvf /backup/mad_dashboard_volume_backup.tar /app

# Backing up Docker images
docker save -o chatbot_backend_image.tar chatbot_backend
docker save -o chatbot_mad_dashboard_image.tar chatbot_mad-dashboard

# Backing up project files
zip -r chatbot_project_files_backup.zip backend/ mad-dashboard/ docker-compose.yml Dockerfile requirements.txt package.json

# Creating a full backup archive
tar cvf chatbot_full_backup.tar chatbot_project_files_backup.zip backend_volume_backup.tar mad_dashboard_volume_backup.tar chatbot_backend_image.tar chatbot_mad_dashboard_image.tar

echo "Backup completed successfully."
