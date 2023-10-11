docker-compose up -d postgres
export DATABASE_URL=postgres://postgres:postgres@`docker-compose port postgres 5432`
echo $DATABASE_URL
export DJANGO_SETTINGS_MODULE=devproject.test_settings
export POSTGRES_DB=misago
export POSTGRES_USER=misago
export POSTGRES_PASSWORD=misago
export POSTGRES_HOST=localhost