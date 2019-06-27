import click
import string

def eliminateDigits(str):
	newStr = ""
	for index in range(len(str)):
		if str[index] in string.ascii_letters:
			newStr = newStr+str[index]
	
	return newStr



@click.option('--removedigits/ --no-removedigits', default=False, 
				help='remove digits from input ')
				
@click.group()
@click.pass_context
def strcmd(PrevOption, removedigits):
	
	"""Supports some string commands from command"""
	PrevOption.obj['rmDigit'] = removedigits

	
@strcmd.command('concat')
@click.option('-d', '--delimiter', default=':')
@click.argument('TOKENS', nargs=-1)
@click.pass_context
def concat(PrevOption, **args):

	"""pass one or more strings, concat them with delimiter and print them out"""

	removeDigits = PrevOption.obj['rmDigit']
	delimiter = args['delimiter']
	tokens = args['tokens']
	result = ""

	for value in tokens:
		if(removeDigits):
			value = eliminateDigits(value)
		
		if(result == ""):
			result = result+value
		else:
			result = result+delimiter+value
		
	click.echo(result)
	

@strcmd.command('lower')
@click.argument('TOKENS', nargs=-1)
@click.pass_context
def lower(PrevOption, **tokens):
	"""Converts the given word to lower case letters"""
	tokens = tokens['tokens']
	
	removeDigits = PrevOption.obj['rmDigit']
	
	result = ""
	
	for token in tokens:
		
		if(removeDigits):
			token = eliminateDigits(token)
		
		result = result+token.lower()
			
	click.echo(result)
	
@strcmd.command('upper')
@click.argument('TOKENS', nargs=-1)
@click.pass_context
def upper(PrevOption, **tokens):
	"""Converts the given word to upper case letters"""
	
	removeDigits = PrevOption.obj['rmDigit']
	tokens = tokens['tokens']
	
	result = ""
	
	for token in tokens:

		if(removeDigits):
			token = eliminateDigits(token)
			
		result = result+token.upper()

	click.echo(result)

	

	
	
	
	
if __name__ == '__main__':
	strcmd(obj = {})

