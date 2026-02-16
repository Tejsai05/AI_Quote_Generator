# AI Quote Generator 🎯

A Flask-based web application that generates inspirational quotes using the API Ninjas Quotes API. The application features a clean interface with user authentication pages and a dynamic quote generation system.

## Features

- 🎲 Random AI-powered quote generation
- 🏠 Clean home page interface
- 🔐 User login and registration pages
- 📱 Responsive design
- ⚡ Real-time quote fetching from API Ninjas

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML/CSS
- **API**: API Ninjas Quotes API
- **Environment Management**: python-dotenv

## Project Structure

```
AI_Quote_Generator/
├── app.py                    # Main Flask application
├── templates/
│   ├── home.html            # Landing page
│   ├── index.html           # Quote display page
│   ├── login.html           # Login page
│   └── registration.html    # Registration page
├── .env                     # API key configuration (not in repo)
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tejsai05/AI_Quote_Generator.git
   cd AI_Quote_Generator
   ```

2. **Install dependencies**
   ```bash
   pip install flask requests python-dotenv
   ```

3. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your API Ninjas API key:
     ```
     NINJA_API_KEY=your_api_key_here
     ```
   - Get your free API key from [API Ninjas](https://api-ninjas.com/)

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

## Routes

- `/` - Home page
- `/AI` - Quote generator page
- `/login` - Login page
- `/registration` - Registration page

## API Reference

This project uses the [API Ninjas Quotes API](https://api-ninjas.com/api/quotes) to fetch random inspirational quotes.

## Future Enhancements

- Implement actual user authentication
- Add database integration for user management
- Save favorite quotes
- Category-based quote filtering
- Share quotes on social media

## License

This project is open source and available under the MIT License.

## Author

[Tejsai05](https://github.com/Tejsai05)
