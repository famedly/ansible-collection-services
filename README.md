# `famedly.services` ansible collection

![Matrix](https://img.shields.io/matrix/ansible-famedly:matrix.org)

## Scope

This ansible collection consists of roles for various services used at famedly,
with no direct relation to any customers.

## Roles

- [`vaultwarden`](roles/vaultwarden/README.md): role for deploying [vaultwarden](https://github.com/dani-garcia/vaultwarden)
  (formerly known as `bitwarden_rs`), a bitwarden compatible server, deployed using a docker container.
- [`snipe-it`](roles/snipe-it/README.md): used for deploying [SnipeIt](https://snipeitapp.com/), an open-source asset management.

## License

[AGPL-3.0-only](LICENSE.md)

## Authors

- Jadyn Emma Jäger <jadyn@jadyn.dev>
- Jan Christian Grünhage <jan.christian@gruenhage.xyz>
- Johanna Dorothea Reichmann <transcaffeine@finallycoffee.eu>
- Vincent Wilke <v.wilke@famedly.com>
