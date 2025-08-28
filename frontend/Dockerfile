# Используем базовый образ Node.js
FROM node:18

# Указываем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями (package.json и package-lock.json)
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

RUN npm install axios

RUN npm install 

# Копируем весь код приложения
COPY . .

# Открываем порт для работы React-приложения
EXPOSE 3000

# Запускаем приложение
CMD ["npm", "start"]
