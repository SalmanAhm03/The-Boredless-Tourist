# The Boredless Tourist

The Boredless Tourist is a Python-based travel recommendation system that helps users discover interesting attractions in various cities based on their personal interests. This project demonstrates core Python concepts such as lists, functions, string formatting, and simple data filtering logic.

## Features

- 🌍 **Destination Indexing**: Maintains a catalog of global destinations.
- 📍 **Attraction Mapping**: Links attractions to destinations with interest-based tags.
- 🧭 **Interest-Based Recommendations**: Suggests attractions based on a traveler's location and interests.
- 🧪 **Sample Traveler Scenarios**: Includes predefined test data for demonstration purposes.

## Getting Started

### Prerequisites

- Python 3.x is installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SalmanAhm03/The-Boredless-Tourist.git
   cd The-Boredless-Tourist
   ```

2. Run the script:

   ```bash
   python boredless_tourist.py
   ```

## Usage

The main script, `boredless_tourist.py`, shows how to:

- Add attractions to destinations
- Tag each attraction with relevant interest categories
- Recommend personalized attractions based on a traveler's interests

### Example

```python
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
recommendations = get_attractions_for_traveler(test_traveler)
print(recommendations)
```

### Output

```
Hi Erin Wilkes, we think you'll like these places around Shanghai, China: Yu Garden, Shanghai Museum.
```

## Project Structure

```
The-Boredless-Tourist/
├── boredless_tourist.py   # Main Python script
└── README.md              # Project documentation
```

## Contributing

Contributions are welcome! If you'd like to enhance the functionality or fix bugs, feel free to fork the repo and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This project was developed as part of Codecademy's Python course. For community discussions and alternative solutions, visit the [Codecademy Forums](https://discuss.codecademy.com/t/the-boredless-tourist/734504).

