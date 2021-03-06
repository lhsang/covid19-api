<p align="center">
    <img src="https://cdn2.iconfinder.com/data/icons/covid-19-2/64/29-Doctor-256.png">
</p>

<h1>COVID19-API</h1>

[![issues](<https://img.shields.io/github/issues/nat236919/Covid2019API>)](https://github.com/nat236919/Covid2019API/issues)
[![forks](<https://img.shields.io/github/forks/nat236919/Covid2019API>)](https://github.com/nat236919/Covid2019API/forks)
[![stars](<https://img.shields.io/github/stars/nat236919/Covid2019API>)](https://github.com/nat236919/Covid2019API/stars)
[![license](<https://img.shields.io/github/license/nat236919/Covid2019API>)](https://github.com/nat236919/Covid2019API/blob/master/LICENCE)

This API provides the information regarding '2019 Novel Coronavirus (covid-19)'. It contains a number of confirmed, death, and recovered cases based on the data provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE).

#### Examples:
* https://covid2019-api.herokuapp.com/
* https://covid2019-api.azurewebsites.net/

#### Applications:
* [Coronavirus App by YaseenAbdullah](https://github.com/YaseenAbdullah/coronavirus)
* [Covid 19 App - Map, info & help by DavidBarbaran](https://github.com/DavidBarbaran/Covid19App)
* [COVID-19 Visual Explorer by FitnessAI](https://www.fitnessai.com/covid-19-charts-coronavirus-growth-rate-visual-explorer)
* [BAILAM (Data and API Integration)](https://www.bailam.com/covid19)
* [Coronavirus Tech Handbook (Data Tools)](https://coronavirustechhandbook.com/data-tools)



#### References
https://github.com/CSSEGISandData/COVID-19

## Branches
|  Branch           |     Feature                      |              Description                                     |
| ----------------- | -------------------------------- |  ----------------------------------------------------------- |
| master            | Docker + Web API                 | For deploying to a server                                    |
| development       | Docker + Web API                 | For testing before merging to Master                         |

## Features
1. The current data (daily updated)
2. Confirmed, Deaths, Recovered
3. The affected countries
4. Individual affected country
5. Timeseries

## How to install
* Run the following command in your command line to run the server
{your_path}/app >
```console
uvicorn main:app
```

## How to install (Docker-compose)
* Run the following command in your command line to run the server
```console
docker-compose up
```

* Or run the server in the background
```console
docker-compose up -d
```

* The port can be changed at <b>docker-compose.override.yml</b>
```yml
version: '3'
services:
  web:
    container_name: "covid19_api_web_container"
    volumes:
      - ./app:/app
    ports:
      - "80:80"
    environment:
      - 'RUN=uvicorn main:app'
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://nuttaphat.azurewebsites.net"><img src="https://avatars0.githubusercontent.com/u/9074112?v=4" width="100px;" alt=""/><br /><sub><b>Nuttaphat Arunoprayoch</b></sub></a><br /><a href="#maintenance-nat236919" title="Maintenance">🚧</a> <a href="https://github.com/nat236919/Covid2019API/commits?author=nat236919" title="Code">💻</a> <a href="https://github.com/nat236919/Covid2019API/commits?author=nat236919" title="Documentation">📖</a> <a href="https://github.com/nat236919/Covid2019API/pulls?q=is%3Apr+reviewed-by%3Anat236919" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/soapy1"><img src="https://avatars0.githubusercontent.com/u/976973?v=4" width="100px;" alt=""/><br /><sub><b>Sophia Castellarin</b></sub></a><br /><a href="https://github.com/nat236919/Covid2019API/commits?author=soapy1" title="Code">💻</a></td>
    <td align="center"><a href="https://keybase.io/endoffile78"><img src="https://avatars2.githubusercontent.com/u/11342054?v=4" width="100px;" alt=""/><br /><sub><b>Jeremy</b></sub></a><br /><a href="https://github.com/nat236919/Covid2019API/commits?author=endoffile78" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ChooseYourPlan"><img src="https://avatars2.githubusercontent.com/u/32968964?v=4" width="100px;" alt=""/><br /><sub><b>Tim</b></sub></a><br /><a href="#translation-ChooseYourPlan" title="Translation">🌍</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
