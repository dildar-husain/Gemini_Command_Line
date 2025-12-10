#!/usr/bin/env python3
"""
Gemini Command Line - A command-line interface for Google's Gemini AI
"""

import os
import sys
import argparse
from typing import Optional
import google.generativeai as genai
from dotenv import load_dotenv


class GeminiCLI:
    """Command-line interface for Gemini AI"""
    
    def __init__(self, api_key: str, model_name: str = "gemini-pro"):
        """
        Initialize the Gemini CLI
        
        Args:
            api_key: Google API key for Gemini
            model_name: Name of the Gemini model to use
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        self.chat = None
        
    def send_message(self, message: str) -> str:
        """
        Send a message to Gemini and get response
        
        Args:
            message: The message to send
            
        Returns:
            The response from Gemini
        """
        try:
            response = self.model.generate_content(message)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
    
    def start_chat(self):
        """Start an interactive chat session"""
        self.chat = self.model.start_chat(history=[])
        
    def send_chat_message(self, message: str) -> str:
        """
        Send a message in chat mode
        
        Args:
            message: The message to send
            
        Returns:
            The response from Gemini
        """
        if self.chat is None:
            self.start_chat()
        
        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
    
    def interactive_mode(self):
        """Run in interactive chat mode"""
        print("Gemini Command Line - Interactive Mode")
        print("Type 'exit' or 'quit' to end the session")
        print("Type 'clear' to clear conversation history")
        print("-" * 50)
        
        self.start_chat()
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['exit', 'quit']:
                    print("Goodbye!")
                    break
                    
                if user_input.lower() == 'clear':
                    self.start_chat()
                    print("Conversation history cleared.")
                    continue
                
                response = self.send_chat_message(user_input)
                print(f"\nGemini: {response}")
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except EOFError:
                print("\n\nGoodbye!")
                break


def main():
    """Main entry point for the CLI"""
    parser = argparse.ArgumentParser(
        description="Gemini Command Line - Use Google's Gemini AI from the command line",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  gemini.py --interactive                    # Start interactive chat mode
  gemini.py --query "What is Python?"        # Single query
  gemini.py -q "Explain AI" -m gemini-pro    # Query with specific model
        """
    )
    
    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Start interactive chat mode'
    )
    
    parser.add_argument(
        '-q', '--query',
        type=str,
        help='Send a single query and exit'
    )
    
    parser.add_argument(
        '-m', '--model',
        type=str,
        default='gemini-pro',
        help='Gemini model to use (default: gemini-pro)'
    )
    
    parser.add_argument(
        '--api-key',
        type=str,
        help='Google API key (overrides environment variable)'
    )
    
    args = parser.parse_args()
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = args.api_key or os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found.", file=sys.stderr)
        print("Please set the GEMINI_API_KEY environment variable or use --api-key option.", file=sys.stderr)
        print("\nYou can get an API key from: https://makersuite.google.com/app/apikey", file=sys.stderr)
        sys.exit(1)
    
    try:
        cli = GeminiCLI(api_key=api_key, model_name=args.model)
        
        if args.query:
            # Single query mode
            response = cli.send_message(args.query)
            print(response)
        elif args.interactive:
            # Interactive mode
            cli.interactive_mode()
        else:
            # No arguments provided, show help
            parser.print_help()
            print("\nTip: Use --interactive to start a chat session or --query to ask a question")
            
    except Exception as e:
        print(f"Error initializing Gemini: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
