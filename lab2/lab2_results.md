# Names: Careney and Riley
# Lab: Lab2 (Intermediate Prompt Engineering)
# Date: 10/10/2025

1. Zero-Shot and Few-Shot:

When would you choose zero-shot?
-When you don't have examples
-For quick testing
-When the task is simple


When is few-shot worth the extra effort?
-When you have good examples
-When zero-shot doesn't work well
-For important tasks that need better accuracy

How did the classification output change from Task 3.11 Task 3.12
- I only noticed one inaccurate classification: Ollama started misclassifying the "You are the lucky winner!" email as IMPORTANT instead of SPAM.
-The model learns from examples. If you give it bad examples, it learns the pattern. Even one wrong example can make it get similar emails wrong. Good examples = good results.

How did the generated code change from Task 3.21 to Task 3.22?
- The computer gave me different answers each time I asked for the same thing. The "find max" function kept changing, sometimes it was short and simple, other times it was longer with more steps. The other two functions stayed exactly the same every time. It's like when you ask people the same question and get slightly different answers each time.