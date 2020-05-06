import aiohttp
import asyncio

class GetById:
	
	def __init__(self, response):
		self.id = self.bot_id(response)
		self.timestamp = self.bot_timestamp(response)
		self.name  = self.bot_name(response)
		self.owner = self.bot_owner(response)
		self.library = self.bot_library(response)
		self.prefix = self.bot_prefix(response)
		self.votes = self.bot_votes(response)
		self.servers = self.bot_servers(response)
		self.intro = self.bot_intro(response)
		self.description = self.bot_description(response)
		self.web = self.bot_web(response)
		self.git = self.bot_git(response)
		self.url = self.bot_URL(response)
		self.discord = self.bot_support_discord(response)
		self.categories = self.bot_category(response)
		self.status = self.bot_status(response)
		self.avatar = self.bot_avatar(response)
		self.verified = self.bot_verified(response)
		self.trusted = self.bot_trusted(response)
		self.state = self.bot_state(response)

	@classmethod
	async def get_response(cls, bot_id):
		URL = f'https://api.koreanbots.cf/bots/get/{bot_id}'
		async with aiohttp.ClientSession() as cs:
			async with cs.get(URL) as r:
				response = await r.json()
				return response

	@classmethod
	def bot_id(cls, response):
		data = response['data']
		return data['id']

	@classmethod
	def bot_timestamp(cls, response):
		data = response['data']
		bot_timestamp = data['date']
		return bot_timestamp

	@classmethod
	def bot_name(cls, response):
		data = response['data']
		bot_name = data['name']
		return bot_name

	@classmethod
	def bot_timestamp(cls, response):
		data = response['data']

	@classmethod
	def bot_owner(cls, response):
		data = response['data']
		owner = data['owners']
		return owner

	@classmethod
	def bot_library(cls, response):
		data = response['data']
		library = data['lib']
		return library

	@classmethod
	def bot_prefix(cls, response):
		data = response['data']
		prefix = data['prefix']
		return prefix

	@classmethod
	def bot_votes(cls, response):
		data = response['data']
		votes = data['votes']
		return votes

	@classmethod
	def bot_servers(cls, response):
		data = response['data']
		servers = data['servers']
		return servers

	@classmethod
	def bot_intro(cls, response):
		data = response['data']
		intro = data['intro']
		return intro

	@classmethod
	def bot_description(cls, response):
		data = response['data']
		description = data['desc']
		return description

	@classmethod
	def bot_web(cls, response):
		data = response['data']
		web = data['web']
		return web

	@classmethod
	def bot_git(cls, response):
		data = response['data']
		git = data['git']
		return git

	@classmethod
	def bot_URL(cls, response):
		data = response['data']
		URL = data['url']
		return URL
	
	@classmethod
	def bot_support_discord(cls, response):
		data = response['data']
		support_discord = data['discord']
		return support_discord

	@classmethod
	def bot_category(cls, response):
		data = response['data']
		category = data['category']
		return category

	@classmethod
	def bot_status(cls, response):
		data = response['data']
		status = data['status']
		return status

	@classmethod
	def bot_avatar(cls, response):
		data = response['data']
		avatar = data['avatar']
		return avatar

	@classmethod
	def bot_verified(cls, response):
		data = response['data']
		verified = data['verified']
		return verified

	@classmethod
	def bot_trusted(cls, response):
		data = response['data']
		trusted = data['trusted']
		return trusted

	@classmethod
	def bot_state(cls, response):
		data = response['data']
		state = data['state']
		return state