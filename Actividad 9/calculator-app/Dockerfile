# Utiliza una imagen base con un servidor web para aplicaciones estáticas
FROM nginx:alpine

# Copia los archivos de la aplicación al directorio de trabajo en el contenedor
COPY ./ /usr/share/nginx/html/

# Expone el puerto 80 para el servidor web
EXPOSE 80