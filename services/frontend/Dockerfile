FROM nginx:alpine

# Копируем наш кастомный конфиг Nginx
COPY default.conf /etc/nginx/conf.d/default.conf

# Копируем HTML-страницу
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80