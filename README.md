<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rocket League Bot Setup</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
            color: #333;
        }

  .container {
      max-width: 800px;
      margin: 50px auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 5px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }

  h1 {
      color: #333;
      text-align: center;
  }

  p {
      line-height: 1.6;
  }

  code {
      background-color: #f2f2f2;
      padding: 2px 5px;
      border-radius: 3px;
      font-family: "Courier New", Courier, monospace;
  }

  .steps {
      margin-top: 20px;
  }

  .steps ol {
      list-style-type: decimal;
      padding-left: 20px;
  }
  </style>
</head>

<body>

  <div class="container">
      <h1>Rocket League Bot Setup</h1>
      <p>This repository contains a bot for Rocket League. Follow the steps below to set it up:</p>

  <div class="steps">
      <ol>
          <li>Ensure Rocket League is installed on your system.</li>
          <li>If Rocket League is installed, follow these steps:</li>
          <ol>
              <li>Open CMD.</li>
              <li>Run the following commands:</li>
              <code>python -m pip install rlbot_gui rlbot eel</code>
              <code>python -c "from rlbot_gui import gui; gui.start()"</code>
              <li>(Optional) Create a .bat file with the command from step 3 and execute it.</li>
              <li>Once the GUI loads, click "Add" and load the folder containing your bot.</li>
              <li>Drag the bot to the orange and blue team.</li>
              <li>Run the program.</li>
          </ol>
          <li>If Rocket League is not installed:</li>
          <ol>
              <li>Install Epic Games Launcher.</li>
              <li>Download Rocket League.</li>
          </ol>
      </ol>
  </div>
  </div>

</body>

</html>
