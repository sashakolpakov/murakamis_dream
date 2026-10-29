(() => {
  const base = document.body.dataset.base || './';
  let indexPromise;
  const index = () => indexPromise ||= fetch(base + 'assets/search.json').then(r => {
    if (!r.ok) throw new Error('Search index could not be loaded.');
    return r.json();
  }).then(rows => rows.map(row => ({...row, haystack: (row.title + ' ' + row.topic + ' ' + row.text).toLowerCase()})));
  const tokens = query => query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  const match = (rows, query, type = '', topic = '') => {
    const ts = tokens(query);
    return rows.filter(row => (!type || row.type === type) && (!topic || row.topic === topic) && ts.every(t => row.haystack.includes(t)))
      .sort((a, b) => {
        const rank = row => ts.reduce((n, t) => n + (row.title.toLowerCase().includes(t) ? 10 : 0), 0) + (row.type === 'Guide' ? 5 : 0);
        return rank(b) - rank(a) || a.title.localeCompare(b.title);
      });
  };
  function render(container, rows, query, limit) {
    container.replaceChildren();
    const ts = tokens(query);
    rows.slice(0, limit).forEach(row => {
      const article = document.createElement('article'); article.className = 'search-result';
      const h = document.createElement('h3'); const a = document.createElement('a');
      a.href = row.url.startsWith('https:') ? row.url : base + row.url; a.textContent = row.title; h.append(a);
      const meta = document.createElement('div'); meta.className = 'result-meta';
      meta.textContent = `${row.type} · ${row.topic} · ${row.status}`;
      const p = document.createElement('p');
      const position = ts.length ? Math.max(0, row.text.toLowerCase().indexOf(ts[0]) - 70) : 0;
      p.textContent = (position ? '…' : '') + row.text.slice(position, position + 240).trim() + (row.text.length > position + 240 ? '…' : '');
      article.append(h, meta, p); container.append(article);
    });
  }
  const dialog = document.getElementById('search-dialog');
  const searchInput = document.getElementById('search-input');
  const resultBox = document.getElementById('search-results');
  const searchStatus = document.getElementById('search-status');
  let timer, searchGeneration = 0;
  document.querySelectorAll('[data-search-open]').forEach(b => b.addEventListener('click', () => {dialog.showModal(); searchInput.focus();}));
  document.getElementById('search-close').addEventListener('click', () => dialog.close());
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && dialog.open) {event.preventDefault(); dialog.close(); return;}
    if (event.key === '/' && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) {event.preventDefault(); dialog.showModal(); searchInput.focus();}
  });
  searchInput.addEventListener('input', () => {
    clearTimeout(timer); const generation = ++searchGeneration;
    timer = setTimeout(async () => {
      if (!searchInput.value.trim()) {resultBox.replaceChildren(); searchStatus.textContent = 'Search guide chapters, full technical notes, and audit filenames.'; return;}
      searchStatus.textContent = 'Searching…';
      try {const found = match(await index(), searchInput.value); if (generation !== searchGeneration) return;
        render(resultBox, found, searchInput.value, 30); searchStatus.textContent = `${found.length} matches${found.length > 30 ? ' · showing the first 30; refine your query' : ''}`;
      } catch (error) {searchStatus.textContent = error.message + ' Serve docs over HTTP for local search.';}
    }, 120);
  });
  const menu = document.getElementById('menu-toggle');
  menu.addEventListener('click', () => {const open = document.querySelector('.sidebar').classList.toggle('open'); menu.setAttribute('aria-expanded', String(open));});
  document.addEventListener('click', event => {if (window.innerWidth <= 760 && !event.target.closest('.sidebar') && !event.target.closest('#menu-toggle')) {document.querySelector('.sidebar').classList.remove('open'); menu.setAttribute('aria-expanded', 'false');}});
  const archive = document.getElementById('archive-results');
  if (archive) {
    const query = document.getElementById('archive-query'), type = document.getElementById('archive-type'), topic = document.getElementById('archive-topic');
    const count = document.getElementById('archive-count'), more = document.getElementById('archive-more');
    let rows, limit = 60;
    const update = () => {if (!rows) return; const found = match(rows, query.value, type.value, topic.value); render(archive, found, query.value, limit); count.textContent = `${found.length} records · showing ${Math.min(limit, found.length)}`; more.hidden = found.length <= limit;};
    index().then(data => {rows = data; [...new Set(rows.map(r => r.topic))].sort().forEach(value => {const option = document.createElement('option'); option.value = value; option.textContent = value; topic.append(option);}); update();}).catch(e => {count.textContent = e.message;});
    [query, type, topic].forEach(control => control.addEventListener('input', () => {limit = 60; update();}));
    more.addEventListener('click', () => {limit += 60; update();});
  }
})();
