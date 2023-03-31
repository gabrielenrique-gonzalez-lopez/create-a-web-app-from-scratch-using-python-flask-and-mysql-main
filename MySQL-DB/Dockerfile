FROM mysql:8.0

ENV MYSQL_DATABASE flask_blog
ENV MYSQL_USER root

ADD schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306

CMD ["mysqld"]
