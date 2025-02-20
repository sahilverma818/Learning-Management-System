import React from 'react';
import './VideoComponent.css';
import ReactMarkdown from 'react-markdown';


const VideoComponent = () => {

  const description = `
  # Day 1 - What is Programming and Python?
  
  ## What is Programming
  
  Welcome to my course on Python programming. If you know me, you know that I always start a beginner Python class with a fundamental question - **"What is Programming?"**
  
  Programming is a way for us to tell computers what to do. The computer is a very dumb machine and it only does what we tell it to do. Hence, we learn to program and tell computers to do what we are very slow at - computation.
  
  If I ask you to calculate \`5+6\`, you will immediately say \`11\`. How about \`23453453 X 56456\`? You will start searching for a calculator or jump to a new tab to calculate the same.
  
  This **100 Days of Code** series will help you learn Python from the beginning to the end. We will start from zero, and by the time we finish this course, I promise you will be a **job-ready Python developer!**
  
  ---
  
  ## What is Python?
  
  Python is a **dynamically typed, general-purpose programming language** that supports an **object-oriented** programming approach as well as a **functional programming** approach.
  
  Python is an **interpreted** language (meaning, the source code of a Python program is converted into bytecode that is then executed by the Python virtual machine) and a **high-level programming language**.
  
  It was created by **Guido Van Rossum** in **1989**.
  
  ### Features of Python:
  - Python is **simple** and **easy to understand**.
  - It is **interpreted** and **platform-independent**, which makes debugging very easy.
  - Python is an **open-source** programming language.
  - Python provides **extensive library support**. Some popular libraries include **NumPy, TensorFlow, Selenium, OpenCV, etc.**.
  - It is possible to **integrate other programming languages** within Python.
  
  ### What is Python used for?
  - **Data Visualization** to create plots and graphical representations.
  - **Data Analytics** to analyze and understand raw data for insights and trends.
  - **AI and Machine Learning** to simulate human behavior and learn from past data without hard coding.
  - **Web Development** to create web applications.
  - **Database Management** to work with various databases.
  - **Business and Accounting** to perform complex mathematical operations along with quantitative and qualitative analysis.
  
  ---
  
  ## In this tutorial, we will use Replit to create a Python program
  
  ### Why Replit?
  - **Replit is an online IDE** that is very easy to write code in.
  - Replit also offers a **robust mobile app** that works great (*Personal experience*).
  - You can **easily fork** this Repl and continue learning in your own style.
  
  ---
  
  #### Setting up Replit
  
  ##### Step 1: Open your web browser and visit the [Replit website](https://replit.com)
  
  ##### Step 2: Replit page will appear, Click on **Sign In**, and create a new account. If you already have an account, click on **Log In**.
  
  ##### Step 3: After logging into your account, click on **"Create Repl"**.
  
  ##### Step 4: This dialog box will appear, search for **Python** and click on **"Python"** from the dropdown.
  
  ##### Step 5: Give the name of the new Repl in the title and click on **"Create Repl"**.
  
  ##### Step 6: This page will appear, and by default, the \`main.py\` file will be present in the Replit template. This is where you can start writing Python code.
  
  ##### Step 7: In the \`main.py\` file, write the following code:
  
  \`\`\`python
  print("Hello World")
  \`\`\`
  
  Click on the **Run** button to show the output in the **Console** box.
  
  ### Output:
  \`\`\`
  Hello World
  \`\`\`
  
  This is how you can create a program in Python and run it on the console.
  
  ---
  
  The **download and installation process** are given in the next lesson.
  `;
  
  return (
    <div className="video-content">
      <h1>Day 1 - What is Programming and Python?</h1>
      <div className="video-player">
        <iframe 
          src="https://www.youtube.com/embed/videoid" 
          title="Day 1 - What is Programming and Python?"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
        ></iframe>
      </div>
      <div className="video-description">
        <ReactMarkdown>{description}</ReactMarkdown>
      </div>
    </div>
  );
};

export default VideoComponent;
