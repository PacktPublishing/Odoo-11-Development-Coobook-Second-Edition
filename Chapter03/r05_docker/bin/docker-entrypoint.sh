#!/bin/bash
ODOO=/srv/odoo/src/odoo/odoo-bin

echo "$@"

$ODOO --addons-path="$ODOO_ADDONS_PATH" \
      -d "$ODOO_DB_NAME" \
      --db_host="$ODOO_DB_HOST" \
      --db_user="$ODOO_DB_USER" \
      --db_password="$ODOO_DB_PASSWORD" \
      --no-database-list \
      --db-filter="$ODOO_DB_FILTER" \
      --db_port="$ODOO_DB_PORT" \
      --data-dir=/filestore "$@"
