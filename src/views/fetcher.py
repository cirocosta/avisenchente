import webapp2
from utils import fetcher
from models import usuario


class FetcherCron(webapp2.RequestHandler):
	""" View to be request by the cron for updating the database """

	tokens = usuario.Aparelho().get_tokens()
	for token in tokens:
		ff = fetcher.Fetcher(token)
		ff.update_database_data()