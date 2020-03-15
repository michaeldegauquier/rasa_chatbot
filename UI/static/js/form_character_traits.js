$(function() {
    console.log("ready!");

    $("form").submit(function(event) {
        let inputForm = $("input:first").val();
        if (inputForm !== "") {
            const Urlc = 'https://wcl0c5rsb4.execute-api.us-east-1.amazonaws.com/deployct/character-trait/1';
            let dataObject = {"Id": 1, "character_traits": [inputForm]};

            // Put the new character traits in the database on AWS
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

            // Reset the data from the chatbot about the car insurance
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


// Reddit. Execute a python script on button click? Geraadpleegd via
// https://www.reddit.com/r/learnpython/comments/9xyozb/execute_a_python_script_on_button_click/
// Geraadpleegd op 14 maart 2020