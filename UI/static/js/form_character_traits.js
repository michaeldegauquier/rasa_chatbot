$(function() {
    console.log("ready!");

    $("form").submit(function(event) {
        let inputForm = $("input:first").val();
        if ( inputForm !== "") {
            const Urlc = 'https://wcl0c5rsb4.execute-api.us-east-1.amazonaws.com/deployct/character-trait/1';
            let dataObject = {"Id": 1, "character_traits": [inputForm]};

            $.ajax({
                url: Urlc,
                type: 'PUT',
                data: JSON.stringify(dataObject),
                headers: {
                    "Content-Type": "application/json"
                },
                dataType: 'json',
                success: function (result) {
                    console.log(result);
                },
                error: function (error) {
                    console.log(error);
                }
            });

            const Url = 'http://localhost:8080/reset_bot';
            $.ajax({
                type: "GET",
                url: Url,
                success: function (result) {
                    console.log(result);
                },
                error: function (error) {
                    console.log(error);
                }
            });
        }
        else {
            $("p").text("Not valid!").show().fadeOut(500);
        }
        event.preventDefault();
    });
});
