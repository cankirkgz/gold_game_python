<h1>Golden Game</h1>
    <p>Golden Game is a strategic two-player game developed using Python with Tkinter for the graphical user interface and SQLite for data storage. The game involves players selecting characters with unique strategies to compete against each other, earning or losing gold based on their moves.</p>
    
  <h2>Overview</h2>
    <p>In Golden Game, each player starts with 10 gold and can choose from five distinct characters, each with their own strategy:</p>
    <ul>
        <li><strong>Kopyacı</strong>: Copies the last move of the opponent.</li>
        <li><strong>Ponçik</strong>: Always chooses to 'give'.</li>
        <li><strong>Çakal</strong>: Always chooses to 'take'.</li>
        <li><strong>Gözükara</strong>: Chooses 'take' if it has been used previously; otherwise, 'give'.</li>
        <li><strong>Sinsi</strong>: Chooses 'give', then 'take', and so forth in a specific pattern.</li>
    </ul>
    <p>The game consists of up to 10 rounds, with players making strategic choices each round to accumulate gold.</p>
    
  <h2>Features</h2>
    <ul>
        <li><strong>Character Selection</strong>: Choose from five different characters with unique strategies.</li>
        <li><strong>Round Play</strong>: Play up to 10 rounds, with each round updating players' gold based on their moves.</li>
        <li><strong>Database Storage</strong>: Game results and round details are saved in an SQLite database.</li>
        <li><strong>GUI</strong>: User-friendly interface built with Tkinter for game control and display.</li>
    </ul>
    
  <h2>Getting Started</h2>
    
  <h3>Requirements</h3>
    <ul>
        <li>Python 3.x</li>
        <li>Tkinter (usually comes with Python)</li>
        <li>SQLite (included with Python's standard library)</li>
    </ul>
    
  <h3>Installation</h3>
    <pre><code>git clone https://github.com/yourusername/golden-game.git
cd golden-game
python golden_game.py
    </code></pre>
    
  <h3>Usage</h3>
    <ul>
        <li><strong>Start the Game</strong>: Select the characters for Player 1 and Player 2 from the dropdown menus and click "Start Game".</li>
        <li><strong>Play Rounds</strong>: After starting the game, click "Start Round" to play each round. The game will update with the current state after each round.</li>
        <li><strong>View Results</strong>: The results of each round are displayed on the screen, and the final results will be shown when the game ends.</li>
    </ul>
    
  <h2>Customization</h2>
    <p>Feel free to modify the code to add new features, characters, or mechanics. For example, you can:</p>
    <ul>
        <li>Add new character types by creating new classes.</li>
        <li>Change game rules or mechanics.</li>
        <li>Enhance the GUI with additional features.</li>
    </ul>
    
  <h2>Troubleshooting</h2>
    <p>If you encounter any issues:</p>
    <ul>
        <li>Ensure that all dependencies are installed and that you are using Python 3.x.</li>
        <li>Check the console for error messages that can provide clues to any problems.</li>
        <li>Refer to the <a href="https://docs.python.org/3/library/tkinter.html">Tkinter documentation</a> and <a href="https://www.sqlite.org/docs.html">SQLite documentation</a> for help with related issues.</li>
    </ul>
    
  <h2>Contributing</h2>
    <p>Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow the coding standards and include tests for new features.</p>
    
  <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
