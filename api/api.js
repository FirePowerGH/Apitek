// https://openlibrary.org/search.json?title=harry+potter&fields=title,author_name&lang=en&limit=1

export function getNewBook(query) {
    fetch(`https://openlibrary.org/search.json?title=${query}&fields=title,author_name&lang=en&limit=1`)
    .then(respons => {
        if (respons.status != 200){
            return "Something went wrong"+"<br>"+"Code: "+respons.status
        }
    return respons.json()
    })
}