from .backend import app

if __name__ == "__main__":
  print('Server running at localhost:8890')
  app.run(host='0.0.0.0', port=8890)

