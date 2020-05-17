$(function() {
    console.log("ready!");
    $('#profile_div').hide();

    $("form").submit(async function(event) {
        deleteMessages();
        let a = false;
        let inputForm = $("textarea:first").val();
        console.log(inputForm);
        if (inputForm !== "") {
            $("span.loading").text("Searching for person, please wait...").show();
            $('#profile_div').hide();

            /*const Urlc = 'https://wcl0c5rsb4.execute-api.us-east-1.amazonaws.com/deployct/character-trait/1';
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
            });*/

            // Reset the data from the chatbot about the car insurance
            const UrlChatbot = /*'https://d84f23e9.ngrok.io/test';*/ 'http://localhost:8080/test';
            const UrlFaceGen = 'http://5c6b24d0.ngrok.io';
            let name = document.getElementById('showName');
            let nameChatbox = document.getElementById('nameChatbox');

            $.ajax({
                type: 'POST',
                url: UrlChatbot,
                data: JSON.stringify(inputForm),
                headers: {
                    "Content-Type": "application/json"
                },
                dataType: 'json',
                success: function (result) {
                    console.log(result);
                    name.innerHTML = 'You can talk now with ' + result.name + '.';
                    nameChatbox.innerHTML = ' ' + result.name;
                    getImage(UrlFaceGen, result);
                },
                error: function (error) {
                    $("span.loading").text("Searching for person, please wait...").fadeOut();
                    console.log(error);
                }
            });
        }
        else {
            $("span.error").text("Description is required!").show().fadeOut(1000);
        }
        event.preventDefault();
    });

    function getImage(UrlFaceGen, data) {
            $.ajax({
                type: 'POST',
                url: UrlFaceGen,
                data: JSON.stringify(data),
                headers: {
                    "Content-Type": "application/json"
                },
                dataType: 'json',
                success: function (result) {
                    console.log(result);
                    setInterval("");
                    setTimeout(loadImage, 20000);
                    $("span.loading").text("Loading image, please wait...");
                },
                error: function (error) {
                    $("span.loading").text("Searching for person, please wait...").fadeOut();
                    console.log(error);
                }
            });
    }

    function loadImage() {
        $('#profile_div').fadeIn();
        $("span.loading").text("Loading image, please wait...").fadeOut();
        return true;
    }

    setInterval(function(){
        $("#re").attr("src", "https://drive.google.com/uc?export=view&id=1XGwyvEIPvxvef9f2O9XMzVSuamME3mSm&t="+new Date().getTime());
        $("#re1").attr("src", "https://drive.google.com/uc?export=view&id=1XGwyvEIPvxvef9f2O9XMzVSuamME3mSm&t="+new Date().getTime());
    },2000);

    // Delete all messages
    function deleteMessages() {
        $("p.userMsg").fadeOut();
        $("p.botMsg").fadeOut();
        $("img.botAvatar").fadeOut();
    }
});


// Reddit. Execute a python script on button click? Geraadpleegd via
// https://www.reddit.com/r/learnpython/comments/9xyozb/execute_a_python_script_on_button_click/
// Geraadpleegd op 14 maart 2020

// Stackoverflow. Refresh <img> in jQuery periodically. Geraadpleegd via
// https://stackoverflow.com/questions/7337113/refresh-img-in-jquery-periodically
// Geraadpleegd op 5 mei 2020

// How do I display images from Google Drive on a website? Geraadpleegd via
// https://stackoverflow.com/questions/15557392/how-do-i-display-images-from-google-drive-on-a-website
// Geraadpleegd op 5 mei 2020