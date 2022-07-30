# Telegram bio updater

## What it does

1. With a given frequency, it gets some text supplied by a [server](https://github.com/br4ch1st0chr0n3/bio-faker-back)

1. Sets this text as your bio

1. Note: it does not make you always `online`

## Running

1. You need your telegram `api_id` and `api_hash`.

   - Create your telegram app [here](https://my.telegram.org/apps)
   - Copy hash and id:
     ![](media/my_telegram.png)
   - Do not share it with anyone!

1. [Install](https://docs.docker.com/engine/install/) Docker

1. Set it to [rootless mode](https://docs.docker.com/engine/security/rootless/)

1. Clone this repo

```sh
git clone https://github.com/br4ch1st0chr0n3/bio-faker-tg
cd bio-faker-tg
```

1. Copy template credentials file

```sh
cp credentials.template.env credentials.env
```

1. Put your credentials into `credentials.env`

### From sources

1. Start the app. You will have to establish a session

```sh
sh source_start.sh
```

## From DockerHub

* When establishing a session, a `sessions/account1.session` file will be created. Using this file **everyone** can access your account. Do not share this file with anyone!

## References

- `python.analysis.diagnosticSeverityOverrides` (see [here](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)) to show import errors

- cache python packages: [src](https://pythonspeed.com/articles/docker-cache-pip-downloads/)

- docker variables: [src](https://vsupalov.com/docker-arg-env-variable-guide/)
