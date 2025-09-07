# Internet Cafe Inventory Management

This project is a command-line inventory management system for a small internet cafe. It allows the user to manage items and suppliers through a console interface. All data is saved to and loaded from local text files (`items.txt` and `dealers.txt`), ensuring data persistence between sessions.

## Core Features

### Item Management
*   **Add, Delete, and Update Items**: Perform full CRUD (Create, Read, Update, Delete) operations for inventory items.
*   **Input Validation**: All user inputs are validated to prevent errors. For example, item codes must be unique and numeric, prices must be positive numbers, and dates must follow the `YYYY/MM/DD` format.
*   **View Items**: Displays a formatted table of all inventory items, sorted alphabetically by category. It also calculates and shows the total value of the entire inventory.

### Dealer Management
*   **Load Dealers**: Loads a list of potential dealers from `dealers.txt`.
*   **Random Selection**: Randomly selects four dealers from the available list, simulating a process for choosing suppliers.
*   **View Dealers**: Displays the details of the four randomly selected dealers, sorted alphabetically by location.
*   **View Dealer's Items**: Shows all items offered by a specific, user-selected dealer.

### Data and Sorting
*   **File-Based Storage**: All inventory and dealer information is stored in plain text files (`items.txt` and `dealers.txt`), making the data easy to view and edit outside the application.
*   **Custom Sorting**: The application uses a custom-implemented bubble sort algorithm to organize items by category and dealers by location, as per the project's constraints.

## How to Run

1.  Ensure you have Python installed.
2.  The script will automatically create `items.txt` and `dealers.txt` if they don't exist.
3.  Run the main script from your terminal:
    ```sh
    python internet_cafe.py
    ```

## Author

*   GitHub: [p-sahas](https://github.com/p-sahas)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
