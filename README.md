# OpenCV Video Stream

La comunicación se basa en un modelo cliente-servidor. En este caso, el Hodor sería el servidor y la computadora que recibe el video sería el cliente. Por lo tanto, en el Hodor hay que correr el script 'server.py' y en la notebook el script 'client.py'

## Requisitos

- Ambas computadoras, cliente y servidor, deben contar con la librería de python de OpenCV. \
Se instala mediante: `pip install opencv-python`
- El cliente debe contar con la librería Pillow. \
Se instala mediante: `pip install pillow`
- Ambas computadoras deben estar conectadas en la misma red.
- El script del servidor debe estar en ejecución antes de correr el script del cliente.

## Configuración

La comunicación entre las dos computadoras se establece mediante un socket. Lo único que hay que modificar es la dirección IP del server en el script del cliente. Es decir, en el script que corre sobre el Hodor hay configurar la IP de la computadora a la que queremos transmitir el video.

En lo siguiente, teóricamente no habría que modificar nada pero por las dudas dejo escrito:
Tanto en el script del cliente como en el del servidor hay que configurar la dirección IP y el puerto por el cuál se va a comunicar (en el método `bind` en el caso del servidor y `connect` en el caso del cliente). Arbitrariamente está puesto el puerto 8089 (TCP) pero se podría usar cualquier otro, la única precaución que hay que tener es que ambos scripts tengan el mismo puerto. \
Con respecto a la IP en el servidor, está puesta 0.0.0.0, lo que permite escuchar de todas las direcciones IP. Lo puse para tener un problema menos en cuanto a la conectividad, pero si por alguna razón se considera inseguro, los scripts deberían funcionar igualmente si se coloca la IP del servidor.

Por último, no hay que olvidar de actualizar en índice de la cámara en el script del cliente por el correspondiente:

```py
# Captura de video
cam = cv2.VideoCapture(0) # Cambiar 0 por el índice de la cámara que corresponda.
```

## Ejecución

1. Correr el script del servidor `python server.py`
2. Correr el script del cliente `python client.py`

Esto debería abrir una ventana en el servidor con el video del cliente.

Para finalizar, presionar la tecla 'q' en la ventana de video del servidor.
