#!/bin/bash

export PGPASSWORD=$POSTGRES_PASSWORD

SQL_COUNT_ALL_DB="SELECT count(*) FROM pg_database where datname in ('$POSTGRES_DB','$PYCOOK_DB')"
PSQLCom="psql --host 127.0.0.1 -U $POSTGRES_USER -d $POSTGRES_DB -t -c"

#execute un sql select
execSqlSelect () {
  pDB=$1    #nom de la database
  pSQL=$2  #commande SQL a executer

  vCom="$PSQLCom \"$pSQL\""
  res=$($PSQLCom "$pSQL")
  res=$(echo "$res" | xargs) #trim whitespace
  echo  "$(date) Execute select: $vCom -----> $res"
}

addDatabase(){
  pDBtoAdd=$1    #nom de la database
  pUsername=$2  #nom de l'utilisateur de la BDD
  pPassword=$3  #mot de passe de l'utilisateur de la BDD

  vSQL_COUNT_DB="SELECT count(*) FROM pg_database where datname in ('$pDBtoAdd')"
  execSqlSelect "$POSTGRES_DB" "$vSQL_COUNT_DB"
  toInt "$res"
  nbDb=$res
  if [ "$nbDb" == "0" ]; then
    echo echo  "$(date) The database '$pDBtoAdd' doesn't exist -> so create it"
    vSQL1="CREATE ROLE \"$pUsername\" WITH LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT -1 PASSWORD '$pPassword'"
    vSQL2="CREATE DATABASE \"$pDBtoAdd\" WITH OWNER = \"$pUsername\" ENCODING = 'UTF8' CONNECTION LIMIT = -1"

    execSqlSelect "$POSTGRES_DB" "$vSQL1"
    execSqlSelect "$POSTGRES_DB" "$vSQL2"

  else
    echo echo  "$(date) The database '$pDBtoAdd' already exist"
  fi

}

toInt(){
  var=$1
  set /a var=%var% + 0
}

execSqlSelect "$POSTGRES_DB" "$SQL_COUNT_ALL_DB"
toInt "$res"
nbDb=$res

if [ "$nbDb" == "2" ]; then
  echo echo  "$(date) The number of databases is good : 2 -> exit 0"
else
  echo echo  "$(date) The number of databases is WRONG : $nbDb!=2 -> try to add databases"
  addDatabase $PYCOOK_DB $PYCOOK_USER $PYCOOK_PASSWORD
fi

execSqlSelect "$POSTGRES_DB" "$SQL_COUNT_ALL_DB"
toInt "$res"
nbDb=$res
if [ "$nbDb" == "2" ]; then
  echo echo  "$(date) The number of databases is good : 2 -> exit 0"
  exit 0
else
  echo echo  "$(date) ERROR The number of databases is wrong a database has to be in error -> exit 1"
  exit 1
fi
