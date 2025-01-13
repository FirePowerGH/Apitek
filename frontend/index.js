//import { getNewBook } from "../api/api";

function getBookTitle(event) {
    event.preventDefault();

    let textData = document.getElementById("newBook").value;

    let formatText = textData.replace(/\s/g, '+');
    console.log(formatText)
}