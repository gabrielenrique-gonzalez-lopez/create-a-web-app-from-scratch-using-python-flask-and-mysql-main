FROM mysql:8.0.32

#ENV MYSQL_DATABASE flask_blog

EXPOSE 3306

COPY schema.sql /docker-entrypoint-initdb.d

