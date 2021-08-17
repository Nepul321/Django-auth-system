const username = document.getElementById('id_username');
const first_name = document.getElementById('id_first_name');
const last_name = document.getElementById('id_last_name');
const email = document.getElementById('id_email');

const elements = [username, first_name, last_name, email];
const paragraphs = document.querySelectorAll('p');
const labels = document.querySelectorAll('label');

const links = document.querySelectorAll('a')

elements.forEach(element => {
    element.className += "border border-gray-400 shadow p-3 w-full rounded my-2";
    element.setAttribute('required', '');
});

paragraphs.forEach(paragraph => {
    paragraph.className += " my-3";
});

labels.forEach(label => {
    label.className += " block mb-2 font-bold text-gray-600 my-2 mb-2";
});

links.forEach(link => {
    link.setAttribute('class', 'text-blue-500')
})