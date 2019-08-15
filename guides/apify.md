---
id: apify
title: Building Apify integrations in Transposit
layout: docs.mustache
tags: doc
description: "Apify provides a way to turn any website into a custom API. Connect actors, tasks, and datasets from Apify to multiple different connectors easily with Transposit."
---

<img src="/docs/assets/apify-logo.svg" class="fr pl2 pb2" width="100">

Apify is the place to find, develop, buy and run cloud programs called actors. These actors allow you to automate any workflow on the web no matter the API support to be used in your applications. Their actors, tasks, and datasets allow you and your team to have the data of the web at your fingertips.

The best Slack apps are the ones perfectly adapted to your needs. The Slack App Directory has over 15k listings, but Slack workspaces use over 450k custom integrations every week. One size doesn't fit all. When you want to build a Slack extension that's tailored to your specific needs, Transposit handles the overhead so you get to focus on the fun. Imagine connecting Slack to AWS, Jira, or CircleCI without worrying about auth!

<div class="center">
  <div class="cf">
    <div class="fl w-100 w-50-ns pa2">
      <div><strong>Web scraping</strong><br><img src="/docs/assets/slack-slashcommand.png"></div>
    </div>
    <div class="fl w-100 w-50-ns pa2">
      <div><strong>Web automation</strong><br><img src="/docs/assets/slack-bot.png"></div>
    </div>
  </div>
</div>

<div class="center">
  <div class="cf">
    <div class="fl w-100 w-50-ns pa2">
      <div><strong>Custom inputs</strong><br><img src="/docs/assets/slack-workflow.png"></div>
    </div>
    <div class="fl w-100 w-50-ns pa2">
      <div><strong>Notifications</strong><br><img src="/docs/assets/slack-notification.png"></div>
    </div>
  </div>
</div>

## Key Features

<div class="landing-title">Managed authentication 🔐</div>
<div class="landing-copy">Your Apify integrations need to work with cloud services on behalf of your users. Transposit manages users, their credentials, refreshing tokens, and storing them securely.</div>

<div class="landing-title">User customization 🎨</div>
<div class="landing-copy">When you’re building a custom Apify integration you want it to be, well, custom! Transposit gives a simple mechanism to let users customize: specify a Jira query, pick a Google calendar, add a phone number for SMS alerts</div>

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
      <img src="/img/app-icons/icon-app-pridebot.svg" alt="App icon" class="app-graphic">
      <h2 class="f6 f5-ns">Pridebot</h2>
      <p class="f6 lh-copy mt0">
        A bot that matches you with the soonest Pride event in your city, using Twilio and Apify.
      </p>
      <p class="ma0">
        <a class="btn f6 br2 ba ph2 pv1 mb2 dib mr1" href="https://console.transposit.com/t/transposit-sample/pridebot?readme=true">View code</a>
      </p>
    </div>
    <div class="app-card app-card-small ma2 pa3 br2">
      <img src="/img/app-icons/icon-app-github-transfer.svg" alt="App icon" class="app-graphic">
      <h2 class="f6 f5-ns">Amazon Review Scraper</h2>
      <p class="f6 lh-copy mt0">
       Copy over all Amazon reviews of a product to a new Google Sheet.
      </p>
      <p class="ma0">
        <a class="btn f6 br2 ba ph2 pv1 mb2 dib mr1" href="https://console.transposit.com/t/transposit-sample/amazon_review_scraper?readme=true">View code</a>
        <a class="btn f6 br2 ba ph2 pv1 mb2 dib" href="https://amazon-review-scraper-6vuu1.transposit.io" target="_blank">Try it ↗</a>
      </p>
    </div>
    <div class="app-card app-card-small ma2 pa3 br2">
      <img src="/img/app-icons/icon-app-calendar.svg" alt="App icon" class="app-graphic">
      <h2 class="f6 f5-ns">Apify Demo</h2>
      <p class="f6 lh-copy mt0">
        Sample API calls to start using Apify in Transposit.
      </p>
      <p class="ma0">
        <a class="btn f6 br2 ba ph2 pv1 mb2 dib mr1" href="https://console.transposit.com/t/transposit-sample/apify_demo?readme=true">View code</a>
      </p>
    </div>
  </div>
