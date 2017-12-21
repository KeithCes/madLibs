"""Copyright (c) 2017 * Keith Cestaro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


blankStory = "One day I was walking _1_ from _2_. It seemed like \
just an average _3_. Little did I know, it was actually _4_! I realized \
this after I was _5_ by a _6_ _7_ asking for _8_. At first I wanted to tell \
them to _9_, but after I thought about I decided to give them _10_ instead."
print(blankStory)
print()
print("Input words when prompted to fill their \
respective numbered fields in the story: ")

wordsNeeded = 10
wordOn = 1
words = []
while wordsNeeded > 0:
    print(str(wordOn) + ":")
    x = input()
    words.append(x)
    wordOn += 1
    wordsNeeded -= 1

completeStory = "One day I was walking %s from %s. It seemed like \
just an average %s. Little did I know, it was actually %s! I realized \
this after I was %s by a %s %s asking for %s. At first I wanted to tell \
them to %s, but after I thought about I \
decided to give them %s instead." % (words[0], words[1], words[2],
words[3], words[4], words[5], words[6], words[7], words[8], words[9])
print()
print(completeStory)
