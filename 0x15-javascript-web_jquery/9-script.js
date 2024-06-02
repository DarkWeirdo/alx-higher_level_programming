$(document).ready(function() {
    $.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
        let hello = data.hello;
        $("#hello").text(hello);
    });
});
