document.addEventListener('DOMContentLoaded', function () {
  if (window.dataLayer) {
    dataLayer.push({
      event: 'open_detail_view',
      item_id: '{{ item.pk }}',
      item_title: '{{ item.title|escapejs }}',
      content_type: '{{ item.content_type|escapejs }}'
    });
  }

  var contactBtn = document.getElementById('contactFromDetail');
  if (contactBtn) {
    contactBtn.addEventListener('click', function () {
      if (window.dataLayer) {
        dataLayer.push({
          event: 'contact_from_open_detail',
          item_id: '{{ item.pk }}',
          item_title: '{{ item.title|escapejs }}'
        });
      }
    });
  }
});
