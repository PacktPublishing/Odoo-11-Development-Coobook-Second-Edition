FROM debian:stable
LABEL version="1.1" \
      maintainer="Alexandre Fayolle <alexandre.fayolle@camptocamp.com>" \
      description="Example docker image for the bookshelf project"

CMD ["/srv/odoo/bin/odoo"]
ENV ODOO_ADDONS_PATH="src/odoo/odoo/addons,src/odoo/addons,local/" \
    ODOO_DB_HOST=odoo \
    ODOO_DB_NAME=odoodb \
    ODOO_DB_filter=odoodb$ \
    ODOO_LIST_DB=False \
    ODOO_DB_USER=odoo \
    ODOO_DB_PASSWORD=odoo \
    ODOO_DB_PORT=5432 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8
 
VOLUME ["/filestore"]

WORKDIR /srv/odoo


COPY src/odoo/requirements.txt /srv/odoo/src/odoo/

RUN mkdir local bin \
    && \
    apt-get update \
    && \
    apt-get install -y \
         fontconfig \
         libfreetype6 \
         libx11-6 \
         libxext6 \
         libxrender1 \
         node-clean-css \
         node-less \
         python3-pip \
         virtualenv \
         python3.5 \
         wget \
         xfonts-75dpi \
         xfonts-base \
         xz-utils \
         zlib1g \
    && \
    apt-get install -y \
         gcc \
         libevent-dev \
         libjpeg-dev \
         libldap2-dev \
         libpng-dev \
         libpq-dev \
         libsasl2-dev \
         libxml2-dev \
         libxslt1-dev \
         python3.5-dev \
    && \
    pip3 install --no-cache-dir -r src/odoo/requirements.txt \
    && \
    apt-get remove --purge --autoremove -y \
         gcc \
         g++ \
    && \
    wget -qO wkhtmltox.tar.xz https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && \
    tar -xf wkhtmltox.tar.xz \
    && \
    install wkhtmltox/lib/* /usr/lib \
    && \
    install wkhtmltox/bin/* /usr/bin \
    && \
    rm -rf wkhtmltox wkhtmltox.tar.xz \
    && \
    apt-get remove --purge -y \
         libevent-dev \
         libjpeg-dev \
         libldap2-dev \
         libpng-dev \
         libpq-dev \
         libsasl2-dev \
         libxml2-dev \
         libxslt1-dev \
         python3.5-dev \
         wget \
         xz-utils\
    && \
    apt-get clean \
    ;

COPY . /srv/odoo
RUN mv bin/docker-entrypoint.sh bin/odoo
