
/* Get the element you want displayed in fullscreen mode */
var elem = document.body;
var fullscreenButton = document.querySelector("#fullscreen-button-container");

/* When the openFullscreen() function is executed, open the video in fullscreen.
Note that we must include prefixes for different browsers, as they don't support the requestFullscreen method yet */
function openFullscreen() {
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
        elem.msRequestFullscreen();
    }
    fullscreenButton.style.display = "none";
}

$(document).ready(function () {

    "use strict";

    var todo = function () {
        $('.todo-list .todo-item').click(function () {
            $(this).toggleClass('hello');
        });

        $('#uniform-all-complete input').click(function () {
            if ($(this).is(':checked')) {
                $('.todo-item .checker span:not(.checked) input').click();
            } else {
                $('.todo-item .checker span.checked input').click();
            }
        });

    };

    todo();

});
