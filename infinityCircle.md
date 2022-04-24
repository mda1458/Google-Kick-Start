Let us assume for the simplicity of this problem that the Infinity symbol is made of circles which touch externally at point S as shown below, and let us call it the center of the infinity.

You are given three integers R, A, B. You are currently at the center of the infinity. You will first start drawing the right circle with radius R and reach again the center of infinity. After that, you start drawing the left circle with the radius equal to the radius of last circle multiplied by A. After reaching the center of the infinity you again start drawing the right circle with radius equal to the radius of last circle divided by B (integer divison). After reaching the center of infinity you again draw the left circle with the radius equal to the radius of last circle multiplied by A.

Steps to create the infinity symbol with three circles.

You continue to draw the left and right circles as described above until the radius of the circle to be drawn becomes zero. Calculate the sum of areas of all the circles drawn. It is guaranteed that the process will terminate after finite number of steps.

## Input
The first line of the input gives the number of test cases, T. T lines follow.

Each line represents a test case and contains three integers R, A, B, where R denotes the radius of the first circle, and A and B are the parameters used to calculate the radii of the subsequent circles.

## Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the sum of areas of all the circles drawn until radius of the circle to be drawn becomes zero.

y will be considered correct if it is within an absolute or relative error of 10−6 of the correct answer. See the FAQ for an explanation of what that means, and what formats of real numbers we accept.

## Limits
Time limit: 20 seconds.

Memory limit: 1 GB.


