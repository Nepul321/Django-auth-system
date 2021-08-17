const old_password = document.getElementById('id_old_password');
const new_password1 = document.getElementById('id_new_password1');
const new_password2 = document.getElementById('id_new_password2');

const elements = [old_password, new_password1, new_password2];
const paragraphs = document.querySelectorAll('p');
const labels = document.querySelectorAll('label');

const links = document.querySelectorAll('a')

elements.forEach(element => {
    element.className += "border border-gray-400 shadow p-3 w-full rounded my-2";
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