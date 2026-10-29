(() => {
  const base = document.body.dataset.base || './';
  const indexes = new Map();
  const loadIndex = name => {
    if (!indexes.has(name)) {
      indexes.set(name, fetch(base + `assets/${name}.json`).then(r => {
        if (!r.ok) throw new Error(`${name === 'browse' ? 'Browse' : 'Search'} index could not be loaded.`);
        return r.json();
      }).then(rows => rows.map(row => ({...row, text: row.text || '', haystack: (row.title + ' ' + row.topic + ' ' + (row.text || '')).toLowerCase()}))).catch(error => {
        indexes.delete(name); // A later edit or Reset can retry a failed request.
        throw error;
      }));
    }
    return indexes.get(name);
  };
  const index = () => loadIndex('search');
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
      } catch (error) {if (generation === searchGeneration) searchStatus.textContent = error.message + ' Serve docs over HTTP for local search.';}
    }, 120);
  });
  const menu = document.getElementById('menu-toggle');
  menu.addEventListener('click', () => {const open = document.querySelector('.sidebar').classList.toggle('open'); menu.setAttribute('aria-expanded', String(open));});
  document.addEventListener('click', event => {if (window.innerWidth <= 760 && !event.target.closest('.sidebar') && !event.target.closest('#menu-toggle')) {document.querySelector('.sidebar').classList.remove('open'); menu.setAttribute('aria-expanded', 'false');}});
  const archive = document.getElementById('archive-results');
  if (archive) {
    const query = document.getElementById('archive-query'), type = document.getElementById('archive-type'), topic = document.getElementById('archive-topic');
    const count = document.getElementById('archive-count'), more = document.getElementById('archive-more');
    const reset = document.getElementById('archive-reset');
    const allowedTypes = new Set([...type.options].map(option => option.value));
    let limit = 60, archiveGeneration = 0, archiveTimer;

    const setTopic = value => {
      // Preserve an incoming topic until the requested index supplies its list.
      if (value && ![...topic.options].some(option => option.value === value)) {
        const option = document.createElement('option'); option.value = value; option.textContent = value; topic.append(option);
      }
      topic.value = value;
    };
    const restore = () => {
      const params = new URL(window.location.href).searchParams;
      query.value = params.get('q') || '';
      const requestedType = params.has('type') ? params.get('type') : 'Note';
      type.value = allowedTypes.has(requestedType) ? requestedType : 'Note';
      setTopic(params.get('topic') || '');
      limit = 60;
    };
    const persist = method => {
      const url = new URL(window.location.href);
      const q = query.value.trim();
      if (q) url.searchParams.set('q', q); else url.searchParams.delete('q');
      // An explicit empty type means All types; absence means the Note default.
      if (type.value === 'Note') url.searchParams.delete('type'); else url.searchParams.set('type', type.value);
      if (topic.value) url.searchParams.set('topic', topic.value); else url.searchParams.delete('topic');
      if (url.href !== window.location.href) window.history[method](window.history.state, '', url);
    };
    const update = async () => {
      const generation = ++archiveGeneration;
      const requested = {query: query.value, type: type.value, topic: topic.value};
      const requestedLimit = limit;
      count.textContent = requested.query.trim() ? 'Searching…' : 'Loading the archive…';
      more.hidden = true;
      try {
        const rows = await loadIndex(requested.query.trim() ? 'search' : 'browse');
        if (generation !== archiveGeneration) return;
        const topics = [...new Set(rows.map(row => row.topic))].filter(Boolean).sort();
        topic.replaceChildren();
        const allTopics = document.createElement('option'); allTopics.value = ''; allTopics.textContent = 'All topics'; topic.append(allTopics);
        topics.forEach(value => {const option = document.createElement('option'); option.value = value; option.textContent = value; topic.append(option);});
        topic.value = topics.includes(requested.topic) ? requested.topic : '';
        // Canonicalize invalid incoming parameters without adding a history step.
        persist('replaceState');
        const found = match(rows, requested.query, requested.type, topic.value);
        render(archive, found, requested.query, requestedLimit);
        count.textContent = `${found.length} records · showing ${Math.min(requestedLimit, found.length)}`;
        more.hidden = found.length <= requestedLimit;
      } catch (error) {
        if (generation !== archiveGeneration) return;
        archive.replaceChildren();
        count.textContent = error.message + ' Serve docs over HTTP for local browsing. Change a filter or reset to retry.';
      }
    };
    query.addEventListener('input', () => {
      clearTimeout(archiveTimer); ++archiveGeneration; limit = 60; more.hidden = true;
      archiveTimer = setTimeout(() => {persist('replaceState'); update();}, 150);
    });
    [type, topic].forEach(control => control.addEventListener('change', () => {
      clearTimeout(archiveTimer); limit = 60; persist('pushState'); update();
    }));
    if (reset) reset.addEventListener('click', () => {
      clearTimeout(archiveTimer); query.value = ''; type.value = 'Note'; setTopic(''); limit = 60;
      persist('pushState'); update();
    });
    window.addEventListener('popstate', () => {clearTimeout(archiveTimer); restore(); update();});
    more.addEventListener('click', () => {limit += 60; update();});
    restore(); update();
  }
})();
