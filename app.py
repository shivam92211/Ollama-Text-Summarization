import click
from langchain_community.llms import Ollama


# Defining the api path for Ollama connection
OLLAMA_BASE_URL = "http://localhost:11434/"
# Defining the model Qwen2-0.5B
OLLAMA_MODEL_NAME = "qwen2:0.5b"  


@click.command()
@click.argument("text", required=False) 
@click.option(
    "-t", 
    "--file", 
    type=click.File("r"), 
    help="Path to the text file to summarize."
)
def summarize(text, file):
    """
    Summarizes text from a file or takes text directly as input.

    Args:
        text (str, optional): Text to summarize. Defaults to None.
        file (click.File, optional): File object containing text to summarize.
            Defaults to None.
    """

    # Handling potential issues:
    if not (text or file):
        click.echo("Error: Please provide either text or a file path.")
        return

    # Reading text from either source
    if file:
        content = file.read()
    else:
        content = text

    # Creating Ollama client
    ollama = Ollama(base_url=OLLAMA_BASE_URL, model=OLLAMA_MODEL_NAME)

    # Improved prompt design with context and summary structure
    prompt = f"""
            Summarize the following text:
            {content.strip()}
            Please provide a concise summary of the key points in the text.
            """

    # Making the API call and handling potential errors
    try:
        response = ollama.invoke(prompt)
        summary = response.strip()  
        click.echo(f". Summary of {'text pasted' if not file else file.name}:")
        click.echo(summary)
    except Exception as e:
        click.echo(f"Error: An error occurred during summarization: {e}")


if __name__ == "__main__":
    summarize()
