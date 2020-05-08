class Sort:

    def sort_id(self,response):
            data = response['data']
            idlist = [i['id'] for i in data]
            return idlist

    def sort_name(self,response):
            data = response['data']
            namelist = [n['name'] for n in data]
            return namelist
            
    def sort_servers(self,response):
            data = response['data']
            serverslist = [s['servers'] for s in data]
            return serverslist

    def sort_votes(self,response):
            data = response['data']
            voteslist = [v['votes'] for v in data]
            return voteslist

    def sort_intro(self,response):
            data = response['data']
            introlist = [i['intro'] for i in data]
            return introlist

    def sort_avatar(self,response):
            data = response['data']
            avatarlist = [a['avatar'] for a in data]
            return avatarlist

    def sort_category(self,response):
            data = response['data']
            categorylist = [c['category'] for c in data]
            return categorylist

    def sort_tag(self,response):
            data = response['data']
            taglist = [t['tag'] for t in data]
            return taglist

    def sort_state(self,response):
            data = response['data']
            statelist = [s['state'] for s in data]
            return statelist