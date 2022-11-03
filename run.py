file = open("README.md","w")
template ="""# Project Title

A brief description of what this project does and who it's for


![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

<br>

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

<br>

## Demo

Insert gif or link to demo

<br>

## Authors

- [@octokatherine](https://www.github.com/octokatherine)

<br>

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`

<br>

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```

<br>

## Feedback

If you have any feedback, please reach out to us at fake@fake.com

<br>

## License

[MIT](https://choosealicense.com/licenses/mit/)"""
file.write(template)
file.close()