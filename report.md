# Report for assignment 4

## Project

Name: Toga

URL: https://github.com/beeware/toga

Toga is a cross platform GUI toolkit. It consists of a library of base components with a shared interface to simplify platform-agnostic GUI development.

## Onboarding experience

Our initial plan was to continue with the same project that we used for the previous assignment. Searching for issues we realized that the project lacks a lot of documentation and that the current issues are either to small or too complex to fix within the scope of this assignment. We therefore decided to look for different repositories and finally selected the Toga repo, because of it's extensive documentation and beginner-friendly usability for contribution. The setup of the project was quite straight-forward and we could easily find issues to work on with the label filtering on github. We finally decided to choose and issue that was both well described and seemed appropriate to work on in the scope of this assignment.

## Effort spent

For each team member, how much time was spent in

1. plenary discussions/meetings;

2. discussions within parts of the group;

3. reading documentation;

4. configuration and setup;

5. analyzing code/output;

6. writing documentation;

7. writing code;

8. running code?

For setting up tools and libraries (step 4), enumerate all dependencies
you took care of and where you spent your time, if that time exceeds
30 minutes.

## Overview of issue(s) and work done.

### Issue #2144

Title: Configurable text line height in Canvas 

URL: https://github.com/beeware/toga/issues/2144

The `write_text` and`measure_text` methods in Canvas support multiple lines but lack control over line spacing. Adding a`line_height` argument, similar to CSS, would allow users to specify spacing as a multiple of the font size for better text layout control.

Scope (functionality and code affected).
To change this, the core (interface layer) is affected 

### Issue #2145

Title: Configurable text line height in Label

URL: https://github.com/beeware/toga/issues/2145

What is the problem or limitation you are having?
The Label accepts multiple lines, but there's no way to control their spacing.

Describe the solution you'd like
A line_height style with the same meaning as in CSS. See #2144 for a specification.

Describe alternatives you've considered
The user can split their text into multiple Labels, but because they can't be overlapped, there will be a certain minimum spacing that they can't go below.

Additional context
Compared to Canvas (#2144), the Label version of this feature would be more work to implement, but probably useful to more people.

Scope (functionality and code affected).


## Requirements for the new feature or requirements affected by functionality being refactored

Optional (point 3): trace tests to requirements.

## Code changes

### Patch

(copy your changes or the add git command to show them)

git diff ...

Optional (point 4): the patch is clean.

Optional (point 5): considered for acceptance (passes all automated checks).

## Test results

Overall results with link to a copy or excerpt of the logs (before/after
refactoring).


## UML class diagram and its description

### Key changes/classes affected

Optional (point 1): Architectural overview.

#### Core API - Canvas:
![classes_canvas](https://github.com/user-attachments/assets/fd89b88f-3903-46b6-a68f-579c1ca343ec)

#### Backend - Windows: 
![classes_windows](https://github.com/user-attachments/assets/4599bf39-775a-4073-9195-c8398f44fbb5)

Optional (point 2): relation to design pattern(s).

## Overall experience

What are your main take-aways from this project? What did you learn?

How did you grow as a team, using the Essence standard to evaluate yourself?

Optional (point 6): How would you put your work in context with best software engineering practice?

Optional (point 7): Is there something special you want to mention here?
