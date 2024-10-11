<h3 align="center">California Housing Webapp</h3>

  <p align="center">
    Webapp for making predictions on California Housing Prices
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[streamlit-app-2022-08-10-23-08-72.webm](https://user-images.githubusercontent.com/25290130/184062032-b330c593-67fc-4483-a864-0820cb5b3f5f.webm)

This is a webapp created using streamlit to make predictions for california housing prices. The backend uses a bentoml api endpoint. A SVR model is used for predictions.


### Built With

* [![Streamlit][Streamlit.io]][Streamlit-url]
* [![Scikit-Learn][Scikit-learn.org]][Scikit-learn-url]
* [![Bentoml][Bentoml.com]][Bentoml-url]


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Install Docker for your OS

<!-- USAGE EXAMPLES -->
## Usage

1. ```docker-compose up --build api```

2. ```docker-compose up --build web```

3. Navigate to "localhost:8501" in your browser

[Streamlit-url]: https://streamlit.io/
[Streamlit.io]: https://img.shields.io/badge/Streamlit-0769AD?style=for-the-badge&logo=streamlit&logoColor=FF4B4B
[Scikit-learn.org]: https://img.shields.io/badge/ScikitLearn-0769AD?style=for-the-badge&logo=scikit-learn&logoColor=F7931E
[Scikit-learn-url]: https://scikit-learn.org/stable/
[Bentoml.com]: https://img.shields.io/badge/Bentoml-0769AD?style=for-the-badge&logo=python&logoColor=3776AB
[Bentoml-url]: https://www.bentoml.com/

