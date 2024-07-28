# Book Recommendation System

This project is a Flask-based web application that provides book recommendations. It uses preprocessed data and similarity scores to recommend books based on user input. The web application features a home page displaying the top 50 books and a recommendation page where users can input a book title to get similar book recommendations.

## Features

1. Display of the top 50 books with their details (title, author, image, votes, rating).
2. Recommendation system that suggests similar books based on user input.
3. Interactive UI with Bootstrap styling.

## Installation

To run this project, follow the steps below:

1. Clone the Repository :
   git clone https://github.com/yourusername/book-recommendation-system.git
2. Navigate to the Directory :
   cd book-recommendation-system
3. Install the Required Packages
   Make sure you have pip installed. Then run :
   pip install flask numpy.
4. Place the Data Files : 
   Ensure you have the following pickled data files in the project directory:
   - popular.pkl
   - pt.pkl
   - books.pkl
   - similarity_score.pkl
5. Run the Application :
   python app.py
6. Open the Application
   Open your web browser and navigate to http://127.0.0.1:5000/.

# File Structure

- **app.py:** Main Flask application file.
- **templates/index.html:** HTML template for the home page.
- **templates/recommend.html:** HTML template for the recommendation page.
- **popular.pkl:** Pickled data file containing popular books.
- **pt.pkl:** Pickled data file containing the pivot table of book titles.
- **books.pkl:** Pickled data file containing book details.
- **similarity_score.pkl:** Pickled data file containing similarity scores.

## License
 
This project is licensed under the MIT License. See the LICENSE file for more details

## Support 
 

## Contributing

 Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests. For major changes, please open an issue first to 
 discuss what you would like to change.

 
