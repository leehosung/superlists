# superlists

이 저장소는 Test-Driven Development with Python 을 읽으면서 작성하는 코드들을 보관합니다. 
이 README 파일에는 각 장별로 중요한것들을 모아 둡니다. 

## Chapter1

- "Test first, test first!" 

## Chapter2

- Functional Test == Acceptance Test == End-to-end Test

## Chapter3

- the functional tests are driving what development we do from a high level, while the unit tests drive what we do at a low level
- Functional tests should help you build an application with the right functionality and guarantee you never accidentally break it. Unit tests should help you to write code that's clean and bug free.

## Chapter4

- One of the great things about TDD is that you never have to worry abount forgetting what to do next - just rerun your tests and they will tell you waht you need to work on.
- Don't Test Constants : Unit tests are really about testing logic, flow control, and configuration
- Refactoring is trying to iprove the code without changing its functionality.
- When refactoring, work on eighter the code or the tests, but not both at once.
- Refactoring Cat <-> Testing Goat.

## Chapter5

- Setup, Exercise, Assert is the typical structure for a unit test. group them with a line spacing
- Red, Green, Refactor
    - Start by writing a unit test which fails (Red)
    - Write the simplest possible code to get it to pass (Green), even if that means cheating.
    - Refactor to get to better code that makes more sense. 
- Don't repeat yourself (DRY)
- three strikes and refactor
- before you do any refactoring, always do a commit 
- Always redirect after a POST
- Useful TDD concepts
    - regression
    - unexpected failure
    - red/green/refactor
    - triangulation
    - three strikes and refactor
    - the scratchpad to-do list
    
## Chapter6

- Small design when necessary
- YAGNI: You aint gonna need it 
- REST : Representational State Transfer
- from working state to working state
- fixing that and only that
- URLs without a trailing slash are "action" URLs which modify the database
- use assertRedirects to check a redirection after a POST

## Chapter7

- check the smallest style to get the confidence that the rest of the styling for that page is probably loaded too.
- use assertAlmostEqual
- you shouldn't write tests for design and layout

