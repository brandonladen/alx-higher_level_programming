// select the element
const headerElement = document.querySelector('header');

// check if the element was found
if (headerElement) {
    headerElement.style.color = '#FF0000';
} else {
    console.error('Header element not found')   
}