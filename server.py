import aiohttp
from typing import Literal, Annotated
from pydantic import Field
from mcp.server.fastmcp import FastMCP

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/particle-media-particle-media-default/api/arxiv-research-paper-search'

mcp = FastMCP('arxiv-search')


@mcp.tool()
async def search_paper(search_term: Annotated[str, Field(description="Search term to query arXiv")],
                 field: Annotated[Literal["Title", "Authors", "Comments", "All fields"], Field(description="The field to search in: \"Title\", \"Authors\", \"Comments\", \"All fields\", Default is \"All fields\"")] = "All fields",
                 subject: Annotated[Literal["Computer Science", "Physics", "Economics", "Quantitative Biology", "Electrical Engineering and Systems Science", "Quantitative Finance", "Mathematics", "Statistics"] | None, Field(description='The subject area to filter papers by: "Computer Science", "Physics", "Economics", "Quantitative Biology", "Electrical Engineering and Systems Science", "Quantitative Finance", "Mathematics", and "Statistics". Default is None')] = None,
                 date_from: Annotated[str | None, Field(descritpion="The start date for filtering papers by submission date in 'YYYY-MM-DD' format. Default is None.")] = None,
                 date_to: Annotated[str | None, Field(descritpion="The end date for filtering papers by submission date in 'YYYY-MM-DD' format. Default is None.")] = None,
                 date_type: Annotated[Literal["Submission Date", "Original Submission Date", "Announced Date"], Field(description='The type of date to filter papers by. Default is "Submission Date".')] = "Submission Date",
                 num_results: Annotated[int, Field(description="The maximum number of results to return. Default is 50.")] = 50,
                 start: Annotated[int, Field(description="The starting index for pagination. Default is 0. 1 means the 2nd page, 2 means the 3rd page, etc.")] = 0
                 ):
    """
    Search for papers on arXiv based on various criteria.

    Parameters:
    - search_term (str): The term to search for in the paper metadata.
    - field (Literal["Title", "Author(s)", "Comments", "All fields"]): The field to search in. Default is "All fields".
    - subject (Literal["Computer Science", "Physics", "Economics", "Quantitative Biology", "Electrical Engineering and Systems Science", "Quantitative Finance", "Mathematics", "Statistics"] | None): The subject area to filter papers by. Default is None.
    - date_from (str | None): The start date for filtering papers by submission date in 'YYYY-MM-DD' format. Default is None.
    - date_to (str | None): The end date for filtering papers by submission date in 'YYYY-MM-DD' format. Default is None.
    - date_type (Literal["Submission Date", "Original Submission Date", "Announced Date"]): The type of date to filter papers by. Default is "Submission Date".
    - num_results (int): The maximum number of results to return. Default is 50.
    - start (int): The starting index for pagination. Default is 0. 1 means the 2nd page, 2 means the 3rd page, etc.

    Returns: List[dict]
        A list of dictionaries containing paper metadata, including URL, URL of pdf version, title, authors, abstract, submission date. and originally announced date.
    """
    
    url = "https://arxiv-research-paper-search.p.rapidapi.com/arxiv_search"
    headers = {'x-rapidapi-host': 'arxiv-research-paper-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        "search_term": search_term,
        "field": field,
        "subject": subject,
        "date_from": date_from,
        "date_to": date_to,
        "date_type": date_type,
        "num_results": num_results,
        "start": start
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=payload, timeout=30, raise_for_status=True, headers=headers) as r:
                response = await r.json()
                return response
    except Exception as e:
        logging.warning("", exc_info=True)
        return {"status": "failed", "reason": str(e)}


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
