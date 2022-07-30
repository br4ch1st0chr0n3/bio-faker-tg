Telegram bio updater
===

## What it does
1. With a given frequency, it gets some text supplied by a [server](https://github.com/br4ch1st0chr0n3/bio-faker-back)

1. Sets this text as your bio 

1. Note: it does not make you always `online`

## Running

1. You need your telegram `api_id` and `api_hash`. 
    
    + Create your telegram app [here](https://my.telegram.org/apps)
    + Copy hash and id: 
    ![](media/my_telegram.png)
    + Do not share it with anyone!


### Run from Docker Hub

* Rename the credentials file and fill its fields with your credentials:

```sh
mv credentials.template.env credentials.env
```



## How to install

1. Paste your credentials into `src/credentials.py`:

```python
credentials = {
    'api_id': <api_id>,
    'api_hash': '<api_hash>',
    'session': 'sessions/account1.session'
}
```
1. [Install](https://docs.docker.com/engine/install/) Docker

1. Set it to [rootless mode](https://docs.docker.com/engine/security/rootless/)

1. Either run the following instructions one-by-one, or via a script
```sh
$ sh start.sh
```

---

1. Set an environment variable

    ```shell
    $ export DOCKER_BUILDKIT=1
    ```

1. Build

    ```shell
    $ docker compose build
    ```

1. Create a session file (you need to do it only once)

    ```shell
    $ docker compose run create_session
    Please enter your phone (or bot token): <your telephone>
    Please enter the code you received: <code you received>
    Please enter your password: <your password>
    Signed in successfully as TG Name
    ```

    This will create a `sessions/account1.session` file. Using this file **everyone** can access your account. Do not share this file with anyone!

1. Run the polling script to see container logs

    ```shell
    $ docker compose up updater
    ```

1. Alternatively, run it in background

    ```shell
    $ docker compose up -d updater
    ```

## References
* `python.analysis.diagnosticSeverityOverrides` (see [here](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)) to show import errors

* cache python packages: [src](https://pythonspeed.com/articles/docker-cache-pip-downloads/)

* docker variables: [src](https://vsupalov.com/docker-arg-env-variable-guide/)