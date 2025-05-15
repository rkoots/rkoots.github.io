---
layout: default
title: "Python Quiz - Get Your Certificate"
date: 2025-05-12
categories: guide
author: "RK"
tags: [bootstrap, frontend, web development]
keywords: [bootstrap 5, frontend tutorial, responsive design, CSS framework]
---

# Python Quiz

Test your knowledge on Python! After you complete the quiz, you'll receive your score, and if you score above 80%, you'll be awarded a certificate.

## Quiz Instructions:

1. Answer all questions.
2. Submit your answers by clicking the "Submit" button at the end.
3. You will receive a score and, if it is above 80%, you will get your certificate.

---

<div id="quiz-container">
  <form id="quiz-form">
    <h3>Question 1: What is Python?</h3>
    <label><input type="radio" name="q1" value="a"> A programming language</label><br>
    <label><input type="radio" name="q1" value="b"> A snake</label><br>
    <label><input type="radio" name="q1" value="c"> A coffee drink</label><br>

    <h3>Question 2: What is a list in Python?</h3>
    <label><input type="radio" name="q2" value="a"> A data structure to store multiple items</label><br>
    <label><input type="radio" name="q2" value="b"> A loop type</label><br>
    <label><input type="radio" name="q2" value="c"> A mathematical operation</label><br>

    <h3>Question 3: What does 'def' do in Python?</h3>
    <label><input type="radio" name="q3" value="a"> Defines a function</label><br>
    <label><input type="radio" name="q3" value="b"> Declares a variable</label><br>
    <label><input type="radio" name="q3" value="c"> Displays output</label><br>

    <br><br>
    <button type="button" onclick="submitQuiz()">Submit</button>
  </form>
  <div id="result"></div>
  <div id="certificate" style="display:none; margin-top:20px;">
    <h2>Congratulations! You've earned your Certificate!</h2>
    <p>Your score is above 80%!</p>
  </div>
</div>

<script>
  function submitQuiz() {
    const answers = {
      q1: 'a',  // Correct answer for question 1
      q2: 'a',  // Correct answer for question 2
      q3: 'a'   // Correct answer for question 3
    };

    let score = 0;
    const form = document.getElementById('quiz-form');

    // Check answers
    for (let i = 1; i <= 3; i++) {
      const question = `q${i}`;
      const userAnswer = form.querySelector(`input[name="${question}"]:checked`);
      if (userAnswer && userAnswer.value === answers[question]) {
        score++;
      }
    }

    // Calculate score percentage
    const percentage = (score / 3) * 100;

    // Show result
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `<p>Your score: ${percentage}%</p>`;

    // Show certificate if score > 80
    const certificateDiv = document.getElementById('certificate');
    if (percentage >= 80) {
      certificateDiv.style.display = 'block';
    } else {
      certificateDiv.style.display = 'none';
    }
  }
</script>
