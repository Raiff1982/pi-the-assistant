# Advanced Bot Application

## Overview

This C# program is an advanced bot application that integrates sentiment analysis, ethical decision-making, and response generation using Azure OpenAI. It includes various utility functions for different reasoning methods and API integrations.

## Features

- **Advanced Sentiment Analysis**: Uses BERT for sentiment analysis and integrates it with other models like TextBlob and VADER.
- **Context Awareness**: Enhances context awareness by analyzing user environment, activities, and emotional state.
- **Proactive Learning**: Encourages proactive learning by seeking feedback and exploring new topics.
- **Ethical Decision-Making**: Integrates ethical principles into decision-making processes.
- **Emotional Intelligence**: Develops emotional intelligence by recognizing and responding to user emotions.
- **Transparency and Explainability**: Provides transparency by explaining the reasoning behind decisions.
- **Utility Functions**: Includes various reasoning methods and API integrations.
- **Secure API Handling**: Stores API keys in environment variables.
- **Error Handling and Logging**: Robust error handling and logging mechanisms.
- **Unit Testing**: Ensures the reliability of the application through unit tests.
- **Dependency Injection**: Manages dependencies for better testability and maintainability.

## Setup and Configuration

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install dependencies**:
    Ensure you have .NET Core SDK installed. Then, run:
    ```bash
    dotnet restore
    ```

3. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```plaintext
    AZURE_OPENAI_API_KEY=<your-azure-openai-api-key>
    AZURE_OPENAI_ENDPOINT=<your-azure-openai-endpoint>
    WEATHER_API_KEY=<your-weather-api-key>
    NEWS_API_KEY=<your-news-api-key>
    ALPHA_VANTAGE_API_KEY=<your-alpha-vantage-api-key>
    TRANSLATION_API_KEY=<your-translation-api-key>
    ```

4. **Run the application**:
    ```bash
    dotnet run
    ```

## Usage

The bot can be used to generate responses, analyze sentiment, and perform various reasoning methods. Example usage is provided in the `Program.cs` file.

## Unit Testing

To run the unit tests, use the following command:
```bash
dotnet test