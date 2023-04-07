FROM mysql:5.7

#ENV MYSQL_DATABASE flask_blog

RUN rm -rf /var/lib/mysql/*
RUN mkdir -p /var/lib/mysql

ADD schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306

CMD ["mysqld"]
