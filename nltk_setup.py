import nltk
import os

# Set the NLTK data path to a writable directory in Vercel
nltk_data_dir = os.path.join(os.getcwd(), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# Download required NLTK data
def download_nltk_data():
    try:
        # Check if data already exists
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('corpora/wordnet')
            print("NLTK Data already exists")
        except LookupError:
            print("Downloading NLTK data...")
            nltk.download('punkt', download_dir=nltk_data_dir)
            nltk.download('wordnet', download_dir=nltk_data_dir)
            print("NLTK data downloaded successfully")
    except Exception as e:
        print(f"Error downloading NLTK data: {str(e)}")

# Call the function to download data
download_nltk_data() 