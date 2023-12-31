# `famedly.services` ansible collection

![Matrix](https://img.shields.io/matrix/ansible-famedly:matrix.org)

## Scope

This ansible collection consists of roles for various services used at famedly,
with no direct relation to any customers.

## Roles

- [`alexandrie`](roles/alexandrie/README.md): deploys [alexandrie](https://hirevo.github.io/alexandrie/introduction.html),
  a crate registry (for rust) which is selfhosted and features local and external
  user authentication, aswell as a rich API and an optional web frontend.
- [`vaultwarden`](roles/vaultwarden/README.md): role for deploying [vaultwarden](https://github.com/dani-garcia/vaultwarden)
  (formerly known as `bitwarden_rs`), a bitwarden compatible server, deployed using a docker container.
- [`hedgedoc`](roles/hedgedoc/README.md): deploys [hedgedoc](https://hedgedoc.org/) (formerly known as `CodiMD`),
  a polished and modern alternative to etherpad & co.
- [`ktra`](roles/ktra/README.md): a role for [ktra](https://book.ktra.dev/), a little self hostable cargo crate registry
- [`matomo`](roles/matomo/README.md): role for [matomo](https://matomo.org/) (formerly known as piwik), a web analytics tool
- [`murmur`](roles/murmur/README.md): deploys [murmur](https://www.mumble.info/downloads/), the mumble server software.
- [`snipe-it`](roles/snipe-it/README.md): used for deploying [SnipeIt](https://snipeitapp.com/), an open-source asset management.

## License

[AGPL-3.0-only](LICENSE.md)

## Authors

- Jadyn Emma Jäger <jadyn@jadyn.dev>
- Jan Christian Grünhage <jan.christian@gruenhage.xyz>
- Johanna Dorothea Reichmann <transcaffeine@finallycoffee.eu>
- Vincent Wilke <v.wilke@famedly.com>
