###
### Copy createdb.sql.example to createdb.sql
### then uncomment then set database name and username to create you need databases
#
# example: .env MYSQL_USER=appuser and need db name is myshop_db
#
    CREATE DATABASE IF NOT EXISTS `nextcloud` ;
    GRANT ALL ON `nextcloud`.* TO 'nextuser'@'%' ;

    CREATE DATABASE IF NOT EXISTS `gitea`;
    GRANT ALL ON `gitea`.* TO 'nextuser'@'%' ;
#
###
### this sql script is auto run when mariadb container start and $DATA_PATH_HOST/mariadb not exists.
###
### if your $DATA_PATH_HOST/mariadb is exists and you do not want to delete it, you can run by manual execution:
###
###     docker-compose exec mariadb bash
###     mysql -u root -p < /docker-entrypoint-initdb.d/createdb.sql
###

#CREATE DATABASE IF NOT EXISTS `dev_db_2` COLLATE 'utf8_general_ci' ;
#GRANT ALL ON `dev_db_2`.* TO 'default'@'%' ;

#CREATE DATABASE IF NOT EXISTS `dev_db_3` COLLATE 'utf8_general_ci' ;
#GRANT ALL ON `dev_db_3`.* TO 'default'@'%' ;

FLUSH PRIVILEGES ;
