from app import create_app

# Criar a aplicação usando a factory function
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
