<!--
*** This document uses markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See bellow for the declaration of the reference variables
*** for contributors-url, forks-url, etc. Find and replace "repo_template" with your repo name
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-url]: https://github.com/omnivector-solutions/osd-documentation/graphs/contributors
[forks-url]: https://github.com/omnivector-solutions/osd-documentation/network/members
[stars-url]: https://github.com/omnivector-solutions/osd-documentation/stargazers
[issues-url]: https://github.com/omnivector-solutions/osd-documentation/issues
[license-url]: https://github.com/omnivector-solutions/osd-documentation/blob/master/LICENSE.txt
[website]: https://www.omnivector.solutions
[product-screenshot]: images/screenshot.png

[Contributors][contributors-url] •
[Forks][forks-url] •
[Stargazers][stars-url] •
[Issues][issues-url] •
[MIT License][license-url] •
[Website][website]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/omnivector-solutions/osd-documentation">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Omnivector Slurm Distribution Documentation</h3>

  <p align="center">
    <a href="https://omnivector-solutions.github.io/osd-documentation/master/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/omnivector-solutions/osd-documentation/issues">Report Bug</a>
    ·
    <a href="https://github.com/omnivector-solutions/osd-documentation/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Building the documentation](#Building-the-documentation)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- A modern Python installation
- [sphinx](https://sphinx-doc.org/)

## Building the documentation

1. Clone the repository:
    ```sh
    $ git clone https://github.com/omnivector-solutions/osd-documentation.git
    ```
1. Install the dependencies:
    ```sh
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    ```
1. Build the HTML docs:
    ```sh
    $ make html
    ```

The result is in the `build/html/` directory. Use your favorite browser to open
the [index.html](build/html/index.html).

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Omnivector Solutions - [www.omnivector.solutions][website] - info@omnivector.solutions

Project Link: [https://github.com/omnivector-solutions/osd-documentation](https://github.com/omnivector-solutions/osd-documentation)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)
