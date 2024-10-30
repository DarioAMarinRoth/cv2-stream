import cv2
import socket
import struct
import pickle

# Configuración del socket

SERVER_IP = '0.0.0.0' # !TODO: Cambiar por la IP del servidor

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, 8089))

# Captura de video
cam = cv2.VideoCapture(0)

# Configuración de la calidad de la imagen
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Codificar el frame
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    data = pickle.dumps(frame, 0)
    size = len(data)

    # Enviar el tamaño del frame y luego el frame
    client_socket.sendall(struct.pack(">L", size) + data)

cam.release()
client_socket.close()