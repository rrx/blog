---
title: "Microservices and Monoliths: More than you think"
date: 2024-04-28T09:31:12-08:00
draft: false
---

When evaluating a complex software system, we must consider the architectural choice between microservices and monoliths. Many articles have been written on the difference between these two, but they mostly focus on the obvious. I'd like to dig a little deeper in this article. If you’re not quite clear on the distinction, [here is a great article.](https://aws.amazon.com/compare/the-difference-between-monolithic-and-microservices-architecture/)

<!--more-->

<figure>
    <img src="microservices.jpg" alt="battleship and container ship (sd)" loading="lazy">
    <figcaption>battleship and container ship (sd)</figcaption>
</figure>

When we talk about the choice between microservices and monoliths, it’s commonly presented as an either/or decision. However, most organizations have some combination of both monolith and microservices.  For example, a legacy monolith, with more recent work happening in microservices. Most articles tend to disparage monoliths and evangelize microservices. This bias isn’t helpful to a decision maker faced with a messy history of prior work spanning years or decades.

Consider the following situations.  How would you make these decisions?

- The microservice is no longer so micro, and it’s starting to encounter some issues. Is it time to break it up into smaller services? 
- You want to add a new feature, do you add it to one of the existing services, or do you create a new service?
- A microservice seems to be the source of a number of bugs or outages . Are there some architectural choices we can consider to improving the situation?
- A monolith is working fine, but your manager insists that microservices are the future.  How do you convince them it is not?

Let’s dig into some reasons why you might want to consider one or the other, or even both!  Even if you work in an organization that’s all in on microservices, these principles still apply. Not only does a growing and evolving code base, force you to make these decisions, but the constant change in the industry can also force you reevaluate.

The automatic reflex to build a new service every time you can’t find a place for something will multiply your problems. Alternatively, how can you make the case to your manager that you need to split your service?

Let’s dive into some principles that have helped me make these decisions.
## When to consider a monolith

Monoliths aren’t all bad. In fact there are some compelling advantages. Most of the added complexity can be handled through modularization (the modular monolith) and enforced with tooling or language features.

Just to open up the possibilities here. A monolith might actually look like a microservice, but that microservice, spans multiple domains, or it handles a variety of requests. While it might be nice to split these out, keeping them together isn’t always a bad idea.

Here are some reasons to consider a monolith:

- **Longer Release Cycles**: If your team works with extended release cycles, say every two weeks or more, and there’s no imminent shift towards continuous delivery, a monolith might serve you better. Consider the QA process: testing a single, cohesive artifact or appliance can be far simpler and more straightforward than wrestling with multiple microservices. The integrated nature of a monolith ensures that all components interact within the same environment, significantly simplifying integration testing.

- **Standardized Tech Stack**: Monoliths shine in environments with a uniform tech stack. Leveraging the full feature set of a single programming language to manage different components of your application can offer a robust composition layer, avoiding the overhead of remote procedure calls typical in microservices architectures. Moreover, if your development team isn't huge or highly skilled, having a single stack reduces the learning curve and fosters better understanding and collaboration among team members. Languages that support strong module or library systems can effectively encapsulate and segregate functionality within a monolith, maintaining clarity and modularity without the operational complexity of microservices.

- **Performance Critical Software**: For applications where performance is paramount, such as those handling low-latency requests (think of financial transactions) , the potential performance gains of a monolith can be a game-changer. When all parts of an application run on a single system, the network overhead of microservices can almost be eliminated, potentially unlocking significant gains in processing speed and resource management.

- **Simplicity in Development**:  Often a company starts with a monolithic architecture and only migrates to microservices when the complexity of their operations necessitates it. For startups focused on getting a viable product to market swiftly, the monolith offers fewer moving parts and a lower barrier to initial development. Debugging is more straightforward when you don’t need to trace issues across network boundaries, and the overall system architecture is easier to grasp for new developers.

- **Rapid Development**
In the fast-paced startup world, speed can make it or break it. A monolithic architecture allows for rapid development, and simplifies the design space. When it comes to speed, sometimes less is more. The ability to develop quickly and deploy immediately without the considerations of managing multiple services can be an advantage.

- **When High Availability Is Not a Requirement**: Not every application needs to be available 24/7. For desktop software or applications in use solely during business hours, the high availability that microservices offer might not justify the added complexity. In such cases, if a monolithic architecture can meet you availability needs effectively, there’s no need for the added complexity of multiple services.

## When to consider microservices

Considering microservices goes beyond a decision at the start of a new project.  It's something to consider as your services grow and evolve.  The are often considered when a service has become too difficult to extend or maintain.  Using microservices isn't the only answer, here are some reasons you might want to consider splitting up your monolith into microservices.


- **Managing Stack or Language Incompatibilities**: Microservices are great for integrating across diverse technologies. If your stack is getting a bit wild, a little python here, some Golang there, all wrapped up with multiple targets in a Dockerfile and duck taped with bash scripts, then you might want to consider splitting it up, and setting up each project independently. This can help developers avoid the temptation to continue feeding your Frankenstein monster. Splitting it up will allow you to define clear API boundaries, and let your teams focus on their strengths.

- **Isolating Critical Components**: Separating services according to their criticality ensures that less critical components can fail without cascading effects on entire system. This architectural choice helps in resource allocation, preventing non-essential services from starving out critical ones.

- **Lifecycle Differences**: How frequently your services chances can be a factor to consider. Microservices are ideal for isolating parts of a system that change at different rates. Services that require frequent updates or have a large number of upstream dependencies can be isolated to reduce the risk of introducing errors into stable parts of the system that change infrequently.

- **Stable and Compatible APIs**: Microservices can be used to define and enforce API compatibility using common RPC Frameworks. You can use this trick with monoliths as well, but it's more commonly seen in microservices. Tools like gRPC, Thrift, and GraphQL not only facilitate building and consuming APIs but through some additional tooling, also ensure compatibility across different versions. They help manage the contract between services, preventing breaking changes and maintaining consistency.

- **API Usage Patterns**: Microservices enable tailored scaling and optimization strategies based on specific usage patterns such as high throughput or low latency requirements. This makes them particularly advantageous in systems where performance criteria vary significantly between components.

- **Data and Compliance Requirements**: In scenarios with stringent data handling or compliance regulations like GDPR or FedRAMP, microservices can allow for clear segregation of data, aligning architecture with compliance needs. 

- **Reduce Complexity**: While microservices are often associated with increased complexity, they can also be used to manage complexity. Decomposing your system into self-contained services can actually help encapsulate difficult parts of the system. This can reduce cognitive load when reasoning about the system as a whole.

- **Deploy Contention**: In highly active development environments where deployment pipelines become congested, microservices offer a way out by allowing individual teams to deploy their services independently. In my experience, this is often the final straw that forces a decision to split a service up.

- **Blast Radius**: The concept of 'blast radius' refers to the extent of impact a failure can have on the wider system. Microservices limit this by isolating failures to individual services. This isn't always the case of course. Microservices are also well known for causing cascading failures. A well architected system can avoid these problems.

- **Cleanly Separated Domains**: Microservices encourage the separation of business capabilities into distinct domains, each with its own database and service environment. This is closely related the [Domain Driven Design (DDD)](https://en.wikipedia.org/wiki/Domain-driven_design), which benefits from microservices by aligning service boundaries with domain boundaries.

## Conclusion

I hope this article gave you a some things to think about when considering how services compose together. These are just the considerations I have thought about, and I'm sure there's more. It's worth considering both options. What will work for you depends entirely on your situation. The fun part of software is having the power and flexibility to build things just right. 

Here are some thoughts to end with:

- Not every situation requires Google level architecture, if you find yourself working on a monolith, remember, consider the advantages to doing so.   
- If you think your microservice has gotten too big, it might be just fine, and you can leave it as is.
- If everyone complains about how long it takes to get code deployed, splitting up the code could help, or bankrupt your company.

No easy answers, just lots to think about. Thanks for reading.

