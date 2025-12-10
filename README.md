# Gemini Command Line

A powerful command-line interface for interacting with Google's Gemini AI directly from your terminal.

## Features

- 🚀 **Interactive Chat Mode**: Have continuous conversations with Gemini AI
- 💬 **Single Query Mode**: Ask one-off questions and get instant answers
- 📝 **Conversation History**: Maintain context across multiple messages in chat mode
- 🎯 **Multiple Models**: Support for different Gemini models (gemini-pro, etc.)
- 🔧 **Easy Configuration**: Simple setup with environment variables

## Prerequisites

- Python 3.7 or higher
- Google API key for Gemini AI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dildar-husain/Gemini_Command_Line.git
cd Gemini_Command_Line
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

### Interactive Chat Mode

Start a continuous conversation with Gemini:

```bash
python gemini.py --interactive
```

In interactive mode:
- Type your messages and press Enter to send
- Type `exit` or `quit` to end the session
- Type `clear` to clear conversation history and start fresh
- Use Ctrl+C to exit

### Single Query Mode

Ask a single question and get an answer:

```bash
python gemini.py --query "What is the capital of France?"
```

Short form:
```bash
python gemini.py -q "Explain quantum computing"
```

### Advanced Options

Specify a different model:
```bash
python gemini.py -q "Hello" -m gemini-pro
```

Use API key from command line (overrides environment variable):
```bash
python gemini.py --api-key YOUR_API_KEY --interactive
```

## Command-Line Options

```
-i, --interactive       Start interactive chat mode
-q, --query TEXT        Send a single query and exit
-m, --model MODEL       Gemini model to use (default: gemini-pro)
--api-key KEY          Google API key (overrides environment variable)
-h, --help             Show help message
```

## Examples

1. **Quick question:**
   ```bash
   python gemini.py -q "What is Python?"
   ```

2. **Interactive session:**
   ```bash
   python gemini.py --interactive
   ```

3. **Using a specific model:**
   ```bash
   python gemini.py -q "Explain AI" -m gemini-pro
   ```

## Environment Variables

- `GEMINI_API_KEY`: Your Google API key for Gemini AI (required)

## Error Handling

The CLI includes error handling for:
- Missing API key
- Network issues
- Invalid responses
- User interruptions (Ctrl+C)

## Security Notes

- Never commit your `.env` file or expose your API key
- The `.gitignore` file is configured to exclude `.env` files
- Use environment variables or command-line options for API keys

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Dildar Husain

## Acknowledgments

- Powered by [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- Built with [google-generativeai](https://pypi.org/project/google-generativeai/) Python SDK