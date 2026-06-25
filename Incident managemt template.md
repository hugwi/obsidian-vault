---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---

https://www.atlassian.com/incident-management/postmortem/templates#timeline

## Fault

Describe how the change that was implemented didn't work as expected. If available, attach screenshots of relevant data visualizations that illustrate the fault.

#### EXAMPLE:

{NUMBER} responses were sent in error to {XX%} of requests. This went on for {TIME PERIOD}.

## Detection

When did the team detect the incident? How did they know it was happening? How could we improve time-to-detection? Consider: How would we have cut that time by half?

#### EXAMPLE:

This incident was detected when the {ALERT TYPE} was triggered and {TEAM/PERSON} were paged. 

Next, {SECONDARY PERSON} was paged, because {FIRST PERSON} didn't own the service writing to the disk, delaying the response by {XX MINUTES/HOURS}.

{DESCRIBE THE IMPROVEMENT} will be set up by {TEAM OWNER OF THE IMPROVEMENT} so that {EXPECTED IMPROVEMENT}.

## Root cause identification: The Five Whys

The Five Whys is a [root cause identification technique](https://www.atlassian.com/team-playbook/plays/5-whys). Here’s how you can use it:

- Begin with a description of the impact and ask why it occurred. 
- Note the impact that it had.  
- Ask why this happened, and why it had the resulting impact. 
- Then, continue asking “why” until you arrive at a root cause.

List the "whys" in your postmortem documentation.

#### EXAMPLE:

1. The application had an outage because the database was locked
2. The database locked because there were too many writes to the database
3. Because we pushed a change to the service and didn’t expect the elevated writes
4. Because we don't have a development process established for load testing changes
5. Because we never felt load testing was necessary until we reached this level of scale.

## Root cause

Note the final root cause of the incident, the thing identified that needs to change in order to prevent this class of incident from happening again.

#### EXAMPLE:

A bug in connection pool handling led to leaked connections under failure conditions, combined with lack of visibility into connection state.

## Lessons learned

Discuss what went well in the incident response, what could have been improved, and where there are opportunities for improvement.

#### EXAMPLE:

- Need a unit test to verify the rate-limiter for work has been properly maintained
- Bulk operation workloads which are atypical of normal operation should be reviewed
- Bulk ops should start slowly and monitored, increasing when service metrics appear nominal

## Corrective actions

Describe the corrective action ordered to prevent this class of incident in the future. Note who is responsible and when they have to complete the work and where that work is being tracked.

#### EXAMPLE:

1. Manual auto-scaling rate limit put in place temporarily to limit failures
2. Unit test and re-introduction of job rate limiting
3. Introduction of a secondary mechanism to collect distributed rate information across cluster to guide scaling effects
