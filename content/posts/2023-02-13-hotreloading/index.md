---
title: "Hot-Reloading like it's 1972"
date: 2023-02-13T00:00:00-08:00
draft: false
thumbnail: "smalltalk.png"
---

TL;DR Here's a sketch of a solution for hot-reloading that I hope will bring some greater flow to my
development process.  Present day solutions are more about shipping the final product, than they are
about enjoying the process of coding.  Hot-reloading is one of those features that once you have it,
you just don't want to live without it again.  So let's get hot-reloading like it's 1972!

<!--more-->

## Some hot-reloading please

[Smalltalk](https://en.wikipedia.org/wiki/Smalltalk) was revolutionary when it came out.  It was
totally unlike anything that had come before.
It wasn't perfect, but what it was changed how people thought about personal computing, influencing
much that came later.  Some have speculated on why Smalltalk wasn't more broadly adopted, but we
will never really know.  What I do know is that Smalltalk was very cool in 1972, and we don't have
anything close to that today.  We certainly have some cool technology.  But what we lack is the
experience Smalltalk provided to the developer.  This was during a time when punch cards were still
in active use.  I think we have lost some of what Smalltalk was supposed to be, and I'm interested
in what it would take to have something similar today.

<a title="Smalltalk Demo, Image, CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://www.youtube.com/watch?v=uknEhXyZgsg"><img width="256" alt="Smalltalk-76.blowup" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Smalltalk-76.blowup.png/256px-Smalltalk-76.blowup.png"></a>

The specific feature I'm interested in is
the ability for Smalltalk to modify it own code while running.  This sounds outrageous to us today.
Almost foreign.  Something you might only see in a toy, not a production ready computing system.
But if you think about it, we actually do this all the time when working on large distributed
systems.  We are constantly modifying the code of the actors within the system while the entire
system continues to run.  There's zero downtime in modern internet based systems.  And there's an
army of developers behind the scenes working to make sure that continues to be the case.  Continuous
Delivery normalized this, and it's the standard today for SaaS applications.

What a developer mostly does is edit some files, with the help of some clever IDE tools.  The
compiler then builds and links the code into a final executable.  At which time tests are run, or
the application is started for manual testing.   In my early C++ days, it wasn't uncommon to wait
several minutes for the application to build before I could verify my changes.  It was tedious
work, and it lacked a sense of flow that I longed for.   As a kid, I programmed on a Commodore Vic 20,
using a primitive Basic that only supported line editing.  But with only that, I was able to create
some interesting programs for a kid.  There was no development cycle.  The changes I made were
almost instantaneous.  That's one of the advantages of interpreted languages is that sense of
instant feedback.  Those atrocious C++ build times are a big reason why dynamic languages really
took off in the 90s.  The trade-off with the fast start up times of those dynamic languages was very
compelling, and sparked a lot of exploration.

<a title="StickyChannel92, CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Commodore_Vic-20_Splash.png"><img width="512" alt="Commodore Vic-20 Splash" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Commodore_Vic-20_Splash.png/512px-Commodore_Vic-20_Splash.png"></a>

One of the possible reasons why Smalltalk didn't take off was likely because dynamic languages were
able to do much of what Smalltalk did, without many of it's limitations.  The ability to quickly
prototype an idea and see it in action is something developers wanted.  Tcl (1988),  Python (1991),
Ruby (1995) came out providing instant start up times and live interaction through the REPL.  This
sort of thing has been around since the early days of Lisp, but computers with better graphical
displays kicked off the computer hobbyist revolution,  Lisp didn't quite make it into the
mainstream.  It was something you did at University.  (Some notable exceptions of course).

So that's my superficial take on the last 50 years of programming languages.  What I really want to
know is what is it going to take to bring that sense of programming flow back to my work.  The
feeling like I'm affecting things immediately.  The ability to quickly explore new ideas and try new
things.  But mostly, the ability to not have to wait to see the results of my changes.

Dynamic and scripted languages are definitely an option.  I have
worked in python for 20 years and I love it, but I never want to build anything big in it every
again.  Optional types in Python 3 make things tolerable.  But compared with a proper type system
like in Rust, the short term gains you get at the beginning of a project are lost later on as
complexity rises.  You hit your complexity threshold sooner with untyped languages.

The gamedev world has come up with a lot of clever solutions to get hot reloading to work in C++.
So I know there are other developers who are interested in this sort of working with near instant
feedback loops.  In gamedev back in the day, it wasn't uncommon to be waiting hours for your program
to build.  Being able to hot-reload can be a huge time saver.  Most of these techniques are limited,
and come with restrictions like not being able to modify the function signature, or modify structs
in any way.  But for game dev, that's often fine, and plus, what choice do we have?  The options in
C and C++ are limited.  [Handmade Hero](https://handmadehero.org/) is an example of a game that was
developed on a live stream, [and it featured hot-reloading that the author built
himself](https://www.youtube.com/watch?v=Pax5jIz6m_Q).

There are lots of reasons why hot-patching code might be helpful, but what gets me interested is the
chance to improve my development flow while using statically typed languages, such as Rust or C++.  I
can get this already with Python, but that's not what I want to use all the time.

Other interesting
uses might include dealing with large state files that take a long time to load.  This was one of
the big reasons for  one of the Jupyter notebooks.  In Jupyter, you can load your data files into
the kernel, and then do
exploratory work from there.  It's a great way for data scientists to explore their data.  The final
reason this is interesting to me is because it's something that should be possible, but isn't.
[Pharo](https://www.pharo.org/), a modern open source implementation of Smalltalk, can edit it's entire system, even the JIT
based VM it runs on.  That's impressive.   I'm not interested in programming in Smalltalk through,
so unfortunately I'm out of luck. So let's see what it will take to make these goodies possible.

Here's a screenshot of a Juptyer session exploring COVID data.  The data set was large, but I was
able to query the data in ways that were helpful to me in the early days of the pandemic to
understand the scale of the problem.

[![COVID Jupyter](jupyter.png)](https://github.com/rrx/COVID-19/blob/master/analysis.ipynb)

In C++, there's usually some sort of variation on the `dlopen` approach, which is quite simple.  It
involves watching for changes in shared libraries, and then getting the updated functions from the
modified library so they can be called.

Here's some pseudo-code to describe the a simplified version of the `dlopen` approach:

```python
loop:
  lib = dlopen("hotreload.so")
  f = dlsym(lib, "func")
  loop:
    f(0)  # call the new function
    if changed("hotreload.so"):
      break
```

This method is easy to use in simple cases where the functions have simple parameters.  You don't
have to consider changes in the function signatures.  If you did change the function signature, it
would have undefined behavior.  While incredibly powerful, I'm hoping to go much further.

## My Wish list

So I've come up with my wish list for features I'm looking for in a language or system that supports
hot-reloading.  Something like Smalltalk, Emacs, or live-reloadable SPAs, but closer to native, and
to the tools I want to use.  I know a lot of these features are available here and there in
different languages and products.  Rather than reinventing the wheel, I want to come up with
something that doesn't exist yet.  I program a lot in Rust these days, and my C++ has gotten a bit
rusty you could say.  So I'm hoping for a solution close to that world.  Hot-reloading in Rust is
possible using the `dlopen` approach, but I think we can do better than that.

- Provide hot-reloading that's both fast and safe.  And by safe, I mean memory safety issues, such
  crashes due to accessing data after it's been freed.  And by fast, I mean something close to C++
  in performance.
- Safe interop with C based libraries.
- No VMs if possible.   VM's can provide some great solutions, but they abstract you from the
  hardware, and tie you into specific ecosystems.  I'm hoping to stay as close to the metal as
  possible, so that things like hot-reloading device drivers could be a possibility. (Bad idea?
  Maybe).
- Have the ability to modify my statically compiled editor or IDE while it's running.  Modifying an
  interpreted one is too easy, and also too slow. Emacs allows this, and is a big inspiration, but
  at the end of the day, I don't enjoy that world.
- Hot-reloading is a zero cost abstraction.  This means that if I disable hot-reloading, there should
  be no performance penalty.  For example, if I disable the feature in the release build, it should
  have performance close to C++.
- Ability to hot-reload on embedded devices safely by uploading compiled code fragments over serial.
- Provides near instantaneous feedback on changes to code.  Possibly bypassing the filesystem
  altogether, compiling code in the buffer and swapping to it without even hitting save.
- Provide a rich debugging experience which allows you to debug your application while it's running.
  This is is pretty common.  But combined with safely hot-patching of code, and stack restarts, this can be
  a very powerful thing.
- Deep integration with the editor and IDE, by providing a stable hot-patching API that can be used to build an
  application on a running application.  This API could be used to build a REPL as well for live
  coding in a session.
- Provides a "Playground" like Swift.  These are incredible tools for productivity, and every
  developer should have access to them.
- Be able to access data in memory in such a way that it can be graphically visualized in real-time,
  allowing the ability to visualize large, or fast moving datasets.
- Be able to modify any part of the running code, which could include things like the compiler or
  device drivers.  This could break everything, but as long as you can disable that ability in the
  final product, it's a tool to speed up development and foster an environment of exploration and
  innovation.  This includes the ability to modify structures and function signatures, something
  that is almost impossible using other methods.  It's possible though, as proven by the [Mun
  language](https://docs.mun-lang.org/ch04-04-hot-reloading.html)
- Must have bounded memory.  It's not much use if you run out of memory eventually because you never
  release code that's been run.  The trick here is to make sure it will never be run again before
  releasing it.

At the end of the day, I want to be able build a cathedral of code without ever having to restart
the program.  It sounds impossible, in an age where the solution to most computer problems is to
restart your computer.  But this post is all about a dream.  And there's no technical reason why it
can't be done.  While this might not be possible in Rust or C++ yet, here's how I think it might
work.


## Methods

There are three methods that can be used to accomplish live hot-patching of code that I've been able
to identify.
- Code Rewriting
- Function Hooks
- Functions with non-static lifetime

### Code Rewriting

Code Rewriting at a high level means wrapping code in a lock, and then rewriting the code in place.
This really only works if the code you are rewriting in place is the same size or smaller than the
existing code.  You can get around this by only writing a jump instruction to the location of your
code.  There are some commercial and research solutions that do just this in order to do dynamic binary
instrumentation.  Some examples are [Pin](https://www.intel.com/software/pintool/) and
[Dyninst](https://www.dyninst.org).

[According to the authors of this
paper](https://pldi16.sigplan.org/details/pldi-2016-papers/28/Living-on-the-edge-Rapid-toggling-probes-with-cross-modification-on-x86), "_Locked operations_ are not atomic with respect to _instruction fetch_ when they
operate on multiple cache-lines."  What this means effectively is that locks are not sufficient to
provide safety when modifying live code.  The authors go on to describe an extraordinary method
which does work.  It gives you a sense of what might be required to actually be able to rewrite code
in place.  In addition to this, locks are required, which for the use case I'm exploring introduces
the possibility of deadlocks which might be hard to reason about.

It might be possible to use this method, but the complexity and potential draw backs got me thinking
about simpler alternatives.

### Function Hooks

Function hooks take advantage of some compiler tricks to be able to atomically and safely hook code.
It does this by adding a 8-byte NOP instruction at the beginning of every function.  There are
compiler flags that can enable this, and it's common in Windows code.  Because the NOP is a single
instruction, there's no problem with dealing with instruction pipeline.

- See: [Why do Windows functions all begin with a pointless MOV EDI, EDI instruction?](https://devblogs.microsoft.com/oldnewthing/20110921-00/?p=9583)

[Chris Wellons](https://nullprogram.com) wrote up [an excellent description of the method and how it works.]
(https://nullprogram.com/blog/2016/03/31/) Definitely work a read.  The takeaway from this is that
if you have a little help from the compiler, it's possible safely hook your code, and provide new
  implementations.  [This looks very much like the approach taken by Swift to implement dynamic replacement.](https://www.guardsquare.com/blog/swift-native-method-swizzling)

One advantage of this approach is that you are able to provide a stable function interface that you
can export, or that might be depended on by external code.  The function pointer will never change,
that can be helpful if you are unable to track references in your application.  Function hooks work
when the function lifetime is static, meaning it's statically allocated by the loader before any
code actually runs, and you can never release it, making it impossible to have a use-after-free
error.  This is very safe, which is what we are looking for.  And it's relatively simple.

You can even modify the function signature.  The new function you hook in can expect a different set
of parameters.  The problem however that arises here is that unless you can account for every caller
of your function, and ensure that they will use the new signature, and coordinate that with the
moment you hook the function, then you can't guarantee that it won't break your system.  For this to
be safe we need a way to ensure all callers match the function signature, which can never change.
It's a limitation that's worth the stability.  You can work around this by doing things like soft
restarts, which reset execution, but that's no really what we want here.

Hooks can work great if you need to pass a stable pointer to a function with undefined lifetime.
This means passing a pointer to a function that could use it anytime between the call and the end of
the program.  That pointer is guaranteed to exist because it's static.  This method allows us to
have a static method that can also be hot-patched.

Another win for hooks is that you can dynamically patch code that knows nothing about your hot-reload
mechanism.  The only thing you need is a compiler that can apply the appropriate hook at the
beginning of the function.  This will be very important for C interop, a feature I would very much
like to enjoy.

So what about this function that we use to patch our function.  Is that static as well?  If so, we
could quickly run out of memory because you can't free static functions safely.  To do so, we would
have to ensure that nothing in the program can ever call that code again.  And this is actually
impossible to guarantee without a complete lifetime accounting of all objects in the system.  There
are all sorts of examples of different types of code that can break things unless you assume safety.
So to achieve this, we need to consider another method to complement these hooks, and that's
functions with non-static lifetimes.

### Functions with non-static lifetime

When we hook a function, how do we guarantee that the code will never be run again, allowing us to
free code that's no longer in use.  One possible solution is to use reference counting.  Each
function needs to increment a reference count on function entry, and decrement that function on
exit.  Also, any function which holds a pointer to the function also needs to increment the
reference count.  When no one holds a pointer, and the reference count is 0, we can then safely
free that memory.  This is a
lot to keep track of, and seems complex, but it turns out that [Rust is very good at doing this
exact thing.](https://rustc-dev-guide.rust-lang.org/borrow_check.html) Rust guarantees that object
lifetimes are respected using a combination of compile time and run-time guarantees.  The
compile-time guarantee is what's known as the "borrow checker".  Among other guarantees, it ensures
you will never use
something that's already been freed.  The run-time guarantees are provided using reference counting.
This does place some limits on the kinds of programs you can write, but the trade-off is safety,
exactly what we are looking for.

There are some gotchas though. For example code that never exits.  If a function never exits, it can
never be released.  This can happen if it's a forever loop, or if the code executes a longjmp.  Some care
needs to be taken in these situations.  Longjmp might not happen very often, but loops are
everywhere.

## Proposal

So my proposal is this.  Functions with non-static lifetime, guaranteed with a combination of compile-time and run-time
checks, gives us just what we need to build a cathedral of code in a single line of computation.
But to be certain, what we want is a cathedral, and not a house of cards.  So the next step is to
make sure I haven't missed something important, and get a better understanding of how this might
work in practice.

Even though Rust is really good at tracking lifetimes, when you write a Rust function, there's an
implicit assumption that the function has a static lifetime, which makes sense.  In order to do the
sort of coding I'm proposing, you would need to write the entire program using function pointers.
Rust supports this, but I'm not sure what that would look like.  We can allow `main` to be static,
but beyond that could we build something where every function (other than main), is hot patchable.
I'm pretty sure the answer is either no, or that the monstrosity you wrote would be completely
unmaintainable.  Rust doesn't actually do what we need to do here, which tells me this might be one
of those rare problems where a new programming language is required.

A programming language that:
- Guarantees memory safety at compile-time and run-time
- First-class support for functions with non-static lifetimes.

What this would look like in practice is being able to write a function once, and run it.  And
re-write the function as many times after as you like, and the language keeps track of each version
as an object in memory, rather than in a static compile time layout.  Those dynamically created
functions are freed only when safe, giving us the bounded memory we want.  And I believe this meets
all the requirements I've set out in the post. Let's review those requirements.

<a data-flickr-embed="true" href="https://www.flickr.com/photos/onasill/32292523561" title="Ottawa Ontario ~ Canada ~ Notre-Dame Cathedral Basilica ~ National Historic Site of Canada"><img src="https://live.staticflickr.com/742/32292523561_e53c18de9f.jpg" width="500" height="370" alt="Ottawa Ontario ~ Canada ~ Notre-Dame Cathedral Basilica ~ National Historic Site of Canada"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

<a data-flickr-embed="true" href="https://www.flickr.com/photos/tjflex/1347490869" title="Giant House of Cards"><img src="https://live.staticflickr.com/1380/1347490869_eec02d06e8.jpg" width="375" height="500" alt="Giant House of Cards"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## Considerations

The requirements that deserve further consideration are:

- safe C interop
- hot-reloading as a zero-cost abstraction
- fast like C++
- ability to hot-reload on embedded devices
- ability to modify any part of the code while running, including structs and function signatures
- global state

### Safe C Interop

How can we not only get full C-interop, but also full hot-reloading of any C function?  C doesn't
provide this kind of support for sure, so there's no help there.  But if we are able to provide a
lifetime aware function signature for a C function, that will allow us to treat C functions as
hot-reloadable.  If we get the signature wrong, then things go badly.  This is exactly what Rust
needs to deal with in order to work with C.  So what I'm proposing here isn't very new.

It's easy to imagine a C function that can abuse the system.  These sorts of pathological functions
should just not be used.  That's a limitation for sure, but most useful, and well written C
APIs have very clear lifetime signatures, even if they aren't explicit.

We can even change structs if we want to.  Changing a struct however changes the signature of any
function that uses it, making it incompatible with any existing state using the old structure.
This is a good and keeps things safe.  Mun solves this problem by providing clear casting rules for
struct changes.  There are options here that can be explored further.

As long as we have appropriate lifetimes on the C function signatures, and our system ensures
safety, we can hot-reload C functions and even modify structs and function signatures.  I can foresee
a situation where you make a change to a function, which makes it incompatible with what's running
at the moment.  In this case it might appear as if your function isn't being hot-reloaded.  This
would likely be confusing to a user that's expecting it to run.  But the callers are not yet aware
of the signature change.  This sort of a problem would usually be caught as a type error during
static compilation, and this situation would be no different.  The entire program doesn't compile.
That's a good thing.  Once the type issues are fixed, the code can load.    If code paths have
diverged, there may need to be a mechanism to reset program flow further up the stack, a straight
forward operation typically done by debuggers.  More importantly, for a good user experience, there
may need to be some indication to the user at which stack level the code diverged, so the user can
properly reset execution.  These sorts of debugger operations become essential in this dynamic
environment.

### Zero-cost abstraction

Zero-cost abstraction means that if don't want to use this hot-reloading stuff, the language does not
suffer the performance cost.  There's likely going to be some performance hit to support this.  It
should be easy to compile a version of the code the interprets the functions as having static
lifetimes.  This will likely open up a lot of optimizations that were impossible in the non-static
scenario.  I definitely want that, especially for the case where you want to ship your code, and you
don't want your users, or hackers messing with things.  Solving the non-static problem is the hard
part, if we can solve that, static functions should be easy.

### Fast like C++

Once the functions are downgraded to static lifetimes and everything is compiled, there's no reason
why it wouldn't be as fast as C++.  All of the code related to hot-reloading is removed, and all your
left with is your code.  I think of this like a Python wrapper that runs C code.  If you compiled
out the Python part, all you would be left with is C.

### Embedded device support

Embedded devices present an interesting opportunity.  I've worked as a firmware developer, and I can
definitely say it's even worse than doing C++ application development.  No only are you using some
out of date fork of gcc to compile your code, but you also need to flash the hardware, which can
take almost as long as the compilation step.  There's definitely an opportunity here to really speed
things up.  These devices are memory constrained, so memory can be tight.  I can imagine this
working by having a smart bootloader that implements the memory safety guarantees, which listens for
compiled code updates from the host.  And patches it's memory space.  It wouldn't require a full
toolchain, that work can be done on the host.  It just needs a smart boot loader.  Some of that
intelligence might be able to live on the host even, in which case the boot loader just accepts
commands to write code into memory, and some other debug commands, and you have yourself a
hot-reloadable embedded device.  No more flash rewrites.  Developers will be very very happy.

### Modify any part

Will this give us the ability to modify any part of the code?  I think it does. It even allows us to
rewrite main.  In order to actually run the new version of main though, you will need to pop the
stack right back to the beginning.  To do this safely, we would need to unwind the stack cleanly,
similar to how exceptions work.  We can't just reset the stack pointer to the start unfortunately,
there's likely a lot of state in the stack tracking things like lifetimes and reference counting
that need to be run in order to clean things up properly.  So exceptions would be necessary in the
language in order to support this.  Rust interestingly doesn't support exceptions.   Exceptions
doesn't have to be something that's supported if hot-reloading is disabled, it just needs to be
supported to do this sort of stack restarting, which is effectively an exception that gets thrown
and then caught up the stack somewhere.  The functions may require special compilation in order to
support this.

But with that support in place, we should be able to modify everything, even main!

### Global State

What about global state?  One of the big problems with complex software is you have all of this
state all over the place, and the complexity is such that the total number of states your program
can be in is more than the total number of atoms in the universe.  It doesn't take a very large
program to get there.  Clearly it's impossible to handle every possible state a program can be in,
so we take care to keep that state to a minimum and try to prevent illegal states before they ever
happen.  Programming in this new way opens up new opportunities for crazy states, and I think extra
care is warranted to manage it properly.  The compiler should block programs from being loaded that
do clearly illegal things, but that doesn't cover all of the legal things a programmer can do.

Usually with a program, it runs only once.  But if you're hot-reloading, you can make a change,
and put state into something strange, and then correct your mistake.  Even though you've fixed the
function, the state may still be broken.  This may lead to all sorts of hard to detect bugs,
because the code that created the state is no longer visible to the programmer.  Good debugging
tools can go a long way.  But most importantly, the user needs to be able to reset their state to
something expected.  We can try to use data structures to make impossible states unrepresentable, but
that's unlikely to always be the case.  One of the challenges of this sort of programming, is
learning how to build and construct software that makes resetting state easy.  It's not something we
normally think about.  But if you're building a cathedral from the inside out, it makes sense that
there is some methods of construction that work better than others.  That would be the art of this
sort of programming.  The complexity could easily get out of hand very quickly.  And that might be a
good thing, because it forces the developer to constantly think about state and it's lifetimes.

Very likely, a good garbage collector will be a lifesaver here.  Though I don't think it's
essential.

## Next Steps

So what's next?  Now that I have a pretty good idea of the problem, I'm going to look into a small
proof of concept.  I have already created a rudimentary in-memory linker in Rust with support for creating
and freeing functions.  It uses persistent data structures to keep track of the functions, and
because it's written in Rust, I'm pretty confident that it's safe.  Most of the challenges I had
were in understanding how linkers work, so I could do the same thing, just at run-time and in
memory.

To better understand things, I ended up writing a very simple x86-64 ELF linker in Rust which can
link C object files and dynamic libraries.  It's passing the tests at the moment, and it was quite
an achievement.  It took over my evenings for a few months.  So with this understanding, I think I'm
ready to create another proof-of-concept.

I'd like to include the following:
- Ensure executable memory is properly protected, being marked as RX only.  We can do this by mapping the same memory twice into the process.  Once as RW, and the second time as RX.  This will provide further safety guarantees to ensure that running code doesn't accidentally overwrite itself.
- Get linking working properly in memory.  One thing I learned with my POC is that if you want to do
  hot-linking, it's actually a lot easier than building a static linker.  You don't need to worry as
  much about the ABI.  You still need to worry about it, but you can simplify a few things.  My
  first attempt I made some mistakes, which should hopefully be corrected based on my experience
  with the static linker.
- Work on improving the C-interop, so that C functions can be properly specified to be lifetime
  aware.  This will allow me to treat C functions as reloadable.  To do this, the runtime will need
  to keep track of the function signatures.  If this signature is incorrect, it will likely crash
  everything, but as long as the function signature matches the implementation (which C does not
  guarantee), everything should work.  I mostly want C for interop, not as a language to program in.
  It's not the best fit.  But it's simple and easy to understand for a proof of concept, and it will
  allow me to test my theory without having to invent a new language.

That's what I've got so far.  I can't wait to be hot-reloading like it's 1972!

## Similar Projects

- [Mun](https://docs.mun-lang.org/ch04-04-hot-reloading.html)
- [Nim](https://slides.com/onqtam/nim_hot_code_reloading#/33/0/1)
- [C++ options](https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/wiki/Alternatives)
- [Hot-reloading in Rust](https://github.com/rksm/hot-lib-reloader-rs)
- [Hot-reloading in Python using Reloadium](https://github.com/reloadware/reloadium)
- [Swift Swizzling](https://www.guardsquare.com/blog/swift-native-method-swizzling)

## References

   - [Living on the edge: Rapid-toggling probes with cross modification on x86](https://pldi16.sigplan.org/details/pldi-2016-papers/28/Living-on-the-edge-Rapid-toggling-probes-with-cross-modification-on-x86): A great paper that describes the difficulties that self-modifying code presents for modern CPU architectures.
