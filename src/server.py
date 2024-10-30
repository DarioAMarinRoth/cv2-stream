import cv2
import socket
import struct
import pickle

# Configuración del socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8089))
server_socket.listen(10)
print("INFO: Esperando conexión...")

# Conexión con el cliente
conn, addr = server_socket.accept()
print(f"INFO: Conexión establecida con {addr}.")

# Buffer de datos
data = b""
payload_size = struct.calcsize(">L")

# Loop principal
while True:

    # Recibir el tamaño del frame y luego el frame
    while len(data) < payload_size:
        data += conn.recv(4096)
    
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]

    while len(data) < msg_size:
        data += conn.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Decodificar el frame
    frame = pickle.loads(frame_data)
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

    # Mostrar el frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

conn.close()
server_socket.close()
cv2.destroyAllWindows()