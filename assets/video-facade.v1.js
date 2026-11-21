/* Load each existing video player only after an explicit play request. */
(function () {
  'use strict';
  document.querySelectorAll('[data-video-id]').forEach(function (button) {
    button.addEventListener('click', function () {
      var id = button.dataset.videoId;
      if (!/^[A-Za-z0-9_-]{11}$/.test(id)) return;
      var frame = document.createElement('iframe');
      frame.src = 'https://www.youtube.com/embed/' + id + '?playsinline=1&rel=0&autoplay=1';
      frame.title = button.dataset.videoTitle;
      frame.width = '820';
      frame.height = '461';
      frame.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      frame.referrerPolicy = 'strict-origin-when-cross-origin';
      frame.allowFullscreen = true;
      button.replaceWith(frame);
      frame.focus();
    }, { once: true });
  });
})();
