So what is DevOps?

To understand what it is, you first need to understand why DevOps exists.

Traditionally, IT teams consist of developers and operators.

Developers are responsible for writing code for systems and operators are responsible for ensuring that those systems operate reliably, so customers are happy.

Developers are expected to be agile and are often pushed to write and deploy new code as quickly as possible.

Essentially, developers want to work faster, innovating, and succeeding or failing quickly.

This resulted in developers throwing their code over the wall to operators who then had to

deal with code that was written without much understanding of how it would run in production.

Operators who are expected to keep systems stable would prefer to work slower, focusing on reliability and consistency.

Quite understandably, this way of working wasn't sustainable between these two groups.

Their priorities caused tension between the two teams, and they were not necessarily aligned with the needs of the business.

As a way to knock down the wall and close the gap between developers and operators, a culture instead of practices known as DevOps was born.
01:19
Let's take a look at how Google categorizes DevOps.

There are five key areas.

The first is to reduce organizational silos.

You can increase and foster collaboration by breaking down barriers across teams.

Second, you need to accept failure is normal.

Computers are inherently unreliable, so you can't expect perfect execution, and when you introduce humans into the system, you get even more imperfection.

Things failing will inevitably become part of the process.

Third, you'll want to implement gradual change.

Small incremental changes are easier to review, and if a gradual change does release a bug

in production, it allows you to reduce the time to recover making it simple to roll back.

Fourth, you need to leverage tooling and automation.

Identifying manual work that you can then automate is key to helping your IT team work efficiently and focus on the tasks that matter.

Finally, you'll want to measure everything.

Measurement is a critical gauge for success.

There's no way to tell whether what you're doing is successful if you have no way to measure it.

It's important to understand that DevOps is a philosophy versus a development methodology or technology.

Although DevOps philosophy highlights critical ways for IT teams to operate, it doesn't give explicit guidance on how an organization should implement practices to be successful.

That's where SRE comes in.

So what is SRE?

SRE evolved at Google in early 2000's separately from DevOps.

Back in 2003, Benjamin Treynor Sloss, currently a VP of engineering at Google, was tasked

with managing a team of engineers who are responsible for keeping Google's websites up and running.

You're probably wondering, "Wait, so a bunch of software engineers who write the code now also

have to be responsible for running their production systems? But doesn't the Ops team do that?"

Well the answer at least traditionally is yes.

However, this team only had software engineers, so Ben had them spend some of their time on operations tasks in addition to development tasks.

So they could better understand how their code ran and production.

This way of working is what led the team to site reliability engineering and the associated job role were SREs, who are generally engineers, are responsible for operations.

Just as DevOps aims to close the gap between software development and software operations, this new SRE approach is a concrete way to solve problems that the DevOps philosophy addresses.

Note that SRE is both a practice and a role.

Not every organization that follows SRE principles necessarily must have engineers with the title SRE.

This course mostly focuses on the practices and principles themselves, things like titles and team structures are implementation details.

Several SRE practices align to Google's categorizations of DevOps, and in addition to implementing SRE technical practices, you'll also want to implement cultural practices.

Without a culture to sustain them, it is not possible to maintain the practical aspects of SRE.

Let me explain where these fundamentals fit into the key areas of DevOps we discussed.

With regard to reducing organizational silos, SREs share ownership of production with developers.

Together they define service level objectives or SLOs and error budgets, and share responsibility of how they determine reliability and prioritize work.

Culturally, this promotes shared vision and knowledge as a well as a need for improved collaboration and communications.

Complex systems fail in interesting and complex ways.

Accepting failure as normal state is an important practice within SRE.

A blameless postmortem is held after an incident to improve the understanding of the failure mode

and to identify effective preventive actions to reduce the likelihood or impact of a similar incident.

Learning from incidents in this matter requires a culture of psychological safety and blamelessness.

When implementing gradual change, SREs aim to reduce the cost of failure by rolling out changes to a small percentage of users before making them generally available.

Culturally, this promotes more of design thinking and prototyping.

Next, in order to leverage tooling and automation.

SREs focus on toil automation reducing the amount of manual repetitive work.

Automating this year's job away can undoubtedly be met by resistance, that's why teams need to talk

about and understand the psychology of change and how to address resistance to change within the team.

Finally, measuring everything means that SREs work to measure everything related to toil, reliability, and the health of their systems.

To foster these practices, organizations need a culture of goal setting, transparency, and data-driven decision-making.

Before diving into each of these pillars as they relate to SRE, I want to acknowledge

that sometimes people can see these practices aligning with different or many of the pillars of DevOps.

It is likewise important to acknowledge that the language and definitions across different organizations, are less critical than

driving towards the goal of your organization, and the outcomes you are trying to deliver for your customers.

In other words, we may disagree on the precise terminology, but many of the underlying principles are the same.

The goal of SRE is to serve the business and the user, not the other way round.

The next three modules will dig a bit deeper into all of these SRE practices and cultural concepts.
