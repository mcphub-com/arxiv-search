# arXiv Search MCP

The **arXiv Search MCP** provides a way to search the arXiv repository for scientific papers using a variety of filters and search parameters.

## Endpoint

### GET `/arxiv_search`

Search arXiv papers by keyword, with optional filters for specific fields, subject areas, date ranges, and pagination.

## Query Parameters

| Parameter    | Type    | Description                                                                                                                                          | Required | Default             |
|--------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------|
| `search_term`| string  | The search term to query arXiv papers.                                                                                                              | Yes      | —                   |
| `field`      | string  | The field to search in. Options: `"Title"`, `"Authors"`, `"Comments"`, `"All fields"`.                                                              | No       | `"All fields"`      |
| `subject`    | string  | Filter by subject area. Options include `"Computer Science"`, `"Physics"`, `"Economics"`, `"Quantitative Biology"`, `"Electrical Engineering and Systems Science"`, `"Quantitative Finance"`, `"Mathematics"`, `"Statistics"`. | No       | None (no filter)    |
| `date_from`  | string  | Start date filter for paper submission date, formatted as `'YYYY-MM-DD'`.                                                                           | No       | None                |
| `date_to`    | string  | End date filter for paper submission date, formatted as `'YYYY-MM-DD'`.                                                                             | No       | None                |
| `date_type`  | string  | The type of date to filter papers by. Options: `"Submission Date"`, `"Original Submission Date"`, `"Announced Date"`.                               | No       | `"Submission Date"`  |
| `num_results`| integer | Maximum number of results to return.                                                                                                                | No       | 50                  |
| `start`      | integer | Starting index for pagination. `0` means first page, `1` means second page, etc.                                                                     | No       | 0                   |

## Response

Under the `result` JSON key, this API returns an array of objects, each with title, abstract, authors, and URL.


---

This API is ideal for researchers and developers looking to programmatically access filtered paper metadata from arXiv.
