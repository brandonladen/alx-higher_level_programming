// jQuery script
$(document).ready(function() {

    // select the div by ID
    const element = $('DIV#red_header');

    // add an event handler
    element.click(function() {
        // find the header
        const headerElement = $('header');

        // check if header was found
        if (headerElement) {
            // add class to header tag
            headerElement.addClass('red');
        } else {
            console.error('Header elemnet not found');
        }
    });
});