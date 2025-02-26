# Thirukkural CLI Tool

A simple command-line tool that displays a random Thirukkural along with its explanation, meaning, and transliteration.

## Features
- Displays a **random Thirukkural** each time it runs.
- Supports various flags for detailed output:
  - `-e` / `--explanation` → Show explanation in English.
  - `-p` / `--porul` → Show meaning (Porul) in Tamil.
  - `-t` / `--transliteration` → Show transliteration.

## Installation

### Clone the Repository
```sh
git clone https://github.com/dhatchu97/thirukkural-cli.git
cd thirukkural-cli
Install Dependencies
Ensure you have Python installed. If required, install dependencies (if any):

sh
Copy
Edit
pip install -r requirements.txt
Usage
Run the script without any arguments to get a random Thirukkural:

sh
Copy
Edit
python3 kural.py
Use flags to get specific details:

sh
Copy
Edit
python3 kural.py -e   # Show explanation in English
python3 kural.py -p   # Show porul (meaning) in Tamil
python3 kural.py -t   # Show transliteration
Example Output
Default Usage:
sh
Copy
Edit
┌──(kali㉿kali)-[~/tools/mytools/kural]
└─$ python3 kural.py

Thirukkural #131:
ஒழுக்கம் விழுப்பந் தரலான ஒழுக்கம்
உயர்நலம் ஓம்பப் படும்.
