# driver test

Shows how to share audio devices from host to docker container

https://leimao.github.io/blog/Docker-Container-Audio/

`docker build --no-cache --tag=audiotest .`


`docker run -it --rm --device /dev/snd audiotest`

`arecord -l`
