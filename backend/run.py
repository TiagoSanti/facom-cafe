from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()

# LBD_DATABASE_URI e TADS_DATABASE_URI são variáveis de ambiente
app = create_app(os.getenv('TADS_DATABASE_URI'))

if __name__ == '__main__':
    app.run(debug=True)