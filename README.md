# R Movie Journal App

The **Movie Journal App** is a Django-based application that allows movie enthusiasts to log, review, and organize their cinematic experiences. The backend is fully functional, and plans are underway to integrate a React-based frontend to enhance user interaction.

## Features

- **User Authentication (In Progress)**: Secure user registration, login, and profile management.
- **Movie Database Integration**: Fetch movie details using an IMDb or free movie API.
- **Movie Logging**: Add movies to your personal log with reviews, ratings, and tags.
- **Favorite Lists**: Create and manage custom favorite lists.
- **AI Recommendations (Coming soon)**:  AI-powered movie suggestions based on your preferences.
- **Frontend (In Progress)**: A React-based interface is planned to provide an engaging and interactive user experience.

## Tech Stack

### Backend:
- **Django/DRF**: For robust and scalable backend functionality.
- **SQLite**: Default database for development (can be replaced with PostgreSQL or another database for production).
- **APIs**: Integrates with external movie databases (OMDB).

### Frontend:
- **React**: Planned for an interactive and modern user interface.

## Installation and Setup

### Prerequisites
- Python v3.12
- Django v5.1.3
- Node.js and npm/yarn (node v22.12)
- Git
- OMDB API

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-journal-app.git
   cd movie-journal-app
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate # For Unix/Linux
   env\Scripts\activate   # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup (Pending)
Frontend development with React is in progress and will be integrated soon.

## Usage
- Access the app at `http://127.0.0.1:8000/` after running the development server.
- Create an account, log in, and start logging your movies!

## Roadmap
- [x] Backend implementation with Django
- [x] Database integration and migrations
- [ ] Develop and integrate React frontend
- [ ] Deploy the app for public use

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.


## Acknowledgments
- Movie database APIs for providing extensive movie data.
- Django and React communities for their excellent tools and documentation.
