const activity = (function () {
  const URL = "https://console.transposit.com/api/v1/public/activity";

  function sendEvent(category, action, label) {
    const event = {
      trackerSource: "DOCS",
      type: "event",
      category,
      action,
      label,
    };

    sendEventsUsingBeacon(event);
  }

  function sendPageView(path) {
    const event = {
      trackerSource: "DOCS",
      type: "page-view",
      path
    };

    sendEventsUsingBeacon(event);
  }

  function sendEventsUsingBeacon(event) {
    if (navigator.sendBeacon) {
      const addedToQueue = navigator.sendBeacon(URL, JSON.stringify(event));

      if (!addedToQueue) {
        // if the beacon API is available in the browser, but the browser wasn't able to
        // add the request to the queue we revert to POST request.
        sendEventsUsingPost(event);
      }
    } else {
      sendEventsUsingPost(event);
    }
  }

  function sendEventsUsingPost(event) {
    fetch(URL, {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "text/plain; charset=utf-8",
      },
      body: JSON.stringify(event),
    });
  }

  return {
    sendEvent,
    sendPageView
  };
})();

window.addEventListener('load', function () {
  function handleLinkClick(event) {
    activity.sendEvent("link", "click", event.target.href);
  }

  document.querySelectorAll('a').forEach(function (linkElement) {
    linkElement.addEventListener('click', handleLinkClick);
  });

  activity.sendPageView(window.location.href);
});