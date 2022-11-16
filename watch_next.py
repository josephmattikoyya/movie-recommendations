import spacy

nlp = spacy.load('en_core_web_md')

def recommend_a_movie(given_description):
    nlp_given_description = nlp(given_description)
    similar_movies = {}

    with open('movies.txt', 'r') as movie_file:
        for i in movie_file:
            name, description = i.split(':')
            name = name.strip()
            description = description.strip()
            similarity = nlp(description).similarity(nlp_given_description)
            similar_movies[name] = similarity
    
    recommended_movie = max(similar_movies, key = similar_movies.get)
    return recommended_movie


print(recommend_a_movie("""
Will he save their world or destroy it?
When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk an live in peace.
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.
"""))
