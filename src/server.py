import cv2
import socket
import struct

# Configuración del socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8089))
server_socket.listen(1)
print("INFO: Esperando conexión...")

# Conexión con el cliente
conn, addr = server_socket.accept()
print(f"INFO: Conexión establecida con {addr}.")

# Captura de video
cam = cv2.VideoCapture(0)

# Configuración de la calidad de la imagen
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret, frame = cam.read()
    if not ret:
        break
    
    # Codificar el frame a jpg
    result, encoded_frame = cv2.imencode('.jpg', frame, encode_param)
    frame_bytes = encoded_frame.tobytes()
    size = len(frame_bytes)
    
    # Enviar el tamaño (4 bytes) seguido de los datos
    conn.sendall(struct.pack(">L", size) + frame_bytes)

cam.release()
conn.close()
server_socket.close()