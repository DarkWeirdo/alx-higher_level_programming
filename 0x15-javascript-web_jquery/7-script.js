$(document).ready(function() {
    // Perform an Ajax request to the specified URL
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        type: 'GET', // Specify the type of request
        dataType: 'json', // Expect a JSON response
        success: function(data) {
            // Extract the character's name from the JSON response
            var characterName = data.name;
            
            // Update the DIV#character element with the character's name
            $('#character').text(characterName);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // Handle any errors that occur during the request
            console.error("Error fetching character data:", textStatus, errorThrown);
        }
    });
});
