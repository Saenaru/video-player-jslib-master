from livereload import Server

def rebuild():
    print("Files changed - reloading...")

server = Server()

server.watch('index.html', rebuild)
server.watch('player.js', rebuild)
server.watch('styles.css', rebuild)

server.serve(root='.', host='0.0.0.0', port=5500)