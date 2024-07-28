from flask import Flask, render_template, request
import pickle as pk
import numpy as np

# Load the pickled data files
popular_df = pk.load(open('popular.pkl', 'rb'))
pt = pk.load(open('pt.pkl', 'rb'))
books = pk.load(open('books.pkl', 'rb'))
similarity_score = pk.load(open('similarity_score.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_ratings'].values),
        rating=list(popular_df['avg_rating'].values)
    )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input').strip().lower()

    try:
        # Convert pt.index to lowercase for case-insensitive comparison
        pt_index_lower = pt.index.str.lower()

        # Check if user_input is in pt_index_lower
        if user_input not in pt_index_lower:
            raise ValueError("Book not found")

        index = np.where(pt_index_lower == user_input)[0][0]
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'].str.lower() == pt.index[i[0]].lower()]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)

        print(data)

        return render_template('recommend.html', data=data)

    except Exception as e:
        return render_template('recommend.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
