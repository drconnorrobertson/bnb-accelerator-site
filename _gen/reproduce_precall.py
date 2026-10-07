"""Reproduce the public pre-call resources without funnel tracking or contact data.

Input: downloaded public HTML, never the personalized URL or its embedded state.
The retained DOM subtree contains the visible resource library, not source scripts.
"""
from html.parser import HTMLParser
from html import escape
from pathlib import Path
import re
import sys

class Node:
    def __init__(self, tag='', attrs=(), parent=None):
        self.tag, self.attrs, self.parent, self.children = tag, dict(attrs), parent, []
    def text(self):
        return ''.join(c.text() if isinstance(c, Node) else c for c in self.children)
    def find(self, predicate):
        result = [self] if predicate(self) else []
        for child in self.children:
            if isinstance(child, Node): result.extend(child.find(predicate))
        return result
    def html(self):
        if self.tag in {'script', 'style', 'noscript', 'form', 'input'}: return ''
        content = ''.join(c.html() if isinstance(c, Node) else escape(c) for c in self.children)
        allowed = {'class', 'href', 'src', 'alt', 'title', 'data-cols', 'loading', 'allow', 'allowfullscreen'}
        attrs = {k:v for k,v in self.attrs.items() if k in allowed}
        if self.tag == 'a': attrs.update(target='_self', rel='noopener noreferrer')
        if self.tag == 'iframe': attrs.update(loading='lazy', referrerpolicy='strict-origin')
        attr = ''.join(' '+k+(('="'+escape(v, quote=True)+'"') if v is not None else '') for k,v in attrs.items())
        if not self.tag: return content
        if self.tag in {'img', 'br', 'hr', 'meta', 'link'}: return '<'+self.tag+attr+'>'
        return '<'+self.tag+attr+'>'+content+'</'+self.tag+'>'

class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = self.current = Node()
    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.current); self.current.children.append(n)
        if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}: self.current = n
    def handle_endtag(self, tag):
        n = self.current
        while n.parent:
            if n.tag == tag: self.current = n.parent; return
            n = n.parent
    def handle_data(self, data): self.current.children.append(data)

def read_tree(path):
    parser = Tree(); parser.feed(Path(path).read_text()); return parser.root

def library_html(tree):
    library = tree.find(lambda n: n.attrs.get('class') == 'bnb-embed')[0]
    cards = [c for c in library.children if isinstance(c, Node)]
    output = []
    for i, card in enumerate(cards):
        headings = card.find(lambda n: n.tag in {'h2','h3','h4'})
        if i == 0:
            headings[0].children = ['Sample deal library']
            headings[1].children = ['Explore the original proformas and video breakdowns.']
        elif i == 1:
            headings[0].children = ['Client property case studies']
            for j, p in enumerate(card.find(lambda n:n.tag == 'p')):
                p.children = ['These source-provided client examples are historical, selected examples, not a representative performance sample. Verify current records, costs and availability independently. Proformas and third-party estimates are not realized net income.'] if j == 0 else []
        elif i == 12:
            output.append('<section class="bnb-card" id="your-plan"><h2>Your situation. Your purchase plan.</h2><p>Before the call, write down your available acquisition capital, cash reserve floor, income sources, ownership goals and the time you can realistically commit. Bring questions about financing, local permissions, management responsibilities and downside cash flow.</p><ul><li>What purchase budget leaves enough liquidity for setup, repairs and a slower launch?</li><li>What happens if revenue or the anticipated tax benefit is lower than expected?</li><li>Who is responsible for management oversight and material-participation records?</li><li>What services, fees and third-party work are included in the proposed engagement?</li></ul><p>A large tax bill alone does not make a property suitable. Review the investment independently of any potential deduction with your own qualified advisers.</p></section>')
            continue
        elif i == 32:
            links = card.find(lambda n:n.tag == 'a')
            output.append('<section class="bnb-card" id="research"><h2>Market research resources</h2><p>The original page links to the reports below, including research from 2024–2025. These are background reading, not a current forecast, a reason to rush a purchase, or evidence that an individual property will perform. Market definitions differ between reports; platform profits do not establish host profits.</p><ul>'+''.join('<li>'+a.html()+'</li>' for a in links)+'</ul></section>')
            continue
        if i == 17:
            headings[0].children = ['Market selection and the California question']
        elif i == 19:
            headings[0].children = ['Investment risk: what can go wrong?']
        for frame in card.find(lambda n:n.tag == 'iframe'):
            frame.attrs['title'] = (headings[0].text() if headings else 'Client case study video')
        for image in card.find(lambda n:n.tag == 'img'):
            image.attrs['alt'] = 'Original client case-study slide — historical example, not a promised result'
        html = card.html().replace('$$333,694', '$333,694')
        section_id = {0:'deals',1:'case-studies',2:'client-videos',13:'questions',25:'more-case-studies'}.get(i)
        if section_id: html = html.replace('<section ', '<section id="'+section_id+'" ', 1)
        if i == 0:
            html = html.replace('<ul ', '<p class="resource-note">Prices and “Total Entry” amounts are reproduced from the original page and have not been verified as current. They are not quotes, available inventory or guaranteed all-in budgets. Ask for current property-level underwriting.</p><label class="deal-search" for="deal-search">Find a sample by city, address or price<input id="deal-search" type="search" placeholder="Try Mesa, Denver or Broken Bow" autocomplete="off"></label><p id="deal-count" role="status" aria-live="polite"></p><ul ', 1)
        if i == 2:
            html = html.replace('<section ', '<section ',1).replace('<h2', '<p class="resource-note">Client-reported results and captions are historical and may omit costs or reflect different reporting periods. Results vary; no cash flow, occupancy, appreciation or tax savings are guaranteed.</p><h2',1)
        output.append(html)
    return '\n'.join(output)

if __name__ == '__main__':
    tree = read_tree(sys.argv[1])
    content = library_html(tree)
    if '--patch' in sys.argv:
        print('*** Begin Patch\n*** Update File: scb-precall/index.html\n@@\n-<!-- RESOURCE_LIBRARY -->')
        for line in content.splitlines(): print('+'+line)
        print('*** End Patch')
    else: print(content)
