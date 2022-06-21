debugger;
document.addEventListener("DOMContentLoaded", function(){
    create_movie_data();
    draw_posters()
})
document.getElementById("left-search-button").addEventListener("click", choose_genre);
document.getElementById("left-roll-button").addEventListener("click", glow_element);

//Declarations
let api_key = "9757d60d53dfa952ac5a1c239ee6dc1e";
let genre_url =
    "https://api.themoviedb.org/3/genre/movie/list?api_key=9757d60d53dfa952ac5a1c239ee6dc1e&language=en-US";
let category_url = "https://api.themoviedb.org/3/discover/movie?api_key=9757d60d53dfa952ac5a1c239ee6dc1e&language=en-US&sort_by=popularity.desc&include_adult=false&with_genres=&page=1"

//Create Movie Items
function Movie_Item(title, year, rating, poster_path, overview) {
    this.title = title;
    this.year = year;
    this.rating = rating;
    this.poster_path = poster_path;
    this.overview = overview;
    return this.poster_path;
}

//Testing Only
async function test_fetch(){
    r = fetch(genre_url);
    return r;
}

//Take user input and use it to manipulate the URL for the movie list
async function create_url(x){
    x = x;
    r = await fetch("https://api.themoviedb.org/3/discover/movie?api_key=9757d60d53dfa952ac5a1c239ee6dc1e&language=en-US&sort_by=popularity.desc&include_adult=false&with_genres="+x+"&page=1");
    return r;
}
//Default movie requested. Replaced by create_url()
async function request_movies() {
    let r = await fetch(category_url);
    return r;
}

//Creates movie items with info properties and loops through them to populate the data on the front end
function create_movie_data(selection) {
    response_movie_data = create_url(selection);
    response_movie_data
        .then((response) => response.json())
        .then((json) => {
            let r_json;
            let movie_list = [];
            r_json = json;
            for (let i = 0; i < 9; i++) {
                const movie = new Movie_Item(
                    r_json["results"][i]["original_title"],
                    r_json["results"][i]["release_date"],
                    r_json["results"][i]["vote_average"],
                    r_json["results"][i]["poster_path"],
                    r_json["results"][i]["overview"]
                );
                console.log(typeof movie.poster_path); //For Testing
                //console.log("in loop " + typeof movie_list[0].poster_path);//for Testing
                movie_list.push(movie);
                
                selector_string = String("#movie"+(i+1)+"-data");
                document.querySelector(selector_string).querySelector("#movie_title").innerHTML=movie.title;
                document.querySelector(selector_string).querySelector("#movie_overview").innerHTML=movie.overview;
                document.querySelector(selector_string).querySelector("#movie_release_date").innerHTML=movie.year;
            }
        });
}
//document.querySelector(selector_string).querySelector("#movie_title").innerHTML=movie.title;
//document.querySelector(selector_string).querySelector("#movie_overview").innerHTML=movie.overview;
//document.querySelector(selector_string).querySelector("#movie_release_date").innerHTML=movie.year;

//Create URL function pulls a list of movies that match the genre selected by the user
//JSON items are looped and the 'poster_path' property is appended to the APIs poster URL
//Post image is drawn on the frontend in the last loop
function draw_posters(selection) {
    response_movie_poster = create_url(selection);
    response_movie_poster
        .then((response) => response.json())
        .then((json) => {
            let r_json;
            let poster_list = [];
            r_json = json;
            for (let i = 0; i < 9; i++) {
                poster_list.push(r_json["results"][i]["poster_path"]);
                document.getElementById("movie" + (i+1) + "-poster-img").src = "https://image.tmdb.org/t/p/w185" + poster_list[i];
            }
        });
}

//Input Functions
function choose_genre(){
    let selection = []
    let checkboxes = document.querySelectorAll("input[type = checkbox]:checked");
    for (let i = 0; i < checkboxes.length; i++){
        selection.push(checkboxes[i].value)
    }

    console.log(selection);
    draw_posters(selection);
    create_movie_data(selection);
}

function glow_element(){
    let elements = [];
    t = 0;
    elements = document.getElementsByClassName("movie-container");
    glowTimer = setInterval(function(){
            for (let i = 0; i< elements.length; i++){
                elements[i].style.boxShadow = "";
            }
    
            random_element = Math.floor(Math.random() * 9);
            try{
                document.getElementById("movie"+(random_element + 1)+"-area").style.transition="0.2s";
                document.getElementById("movie"+(random_element + 1)+"-area").style.boxShadow = "10px 5px 30px 10px goldenrod";
            }
            catch(err){
                console.log("error on " + (random_element))
            }
            t=t+1;
            console.log(t);
            if(t == 100){
                clearInterval(glowTimer);
            }
    }, 10)
}

//main
//create_movie_data();
//draw_posters();

response_movies = request_movies();
response_movies
.then(response => response.json())
.then(json => {
    console.log(json)
});
//console.log("out of loop " + typeof movie_list[0].poster_path);
//let movie_poster_url = "https://image.tmdb.org/t/p/w185";

//Comedy 35, Romance 10749, Fantasy 14, SciFi 878
//Action 28, Adventure 12, Animation 16, Crime 80
//Doc 99, Drama 18, Family 10751, History 36
//History 36, Horror 27, Music 10402, Mystery 9648
//TV 10770, Thriller 53, War 10752, Western 37