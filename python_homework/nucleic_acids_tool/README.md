Tool for simple manipulations with nucleic acids.

1. Reads commands from the user in an endless loop: you can "reverse" - "r" or "transcribe" - "t" your sequence and make "complement" - "c" or "reverse_complement" - "rc"'.
2. After the command, the program prompts the user for the nucleic acid sequence, converts it, and outputs the result.
3. Program preserves case (e.g. complement AtGc is TaCg)
4. Works only with DNA OR RNA, not with mixed.

Tests run from the same directory with 'pytest python_homework/nucleid_acids_tool'
