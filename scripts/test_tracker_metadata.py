"""Collision-only metadata; existing tracker routes, records and page bodies survive."""
import copy
import json
import re
import unittest
from build_tracker_proformas import collision_metadata, load, property_page

class TrackerMetadataTests(unittest.TestCase):
 def entry(self,slug='one',added='2026-06-19',row=7163,address='115 Ridgewood Ave'):
  return {'slug':slug,'address':address,'date_added':added,'history':[{'row':row}]}

 def test_ordinary_records_need_no_qualifier(self):
  self.assertEqual(collision_metadata([self.entry()]),{})
  self.assertEqual(collision_metadata([self.entry(),self.entry('two',address='Other address')]),{})

 def test_actual_dates_distinguish_collision_without_mutation(self):
  entries=[self.entry(),self.entry('two','2026-06-22',9956)]
  before=copy.deepcopy(entries);metadata=collision_metadata(entries)
  self.assertIn('Tracker entry added June 19, 2026',metadata['one'][0])
  self.assertIn('Tracker entry added June 22, 2026',metadata['two'][1])
  self.assertEqual(entries,before)
  self.assertEqual(metadata,collision_metadata(list(reversed(entries))))

 def test_missing_invalid_ambiguous_dates_use_real_source_row(self):
  for added in ['',None,'06/19/2026','2026-02-30','2026-6-19']:
   with self.subTest(added=added):
    metadata=collision_metadata([self.entry(added=added),self.entry('two','2026-06-22',9956)])
    self.assertIn('Tracker source row 7163',metadata['one'][0])
    self.assertNotIn('entry added',metadata['one'][0])

 def test_shared_dates_use_distinct_rows(self):
  metadata=collision_metadata([self.entry(),self.entry('two',row=9956)])
  self.assertIn('Tracker source row 7163',metadata['one'][0])
  self.assertIn('Tracker source row 9956',metadata['two'][0])

 def test_missing_or_duplicate_identifiers_fail_closed(self):
  for row in [None,0,'7163']:
   with self.subTest(row=row),self.assertRaises(ValueError):
    collision_metadata([self.entry(added='',row=row),self.entry('two',row=9956)])
  with self.assertRaises(ValueError):
   collision_metadata([self.entry(),self.entry('two')])

 def test_real_records_and_noncolliding_pages_are_preserved(self):
  records,_=load();before=copy.deepcopy(records);metadata=collision_metadata(records)
  expected={'115-ridgewood-ave-mary-esther-fl-32569','399-900-115-ridgewood-ave-mary-esther-fl-32569'}
  self.assertEqual(set(metadata),expected)
  self.assertEqual(records,before)
  ordinary=next(d for d in records if d['slug'] not in expected)
  self.assertEqual(property_page(ordinary),property_page(ordinary,metadata.get(ordinary['slug'])))
  for d in records:
   if d['slug'] not in expected:continue
   route,original=property_page(d);new_route,new=property_page(d,metadata[d['slug']])
   self.assertEqual(route,new_route)
   self.assertEqual(original[original.index('<main'):original.index('</main>')],new[new.index('<main'):new.index('</main>')])
   self.assertEqual(re.findall(r'<link rel="canonical"[^>]+>',original),re.findall(r'<link rel="canonical"[^>]+>',new))
   schemas=[json.loads(s) for s in re.findall(r'<script type="application/ld\+json">(.*?)</script>',new,re.S)]
   article=next(s for s in schemas if s.get('@type')=='Article')
   self.assertEqual(article['headline'],metadata[d['slug']][0])
   self.assertEqual(article['name'],metadata[d['slug']][0])
   self.assertEqual(article['datePublished'],'2026-10-08')
   self.assertEqual(article['dateModified'],'2026-10-08')

if __name__=='__main__':unittest.main()
