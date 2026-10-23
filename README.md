# HTTP Cats

A small Visual Studio Code extension that opens a randomly selected HTTP status-code cat in the built-in Simple Browser. It is a fun way to look up a visual representation of an HTTP response code while you work.

## Usage

1. Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux or `Cmd+Shift+P` on macOS).
2. Run **Http Cats**.
3. The extension opens a random cat from [http.cat](https://http.cat/) in the Simple Browser.

## Requirements

- Visual Studio Code 1.58.0 or later.
- Python 3, used by the extension to start its local service.
- An internet connection to load the cat image.

On first activation, the extension creates a Python virtual environment and installs its required Python packages.

## Development

1. Open this project folder in Visual Studio Code.
2. Press `F5` to launch an Extension Development Host.
3. In the new window, open the Command Palette and run **Http Cats**.

## License

See [LICENSE](./LICENSE).
