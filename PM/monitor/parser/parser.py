#-*- coding: utf-8 -*-

import re
import urllib2

from bs4 import BeautifulSoup

class Parser:
    class ClassNames:
        FOREIGN_PPOMPPU_TITLE_0 = 'list0'
        FOREIGN_PPOMPPU_TITLE_1 = 'list1'
        
        FOREIGN_PPOMPPU_TITLE_CLASS_ENABLED = 'list_title'
        FOREIGN_PPOMPPU_TITLE_COLOR_DISABLED = '#ACACAC'
        
    class Urls:
        PPOMPPU = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'
        FOREIGN_PPOMPPU = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu4'
        
    URLS = { '�˻ѰԽ���': 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu',
               '�ؿܻ˻�': 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu4' }
            
    def __init__(self):
        self.entries = {}
        
    def _get_entries(self, url):
        entries = []
        
        response = urllib2.urlopen(url)
        html = response.read().decode("cp949", "ignore").encode("utf-8", "ignore")
        
        bs = BeautifulSoup(html)
        titles_tags = ( bs.findAll('tr', { 'class': self.ClassNames.FOREIGN_PPOMPPU_TITLE_0 } ) 
                   + bs.findAll('tr', { 'class': self.ClassNames.FOREIGN_PPOMPPU_TITLE_1 }) )
        
        for title in titles_tags:
        
            # [0] Index, [1] Category, [2] Author, [3] Subject & Comments, 
            # [4] Time, [5] Recommend, [6] View
            attributes = title.find_all('td', recursive = False )
                    
            # [0] Index
            index = attributes[0].string
            
            # [1] Category
            category = attributes[1].nobr.string
            
            # [2] Author
            author_object = attributes[2].find('span', { 'class': 'list_name' } )
            if author_object == None:
                author_image = attributes[2].find('img')
                author = author_image['alt']
            else:
                author = author_object.string 
            
            # [3] Subject & Comments
            subject_tag = attributes[3].find('font', { 'class': self.ClassNames.FOREIGN_PPOMPPU_TITLE_CLASS_ENABLED } )
            active = True
                 
            if subject_tag == None:
                subject_tag = attributes[3].find('font', { 'color': self.ClassNames.FOREIGN_PPOMPPU_TITLE_COLOR_DISABLED } )
                active = False
            
            subject = subject_tag.string
            link = subject_tag.parent['href']
            
            if subject_tag.parent.parent.find('span', {'class':'list_comment2'}) == None:
                comment_number = 0
            else:
                comment_number = int(subject_tag.parent.parent.find('span', {'class':'list_comment2'}).span.string)
            
            # [4] Time
            time = attributes[4].nobr.string
            
            # [5] Recommend
            recommend = attributes[5].string
            
            # [6] View
            view = int(attributes[6].string)
            
            entries.append ( { 'index': index, 'category': category, 'author': author, 
                              'subject': subject, 'link': link, 'comment_number': comment_number,
                              'time': time, 'recommend': recommend, 'view': view, 'active': active } )

        return entries    
    
    def refresh_all(self):
        for url in self.entries.keys():
            self.entries[url] = self._get_entries(url)
              
    def get_ppomppu_entries(self):
        self.entries[self.Urls.PPOMPPU] = self._get_entries(self.Urls.PPOMPPU)
        return self.entries[self.Urls.PPOMPPU]
        
    def get_foreign_ppomppu_entries(self):
        self.entries[self.Urls.FOREIGN_PPOMPPU] = self._get_entries(self.Urls.FOREIGN_PPOMPPU)
        return self.entries[self.Urls.FOREIGN_PPOMPPU]
    
    # return tuple list like [ ('a', entry object), ('b', entry object) ... ]
    def match_titles(self, url, keywords):
        matched_entries = []
        
        # check if there's the matching url in enties
        if url in self.entries:
            for entry in self.entries[url]:
                for keyword in keywords:
                    # if the keyword was in subject.. 
                    if entry['subject'].find(keyword.search_word) != -1:
                        matched_entries.append((keyword, entry))
                      
        return matched_entries
    
    def match_ppomppu_titles(self, keyword):
        # if there were no entries for ppomppu, get it from the Internet
        # if not self.Urls.PPOMPPU in self.entries:
        #    self.get_ppomppu_entries()
            
        # pick each entries and try to find whether the keyword is included or not         
        # for entry in entries:
        #    for fp_title in fp_title_objects:
                
        #        print "Searching... %s in %s" % ( fp_title['subject'], entry.keyword.text )
                
                # If there is keyword in the title...
        #        if fp_title['subject'].find(entry.keyword.text) != -1:
        #            print "Found"        
            
        pass 
    
    def match_foreign_ppomppu_titles(self, keyword):
        pass
        