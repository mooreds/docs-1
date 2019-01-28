window.addEventListener('load', function () {
  const URL = "https://console.monkey.transposit.com/api/v1/public/activity"

  function sendEventsUsingBeacon(event) {
    console.log("~~~~ sendEventsUsingBeacon");
    
    if (navigator.sendBeacon) {
      const addedToQueue = navigator.sendBeacon(URL, JSON.stringify(event));

      if (!addedToQueue) {
        // if the beacon API is available in the browser, but the browser wasn't able to
        // add the request to the queue we revert to POST request.
        sendEventsUsingPost(url, data);
      }
    }
  }

  function sendEventsUsingPost(event) {
    console.log("**** sendEventsUsingPost");

    fetch(URL, {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "text/plain; charset=utf-8",
      },
      body: JSON.stringify(event),
    });
  }

  function sendPageView(path) {
    const event = {
      type: "page-view",
      path
    };

    sendEventsUsingBeacon(event);
  }

  function sendEvent(category, action, label) {
    const event = {
      type: "event",
      category,
      action,
      label,
    };

    sendEventsUsingBeacon(event);
  }

  function handlePageLoad() {
    sendPageView(window.location.href);
  }

  function handleLinkClick(event) {
    sendEvent("link", "click", event.target.href);
  }

  document.querySelectorAll('a').forEach(function (linkElement) {
    linkElement.addEventListener('click', handleLinkClick);
  });

  handlePageLoad();
});