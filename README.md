# RepoPulse - Repository Health Dashboard

RepoPulse is a web-based dashboard designed to monitor the health of your GitHub repositories. It aggregates key metrics such as open issues, pull request activity, and the latest commit information, providing a centralized view of your repositories' status. Built with Python (Flask) for the backend and JavaScript (Chart.js) for the frontend, RepoPulse is a lightweight and extensible tool for developers and teams.

---

## Features

- **Open Issues Tracking**: View the number of open issues for each repository.
- **Pull Request Monitoring**: Track the number of open pull requests.
- **Commit Activity**: See the timestamp of the latest commit.
- **Simple and Intuitive UI**: Clean, card-based layout for easy readability.
- **Extensible**: Easily add more repositories or integrate additional metrics.

---

## Screenshots

![RepoPulse Dashboard](dashboard.png)  
*Example of the RepoPulse dashboard displaying repository health metrics.*

---

## Getting Started

### Prerequisites

- Python 3.x
- Flask (`pip install flask`)
- GitHub API Token (for accessing private repositories or increasing rate limits)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/RepoPulse.git
   cd RepoPulse
   ```

2. **Set Up Environment**:
   - Create a `.env` file in the root directory and add your GitHub API token:
     ```plaintext
     GITHUB_TOKEN=your_github_token_here
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Dashboard**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Configuration

### Adding Repositories

To monitor additional repositories, update the `REPOS` list in `app.py`:

```python
REPOS = [
    {"owner": "owner1", "repo": "repo1"},
    {"owner": "owner2", "repo": "repo2"},
    # Add more repositories here
]
```

### Customizing Metrics

You can extend the `fetch_repo_health` function in `app.py` to include additional metrics like code coverage, code quality scores, or CI/CD status.

---

## API Endpoints

- **`/`**: Renders the dashboard UI.
- **`/api/repo-health`**: Returns a JSON object with repository health metrics.

Example response from `/api/repo-health`:
```json
{
    "owner1/repo1": {
        "open_issues": 5,
        "open_prs": 2,
        "last_commit": "2023-10-01 12:34:56"
    },
    "owner2/repo2": {
        "open_issues": 3,
        "open_prs": 1,
        "last_commit": "2023-09-30 09:12:34"
    }
}
```

---

## Roadmap

- [ ] Add support for code quality metrics (e.g., SonarQube, CodeClimate).
- [ ] Include visualizations for trends over time (e.g., open issues over the last 30 days).
- [ ] Implement user authentication for private repositories.
- [ ] Add notifications for critical metrics (e.g., too many open issues).

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [GitHub API](https://docs.github.com/en/rest) for providing repository metrics.
- [Flask](https://flask.palletsprojects.com/) for the backend framework.
- [Chart.js](https://www.chartjs.org/) for data visualization (optional).

---

Happy monitoring with **RepoPulse**! 🚀
