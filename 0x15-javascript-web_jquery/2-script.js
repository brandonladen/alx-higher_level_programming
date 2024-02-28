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
            // use css to set color
            headerElement.css('color', '#FF0000');
        } else {
            console.error('Header elemnet not found');
        }
    });
});