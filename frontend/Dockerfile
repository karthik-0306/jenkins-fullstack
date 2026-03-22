# Use Nginx to serve the dark-themed HTML
FROM nginx:alpine

# Copy your index.html to the Nginx public folder
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 (Standard for Nginx)
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]