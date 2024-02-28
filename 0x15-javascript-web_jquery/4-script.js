//JQureey script
$(document).ready(function () {
    // get the div by id
    const element = $('DIV#toggle_header');
    const headerElement = $('header');

    // add event listener
    element.click(function () {
        headerElement.toggleClass('red green');
    });
});