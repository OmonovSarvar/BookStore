# Book Store

This project is a simple Book Store built using django rest framework

## Getting Started

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/OmonovSarvar/BookStore.git


### only [GET] request http://127.0.0.1:8000/api - Returns all available Books
### only GET request http://127.0.0.1:8000/api/all - Returns all Books
### only POST request http://127.0.0.1:8000/api/new - Endpoint for adding a new Book. (automatically added on behalf of the person who is logged in
### only GET request http://127.0.0.1:8000/api/<id> - Show Book with <id> (detail view)
### only DELETE request http://127.0.0.1:8000/api/<id>/delete - Deletes the Book with <id>
### only PUT/PATCH request http://127.0.0.1:8000/api/<id>/update - Updates the information of the Book with <id>
### only GET request http://127.0.0.1:8000/api/<username> - Returns all Books of user <username>
### only GET request http://127.0.0.1:8000/api/sort/?sort=<field> - sorts Books by the given <filed>
### only POST request http://127.0.0.1:8000/api/signup - View to sign up
### only POST request http://127.0.0.1:8000/api/login - Endpoint for login
### only POST request http://127.0.0.1:8000/api/reset - Endpoint to reset the password for those who have forgotten it
### only GET request http://127.0.0.1:8000/api/subscribe - To subscribe to a blog post
### only GET request http://127.0.0.1:8000/api/search/?search=<title> - search Books by the given title
### only GET request http://127.0.0.1:8000/api/schema - Show schemes
### only GET request http://127.0.0.1:8000/api/schema/swagger - Swagger of the project
### GET POST PUT request http://127.0.0.1:8000/api/token/auth - Gives you bareer token for authentication



## Contact_me

__https://t.me/its_sarvar__
