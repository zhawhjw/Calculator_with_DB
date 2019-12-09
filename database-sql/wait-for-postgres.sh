#!/bin/sh
# wait-for-postgres.sh

set -e

#host="localhost:54320"
shift
cmd="$@"

until PGPASSWORD=pass psql -h "db" -p 5432 -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
