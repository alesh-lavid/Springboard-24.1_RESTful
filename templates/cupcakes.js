//Axios to query the API and recieve list of cupcakes
axios.get('/cupcakes')
    .then(function(response) {
        response.data.forEach(function(cupcake){
            $('#cupcakes-list').append(`
            <li>
                <h3>${cupcake.flavor}</h3>
                <p>Rating: ${cupcake.rating}</p>
            </li>
            `);
        });
    });

    //Listen to form submission
    $('#cupcake-form').on('submit', function(e) {
        e.preventDefault();

        let flavor = $('#flavor').val();
        let rating = $('#rating').val();

        axios.post('/cupcakes', {
            flavor: flavor,
            rating: rating
        }).then(function(response) {
            $('#cupcakes-list').append(`
            <li>
              <h3>${response.data.flavor}</h3>
              <p>Rating: ${response.data.rating}</p>
            </li>
          `);
        });
    });