from app import app
from app import pages
from app import freezer

@freezer.register_generator
def post():
	print(list(pages))

	for page in set(pages):
		print(page.path)
		if page.path.startswith('post'):
			yield {"path" : page.path}

if __name__ == '__main__':
	freezer.freeze()