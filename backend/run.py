from .app import create_app
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)