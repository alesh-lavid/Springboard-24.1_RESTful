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