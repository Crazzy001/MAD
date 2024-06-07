<<<<<<< HEAD
# /mnt/f/chatbot/mad-dashboard/Dockerfile
FROM node:14

RUN apt-get update && apt-get install -y \
    libxshmfence1 \
    libgbm1 \
    libnss3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

CMD ["sh", "-c", "npx electron . --no-sandbox"]
=======
# /mnt/f/chatbot/mad-dashboard/Dockerfile
FROM node:14

RUN apt-get update && apt-get install -y \
    libxshmfence1 \
    libgbm1 \
    libnss3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

CMD ["sh", "-c", "npx electron . --no-sandbox"]
>>>>>>> origin/main
