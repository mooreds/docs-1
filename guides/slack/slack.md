---
id: slack
title: Building Slack bots, slash commands, and workflows
layout: docs.mustache
tags: doc
description: "The best Slack apps are the ones perfectly adapted to your needs. Build Slack bots, slash commands, and workflows. Let Transposit handle auth and execution while you focus on the fun."
---

<img src="/docs/assets/slack-logo.svg" class="fr pl2 pb2" width="100">

Slack is a growing hub for collaboration. Beyond just team messaging, Slack lets you build powerful extensions that turn it into an interface to all of the tools and applications that your team uses. Through bots, slash commands, automated workflows, and notifications, make yourself and your team Slack power users.

The best Slack apps are the ones perfectly adapted to your needs. The Slack App Directory has over 15k listings, but Slack workspaces use over 450k custom integrations every week. One size doesn't fit all. When you want to build a Slack extension that's tailored to your specific needs, Transposit handles the overhead so you get to focus on the fun. Imagine connecting Slack to AWS, Jira, or CircleCI without worrying about auth!

<div class="center">
  <div class="cf">
    <div class="fl w-100 w-50-ns pa2">
      <div><strong>Slash commands - </strong>
        <a href="slash-commands">read more</a>
        <br><img src="/docs/assets/slack-slashcommand.png"></div>
    </div>
    <div class="fl w-100 w-50-ns pa2">
      <div><strong>Bots - </strong>
        <a href="chatbots">read more</a>
        <br><img src="/docs/assets/slack-bot.png"></div>
    </div>
  </div>
</div>

<div class="center">
  <div class="cf">
    <div class="fl w-100 w-50-ns pa2">
      <div><strong>Workflows - </strong>
        <a href="workflows">read more</a>
        <br><img src="/docs/assets/slack-workflow.png"></div>
    </div>
    <div class="fl w-100 w-50-ns pa2">
      <div><strong>Notifications - </strong>
        <a href="notifications">read more</a>
        <br><img src="/docs/assets/slack-notification.png"></div>
    </div>
  </div>
</div>

## Key Features

<div class="landing-title">Managed authentication 🔐</div>
<div class="landing-copy">Your Slack integrations need to work with cloud services on behalf of your users. Transposit manages users, their credentials, refreshing tokens, and storing them securely.</div>

<div class="landing-title">User customization 🎨</div>
<div class="landing-copy">When you’re building a custom Slack integration you want it to be, well, custom! Transposit gives a simple mechanism to let users customize: specify a Jira query, pick a Google calendar, add a phone number for SMS alerts</div>

<div class="landing-title">Broad API support 📱</div>
<div class="landing-copy">Connect and authenticate in seconds to the services you use. Experiment interactively rather than scouring documentation. Check out the growing list of connectors <a href="/docs/references/data-connectors/">here</a></div>

<div class="landing-title">Up-level your work 🤔</div>
<div class="landing-copy">Transposit’s relational engine puts SQL in front of any API. And lets you mix in JavaScript when you need. Write less code in a language designed to manipulate, transform, and compose data.</div>

<div class="landing-title">Severless 🚀</div>
<div class="landing-copy">Build your logic and let Transposit host it for you. Build and deploy a bot for your entire team in minutes. Really.</div>

<div class="landing-title">Fork and customize examples 🌳</div>
<div class="landing-copy">Try some of our sample apps or some apps built by other developers. Close but not what you need? Fork it, and customize it. You don’t need to start from scratch.</div>

## Sample applications

Here's a few starting points. Try them out, view the code, fork a copy, customize to suit your needs.

  <div class="flex flex-wrap justify-center mv3">
    <div class="app-card app-card-small ma2 pa3 br2">
      <img src="/img/app-icons/icon-app-circleci-router.svg" alt="App icon" class="app-graphic">
      <h2 class="f6 f5-ns">CircleCI Router</h2>
      <p class="f6 lh-copy mt0">
        Get an @ mention if you break the build! Replaces the GitHub username in the build status message sent by CircleCI with the user's Slack ID.
      </p>
      <p class="ma0">
        <a class="btn f6 br2 ba ph2 pv1 mb2 dib mr1" href="https://console.transposit.com/t/transposit-sample/circleci_router?readme=true">View code</a>
      </p>
    </div>
    <div class="app-card app-card-small ma2 pa3 br2">
      <img src="/img/app-icons/icon-app-github-transfer.svg" alt="App icon" class="app-graphic">
      <h2 class="f6 f5-ns">GitHub Transfer</h2>
      <p class="f6 lh-copy mt0">
       Transfer files between repos using a Slack slash command.
      </p>
      <p class="ma0">
        <a class="btn f6 br2 ba ph2 pv1 mb2 dib mr1" href="https://console.transposit.com/t/transposit-sample/github_transfer/code?readme=true">View code</a>
      </p>
    </div>
    <div class="app-card app-card-small ma2 pa3 br2">
      <img src="/img/app-icons/icon-app-calendar.svg" alt="App icon" class="app-graphic">
      <h2 class="f6 f5-ns">Slack vacation helper</h2>
      <p class="f6 lh-copy mt0">
        Automatically set your Slack status while your Google Calendar says you're away on vacation.
      </p>
      <p class="ma0">
        <a class="btn f6 br2 ba ph2 pv1 mb2 dib mr1" href="https://console.transposit.com/t/transposit-sample/cal_slack_status?readme=true">View code</a>
        <a class="btn f6 br2 ba ph2 pv1 mb2 dib" href="https://cal-slack-status-p7i9u.transposit.io/" target="_blank">Try it ↗</a>
      </p>
    </div>
  </div>

## Next steps

- [Slash commands](slash-commands): Build custom commands that integrate with your other apps.
- [Chatbots](chatbots): Build bots that chime in with useful info or can hold up their end of a conversation.
- [Workflows](workflows): Build workflows, elevating important decisions and automating the rest.
- [Notifications](notifications): Consolidate notifications in Slack; provide contextual ino and actions.
