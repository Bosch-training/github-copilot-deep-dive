# GitHub Copilot – Deep Dive: Lab Guides

## Module 1: Getting Started with GitHub Copilot

### Exercise 1: Design-Pattern Prompting Comparison
**Objective:**
Build a small, real piece of the shared practice project using Copilot, and directly compare how
naming a design pattern in your prompt changes what Copilot generates versus a bare request.

**Prerequisites for this exercise:**
- VS Code with the GitHub Copilot and GitHub Copilot Chat extensions installed and signed in to a
  licensed seat.
- The shared practice project's starter repository **[Placeholder — replace with the real starter
  repository once provisioned]**.

**Steps:**
1. Open a `.java` file in the shared practice project and start typing to confirm Copilot is active — gray suggestion text should appear as you type.
2. Create a new file and write a comment describing a telemetry-reading class with a required vehicle ID and timestamp, plus optional speed, battery level, and GPS fields.
3. Accept Copilot's suggestion and read what it generated.
4. Delete that file's contents.
5. In Copilot Chat, prompt: "Generate this as a Builder pattern, since GPS and battery level are optional."
6. Compare the Builder-pattern result against your first, bare-prompt attempt.
7. In a fresh Copilot Chat thread, ask: "give me a connection manager" and note the result.
8. In a new fresh thread, ask again, naming the pattern: "Generate a Singleton-pattern connection manager for the time-series store."
9. Compare the two connection-manager results side by side, and discuss which prompting habit explains the difference you saw here and in step 6.

**Expected Result:**
The pattern-named prompts (steps 5 and 8) produce recognizably idiomatic code: a private constructor and static accessor for the Singleton, and a fluent builder with optional-field defaults for the Builder. The bare prompts (steps 2 and 7) produce plausible-looking but non-idiomatic versions.

**Troubleshooting:**
- A bare-prompt result that happens to look like a reasonable Singleton or Builder anyway → check specifically for thread-safety (Singleton) and fluent method-chaining (Builder); a plausible match can still be missing these.

---

## Module 2: Apply GitHub Copilot Capabilities

### Exercise 1: Explaining and Modifying Code with Chat and Agent Mode
**Objective:**
Use Copilot Chat to understand an unfamiliar file in the shared practice project, then use Agent
mode to make a reviewed, multi-file change to it.

**Prerequisites for this exercise:**
- The shared practice project from Module 1.

**Steps:**
1. In Copilot Chat, run `/explain` with `#file` referencing a file in the shared practice project you have not read yet.
2. Open that file yourself and check Copilot's explanation against the actual code.
3. Switch to Agent mode and describe a small, genuine multi-file task, for example: "Add a new field to the telemetry-reading class and update every place that constructs one."
4. Review Agent mode's proposed plan before letting it proceed.
5. Review the full diff Agent mode produces before accepting any of it.
6. Run the project's existing tests or build to confirm the change works.

**Expected Result:**
Copilot's `/explain` answer matches what the file actually does. Agent mode's multi-file change is complete — every construction site updated — reviewed, and passes the existing tests or build.

**Troubleshooting:**
No common pitfalls noted for this exercise.

### Exercise 2: Writing a Custom Instructions File
**Objective:**
Write a working repository-wide custom instructions file and confirm it changes Copilot's output
without restating the convention each time.

**Prerequisites for this exercise:**
- The shared practice project, with no `.github/copilot-instructions.md` present in it yet.

**Steps:**
1. Create a file at `.github/copilot-instructions.md` in the shared practice project.
2. Write one real, stable convention this project should follow, for example a specific logging level for recoverable failures.
3. Save the file.
4. Start a new Copilot Chat thread and ask Copilot to generate something small in the project, without restating the convention in your prompt.
5. Check the generated result against the convention you wrote in step 2.

**Expected Result:**
The generated code follows the written convention without you restating it in the prompt.

**Troubleshooting:**
No common pitfalls noted for this exercise.

### Exercise 3: Capstone Project Kickoff and Setup
**Objective:**
Leave this exercise with your team's assigned capstone project named, scoped in one sentence, and
set up — ready for Module 3 onward, where every exercise switches to this project.

**Prerequisites for this exercise:**
- None beyond the course prerequisites.

**Steps:**
1. As a group, review the three named capstone use cases: Vehicle Telemetry Visualization, Digital Twin Assembly-Line Simulation, and Shop-Floor Resource Allocation.
2. Confirm which one your team is assigned or has chosen.
3. Open your team's starter repository for that use case **[Placeholder — replace with the real per-use-case starter repositories once provisioned]**.
4. Confirm every team member has a licensed Copilot seat signed in against that repository.
5. Write a one-sentence MVP scope stating what "done" looks like at the capstone.

**Expected Result:**
Every team has repository access confirmed, Copilot signed in, and a written one-sentence MVP scope.

**Troubleshooting:**
- An MVP scope that's too large (for example, "rewrite our whole auth service") causes re-scoping in every later module → tighten the one-sentence scope now, before moving to Module 3.

---

## Module 3: Code Refactoring with GitHub Copilot

### Exercise 1: Incremental Refactor with a Security Fix
**Objective:**
Refactor a real, working function in your own team's capstone project using an incremental,
verify-each-step discipline, including one security-focused fix, and produce a written before/after
comparison.

**Prerequisites for this exercise:**
- Your team's capstone project, set up in Module 2's kickoff exercise.

**Steps:**
1. In your capstone project, find one genuinely messy or under-tested function.
2. Ask Copilot to identify code smells in that function.
3. Pick one structural problem from Copilot's list to fix first.
4. Ask Copilot to fix only that one problem, referencing the function directly.
5. Review the diff before accepting it.
6. Run the project's existing tests, if any exist yet.
7. Pick a second, separate structural problem and repeat steps 4–6 for it.
8. Identify one plausible input-validation gap in the same function, such as an unchecked field or an unsanitized value.
9. Ask Copilot to add a specific guard for that gap.
10. Review that diff the same way before accepting it.
11. Write a short before/after comparison stating what changed structurally and what the security fix now prevents.

**Expected Result:**
A smaller, more readable, more defensively-written function, reached through individually verified
changes, with a written before/after comparison.

**Troubleshooting:**
- Accepting a large, multi-concern refactor in one step defeats the exercise → if you catch yourself accepting an enormous diff, stop and name which change addresses which problem before continuing.

---

## Module 4: Make Code Production Ready

### Exercise 1: CI Workflow and Test Suite Generation
**Objective:**
Generate a working GitHub Actions workflow for your capstone project, and a real test suite —
including edge cases — for a function within it.

**Prerequisites for this exercise:**
- Your capstone project, now carrying Module 3's refactor.

**Steps:**
1. Ask Copilot to generate a GitHub Actions workflow that runs your project's test suite on every pull request.
2. Review the generated YAML before committing it.
3. Commit the workflow file.
4. Pick a target function in your project that has no tests yet.
5. Ask Copilot to generate unit tests for that function, explicitly requesting edge and negative cases, not only the happy path.
6. Run the generated tests.
7. Check whether the test suite actually covers an edge case beyond the happy path.

**Expected Result:**
A committed CI workflow, and a passing test suite that includes at least one genuine edge or
negative case.

**Troubleshooting:**
- A generated test suite that only covers the happy path can look complete at a glance → explicitly check for at least one edge or negative case before accepting the suite as done.

### Exercise 2: Documentation and Code Review Pass
**Objective:**
Produce class/method-level and API documentation for your tested code, then open a pull request
and get a Copilot code review on it.

**Prerequisites for this exercise:**
- The tests from Exercise 1 must already exist and pass.

**Steps:**
1. Ask Copilot to generate class-level and method-level documentation for the function from Exercise 1.
2. If that function is exposed as an API endpoint, ask Copilot to generate its API documentation too.
3. Review the generated documentation against the real code for accuracy.
4. Open a pull request containing this module's changes.
5. Request a Copilot code review on the pull request.
6. Read every comment Copilot's review leaves.
7. For each comment, either address it or note why you're consciously dismissing it.

**Expected Result:**
Documentation a reviewer could actually use, and at least one Copilot code review comment addressed
or consciously dismissed.

**Troubleshooting:**
No common pitfalls noted for this exercise.

---

## Module 5: Advanced Topics

### Exercise 1: Content Exclusion and Planted-Issue Review
**Objective:**
Configure a content-exclusion rule on the shared practice sample, and identify a planted issue in
AI-generated code through your own review.

**Prerequisites for this exercise:**
- None beyond the course prerequisites. This exercise uses the shared sample provided for the whole
  room, not your own capstone project — every team reviews the identical, pre-verified issue.

**Steps:**
1. Open the shared content-exclusion configuration sample for one sensitive path **[Placeholder — replace with the real sample content-exclusion configuration once finalized]**.
2. Configure a content-exclusion rule for that path.
3. Confirm, or discuss with your facilitator if live verification isn't possible, what that rule changes about what Copilot can use as context there.
4. Open the shared planted-issue sample **[Placeholder — replace with the real planted-issue sample once finalized]** and review it as though it were an incoming pull request.
5. Identify the issue through your own read, independent of whether an automated review also flags it.
6. Write down specifically what a reviewer should look for to catch this issue.

**Expected Result:**
A configured (or discussed) content-exclusion rule, and a written note naming the planted issue and
what a reviewer should look for.

**Troubleshooting:**
- If the planted issue felt impossible to find or too obvious → tell your facilitator; its difficulty is meant to sit between "too easy" and "too demoralizing," and may need recalibrating.

### Exercise 2: Reviewing Your Own Capstone Project
**Objective:**
Apply this course's review habits to your own capstone project, and write a personal takeaway
naming what you'll use next and where.

**Prerequisites for this exercise:**
- Your capstone project, carrying Modules 2–4's work.

**Steps:**
1. Check whether a code-referencing license match has surfaced during any of your Modules 3–4 hands-on work.
2. If one has surfaced, open it and check the attributed license before deciding whether to keep that suggestion.
3. If none has surfaced, pick your capstone project's riskiest file and do a short review pass on it, applying the "what should a reviewer look for" habit from Exercise 1.
4. Write a one-page personal takeaway naming which of this course's modes — inline completion, Chat, Agent mode, the CLI, code review — you will actually use next, and why.
5. In that takeaway, name the specific place in your capstone project or your regular work where you'll apply it first.

**Expected Result:**
One real review pass completed on your own capstone project, and a written, specific personal
takeaway.

**Troubleshooting:**
No common pitfalls noted for this exercise.

---

## Capstone: Finish, Harden, and Present the MVP

### Exercise 1: Finish, Harden, and Present Your MVP
**Objective:**
Finish your team's capstone project into a demonstrable MVP, and present it with concrete
observations on where Copilot helped, where it went wrong, and what you'd do differently.

**Prerequisites for this exercise:**
- Your capstone project, already carrying Module 3's refactor and Module 4's CI/CD-and-test pass.

**Steps:**
1. Reconvene as your team and reconfirm your one-sentence MVP scope from Module 2's kickoff exercise.
2. Adjust that scope if three modules of real work showed it was too big or too small.
3. Close any remaining gaps in your MVP using whichever Copilot technique the remaining work calls for.
4. Confirm your CI workflow and test suite still pass end to end.
5. Run a last review or content-exclusion check on anything sensitive in the project.
6. Deploy the MVP to the confirmed target environment, or prepare it ready to deploy **[Unverified — confirm the intended deployment target and runtime with the course owner before this capstone runs]**.
7. Prepare a short presentation covering what you built, where Copilot genuinely accelerated you, where it produced something confidently wrong that review caught (or didn't, until later), and what you'd do differently on a real team project.
8. Present to the room.
9. As a group, capture which of this course's modes each person will actually reach for on their next real task.

**Expected Result:**
A working, demonstrable MVP — already refactored, tested, and reviewed — presented with specific,
concrete observations.

**Troubleshooting:**
- A team that fell behind in Module 3 or 4 arrives here with an unrefactored or untested project → flag this to your facilitator early; this block is meant for finishing, not starting those passes from scratch.
