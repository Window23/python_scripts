""" (Functional-Style Programming: Internal vs. External Iteration) Why is internal iteration preferable to external iteration in functional-style programming?

    Answer:
    External iteration means you (the programmer) control the iteration explicitly — e.g.,
    using a for or while loop. You tell the program when to move to the next element, when to stop, etc. This is imperative style.

    Internal iteration means you hand over the control of iteration to the library/framework — e.g.,
    calling .forEach(), .map(), .filter(), or a stream operation. You only provide the behavior (the function to apply),
    and the library decides how to loop internally. This is functional style. """