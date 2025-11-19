""" (Functional-Style Programming: What vs. How)
    Why is programming that emphasizes “what” preferable to programming that emphasizes “how”?
     What is it that makes “what” programming feasible?

     Answer: The how is likely reinventing the wheel.. which is not that feasible.

     1. Why “what” (declarative) is preferable to “how” (imperative):
    Clarity & readability: You describe what you want (the goal), not the low-level steps to get there.
    Less error-prone: No need to manually manage indexes, states, or loop control.
    Easier optimization & parallelization: Since the system controls how execution happens, it can automatically choose efficient strategies (e.g., parallel streams, SQL query optimizers).
    Maintainability: Code is shorter, easier to change, and closer to natural problem descriptions.

    2. What makes “what” programming feasible:
    Higher-level abstractions like functions (map, filter, reduce), streams, and query languages hide the low-level iteration.
    Powerful libraries/runtimes implement the “how” efficiently (so you don’t have to).
    Immutability and pure functions allow these operations to be safely optimized and parallelized. """