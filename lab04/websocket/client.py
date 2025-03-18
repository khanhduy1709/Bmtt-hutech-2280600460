import websocket

class CustomWebSocket(websocket.WebSocketApp):
    def send_frame(self, frame):
        return super().send_frame(frame)

def on_message(ws, message):
    print(f"Received message from server: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = CustomWebSocket("ws://localhost:8888/websocket/",
                        on_message=on_message,
                        on_error=on_error,
                        on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(suppress_origin=True)