FROM mysql:8.0

ENV MYSQL_DATABASE PFG-BLOG
ENV MYSQL_USER python-blog
ENV MYSQL_PASSWORD PfGpAs5

ADD schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306

CMD ["mysqld"]
