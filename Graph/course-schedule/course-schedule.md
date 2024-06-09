# Course Schedule

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

## Introduction

The is a simple solution to the infamous course scheduling problem using a topological sort. Fun fact, my professor actually got an internship at Google Inc. by correctly solving this problem during his interview - that lucky devil.

## Methodolgy

* Let's consider the following `prerequisites = [ [0, 1], [0, 2], [1, 3], [1, 4], [3, 4] ]` and `numCourses = 5`

* We can therefore make a dependency graph looking at all this prerequisites:

<img src="" />
