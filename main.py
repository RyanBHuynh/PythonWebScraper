import requests
from bs4 import BeautifulSoup
import functions

# Code from cURL converter
headers_page_one = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0'
    }

data_page_one = {
    '__EVENTTARGET': 'ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderMainSingle$ppBESearch$bsPanel$stdbtnSearch$LinkStandardButton',
    '__VIEWSTATE': '/wEPDwULLTE5NzE0MzM3MTgPFgIeCVBhZ2VMb2JJRAIBFgJmD2QWAmYPZBYCAgMPZBYCAgEPZBYUAgEPZBYCAgEPFgQeA3NyYwVBfi9XZWJJbWFnZS5hc2h4P1JlYWRJbWFnZUZyb21DYWNoZT1UcnVlJkxvYWRCYW5uZXJJbWFnZT1UcnVlJmlkPTIeA2FsdAUcQnVzaW5lc3MgUmVnaXN0cmF0aW9uIEJhbm5lcmQCAw9kFgJmDw8WAh4HVmlzaWJsZWhkZAIEDxQrAAIUKwACDxYGHhxFbmFibGVFbWJlZGRlZEJhc2VTdHlsZXNoZWV0Zx4SUmVzb2x2ZWRSZW5kZXJNb2RlCylyVGVsZXJpay5XZWIuVUkuUmVuZGVyTW9kZSwgVGVsZXJpay5XZWIuVUksIFZlcnNpb249MjAyMS4xLjIyNC40NSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0AR4VRW5hYmxlRW1iZWRkZWRTY3JpcHRzZ2QQFgZmAgECAgIDAgQCBRYGFCsAAg8WCB4EVGV4dAUiQnVzaW5lc3MgUmVnaXN0cmF0aW9uIEZlZXMgJiBGb3Jtcx4LTmF2aWdhdGVVcmwFMmh0dHBzOi8vd3d3LnNvcy5tby5nb3YvYnVzaW5lc3MvY29ycG9yYXRpb25zL2Zvcm1zHgdUb29sVGlwBQxGZWVzICYgRm9ybXMeBlRhcmdldAUHX3BhcmVudGRkFCsAAg8WCB8HBRlCdXNpbmVzcyBSZWdpc3RyYXRpb24gRkFRHwgFJGh0dHBzOi8vd3d3LnNvcy5tby5nb3YvYnVzaW5lc3MvZmFxcx8JBRpGcmVxdWVudGx5IEFza2VkIFF1ZXN0aW9ucx8KBQdfcGFyZW50ZGQUKwACDxYIHwcFH0J1c2luZXNzIFJlZ2lzdHJhdGlvbiBIb21lIFBhZ2UfCAUsaHR0cHM6Ly93d3cuc29zLm1vLmdvdi9idXNpbmVzcy9jb3Jwb3JhdGlvbnMfCQURQ29ycG9yYXRpb25zIEhvbWUfCgUHX3BhcmVudGRkFCsAAg8WCB8HBSNCdXNpbmVzcyBSZWdpc3RyYXRpb24gT25saW5lIEZpbGluZx8IBSVodHRwczovL3d3dy5zb3MubW8uZ292L2JzZC91c2VyZ3VpZGVzHwkFFENvcnBvcmF0aW9uIFNlcnZpY2VzHwoFB19wYXJlbnRkZBQrAAIPFggfBwUgQnVzaW5lc3MgUmVnaXN0cmF0aW9uIENvbnRhY3QgVXMfCAU0aHR0cHM6Ly93d3cuc29zLm1vLmdvdi9idXNpbmVzcy9jb3Jwb3JhdGlvbnMvY29udGFjdB8JBQpDb250YWN0IFVzHwoFB19wYXJlbnRkZBQrAAIPFggfBwUfU3dpdGNoIHRvIEJ1c2luZXNzIFJlZ2lzdHJhdGlvbh8IBRovTG9naW5XZWxjb21lLmFzcHg/bG9iSUQ9MR8JBQRMYXdzHwoFB19wYXJlbnRkZA8WBmZmZmZmZhYBBXNUZWxlcmlrLldlYi5VSS5SYWRNZW51SXRlbSwgVGVsZXJpay5XZWIuVUksIFZlcnNpb249MjAyMS4xLjIyNC40NSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0ZBYMZg8PFggfBwUiQnVzaW5lc3MgUmVnaXN0cmF0aW9uIEZlZXMgJiBGb3Jtcx8IBTJodHRwczovL3d3dy5zb3MubW8uZ292L2J1c2luZXNzL2NvcnBvcmF0aW9ucy9mb3Jtcx8JBQxGZWVzICYgRm9ybXMfCgUHX3BhcmVudGRkAgEPDxYIHwcFGUJ1c2luZXNzIFJlZ2lzdHJhdGlvbiBGQVEfCAUkaHR0cHM6Ly93d3cuc29zLm1vLmdvdi9idXNpbmVzcy9mYXFzHwkFGkZyZXF1ZW50bHkgQXNrZWQgUXVlc3Rpb25zHwoFB19wYXJlbnRkZAICDw8WCB8HBR9CdXNpbmVzcyBSZWdpc3RyYXRpb24gSG9tZSBQYWdlHwgFLGh0dHBzOi8vd3d3LnNvcy5tby5nb3YvYnVzaW5lc3MvY29ycG9yYXRpb25zHwkFEUNvcnBvcmF0aW9ucyBIb21lHwoFB19wYXJlbnRkZAIDDw8WCB8HBSNCdXNpbmVzcyBSZWdpc3RyYXRpb24gT25saW5lIEZpbGluZx8IBSVodHRwczovL3d3dy5zb3MubW8uZ292L2JzZC91c2VyZ3VpZGVzHwkFFENvcnBvcmF0aW9uIFNlcnZpY2VzHwoFB19wYXJlbnRkZAIEDw8WCB8HBSBCdXNpbmVzcyBSZWdpc3RyYXRpb24gQ29udGFjdCBVcx8IBTRodHRwczovL3d3dy5zb3MubW8uZ292L2J1c2luZXNzL2NvcnBvcmF0aW9ucy9jb250YWN0HwkFCkNvbnRhY3QgVXMfCgUHX3BhcmVudGRkAgUPDxYIHwcFH1N3aXRjaCB0byBCdXNpbmVzcyBSZWdpc3RyYXRpb24fCAUaL0xvZ2luV2VsY29tZS5hc3B4P2xvYklEPTEfCQUETGF3cx8KBQdfcGFyZW50ZGQCBg8WAh4FY2xhc3MFEXN1Yi1oZWFkZXItYnV0dG9uZAIHDxYGHgRocmVmBSovQnVzaW5lc3NFbnRpdHkvQkVTZWFyY2guYXNweD9TZWFyY2hUeXBlPTAfCwUsc3ViLWhlYWRlci1idXR0b24gc3ViLWhlYWRlci1idXR0b24tc2VsZWN0ZWQeCWlubmVyaHRtbAUGU0VBUkNIZAIJDxYEHwwFGi9Mb2dpbldlbGNvbWUuYXNweD9sb2JJRD0wHw0FClVDQyBGSUxJTkdkAgsPFgIeB29uY2xpY2sFKGphdmFzY3JpcHQ6T3BlbkhlbHBGaWxlKCk7IHJldHVybiBmYWxzZTtkAhIPDxYCHwcFHFNlYXJjaCBmb3IgYSBCdXNpbmVzcyBFbnRpdHlkZAITD2QWAgIBD2QWAmYPZBYCAgMPZBYGAgEPFgIfA2gWAgIBDw8WBB8HZR8IBTRodHRwOi8vd3d3LnNvcy5tby5nb3YvYnVzaW5lc3MvY29ycG9yYXRpb25zL2ZhcXMuYXNwZGQCAw9kFgICAQ8PFgoeClBhZ2VGaWVsZHMy7gwAAQAAAP////8BAAAAAAAAAAwCAAAAVkZpbGVPbmUuU3lzdGVtV29ya3MuV2ViRXh0ZXJuYWwsIFZlcnNpb249MC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsBAEAAACoAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbRmlsZU9uZS5TeXN0ZW1Xb3Jrcy5XZWJFeHRlcm5hbC5TZWFyY2hGaWVsZCwgRmlsZU9uZS5TeXN0ZW1Xb3Jrcy5XZWJFeHRlcm5hbCwgVmVyc2lvbj0wLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXQMAAAAGX2l0ZW1zBV9zaXplCF92ZXJzaW9uBAAALUZpbGVPbmUuU3lzdGVtV29ya3MuV2ViRXh0ZXJuYWwuU2VhcmNoRmllbGRbXQIAAAAICAkDAAAAAQAAAAEAAAAHAwAAAAABAAAABAAAAAQrRmlsZU9uZS5TeXN0ZW1Xb3Jrcy5XZWJFeHRlcm5hbC5TZWFyY2hGaWVsZAIAAAAJBAAAAA0DDAUAAABzRmlsZU9uZUZyYW1ld29yay5EYXRhQWNjZXNzU2VydmljZS5EYXRhQ29udHJhY3RzLCBWZXJzaW9uPTAuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49ZDAzMmQxZWRhNDBiYzUxNwUEAAAAK0ZpbGVPbmUuU3lzdGVtV29ya3MuV2ViRXh0ZXJuYWwuU2VhcmNoRmllbGQCAAAAIDxTZWFyY2hGaWVsZFR5cGU+a19fQmFja2luZ0ZpZWxkIzxGaWVsZENvbmZpZ3VyYXRpb24+a19fQmFja2luZ0ZpZWxkBAQvRmlsZU9uZS5TeXN0ZW1Xb3Jrcy5XZWJFeHRlcm5hbC5TZWFyY2hGaWVsZFR5cGUCAAAASEZpbGVPbmVGcmFtZXdvcmsuRGF0YUFjY2Vzc1NlcnZpY2UuRGF0YUNvbnRyYWN0cy5jZk9ubGluZVZpc2libGVSZXFGaWVsZAUAAAACAAAABfr///8vRmlsZU9uZS5TeXN0ZW1Xb3Jrcy5XZWJFeHRlcm5hbC5TZWFyY2hGaWVsZFR5cGUBAAAAB3ZhbHVlX18ACAIAAAABAAAACQcAAAAFBwAAAEhGaWxlT25lRnJhbWV3b3JrLkRhdGFBY2Nlc3NTZXJ2aWNlLkRhdGFDb250cmFjdHMuY2ZPbmxpbmVWaXNpYmxlUmVxRmllbGQTAAAAGF9PbmxpbmVWaXNpYmxlUmVxRmllbGRJRBNfT25saW5lRmlsaW5nUGFnZUlEEl9PbmxpbmVQYWdlRmllbGRJRAtfRmllbGRMYWJlbBFfRmllbGREZXNjcmlwdGlvbhFfRmllbGRJbnN0cnVjdGlvbgpfSXNWaXNpYmxlC19Jc1JlcXVpcmVkDV9Jc01vZGlmaWFibGURX0RlZmF1bHRCb29sVmFsdWUQX0RlZmF1bHRJbnRWYWx1ZRFfRGVmYXVsdFRleHRWYWx1ZQ9fRG9jdW1lbnRUeXBlSWQLX0lzRGlzYWJsZWQUX0lzQXBwZW5kVG9GaWxlZENvcHkSX1JlY29yZGluZ1VzZXJOYW1lDl9SZWNvcmRpbmdUaW1lC19Sb3dWZXJzaW9uLURiT2JqZWN0QmFzZVRhYmxlKzxSb3dWZXJzaW9uPmtfX0JhY2tpbmdGaWVsZAAAAAEBAQAAAAADAQMAAAEAAAAICAgBAQEBblN5c3RlbS5OdWxsYWJsZWAxW1tTeXN0ZW0uSW50MzIsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dblN5c3RlbS5OdWxsYWJsZWAxW1tTeXN0ZW0uSW50MzIsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dAQENCAgFAAAAAAAAAAAAAAAAAAAABggAAAAGU0VBUkNICgoBAAAACgoKAAAGCQAAAAAfnUm0SubZiAAAAAAAAAAACx4cU2VhcmNoQ29udHJvbFZhbGlkYXRpb25Hcm91cAUKdmdCRVNlYXJjaB4UU2VhcmNoVHlwZUZvckNvbnRyb2xmHg9DYW5TZWFyY2hFbnRpdHloHiFJc0lEb05vdFdhbnRUb1NlYXJjaEJ1dHRvblZpc2libGVoZBYKAgIPZBYCAgEPZBYEAgEPDxYEHwcFngFFeGFjdCBNYXRjaCBzZWFyY2hlcyBzaG91bGQgaW5jbHVkZSBjb3Jwb3JhdGUgZGVzaWduYXRpb25zIChpbmMuLCBsbGMsIGV0Yy4pIGFuZCBwdW5jdHVhdGlvbi4gPGJyIC8+IFdlIHJlY29tbWVuZCB5b3UgZG8gbm90IGluY2x1ZGUgdGhlc2UgZm9yIG90aGVyIHNlYXJjaGVzLh8DZ2RkAgsPEGQQFQQNQnVzaW5lc3MgTmFtZRBSZWdpc3RlcmVkIEFnZW50EU5hbWUgQXZhaWxhYmlsaXR5C0NoYXJ0ZXIgTm8uFQQBMAExATIBMxQrAwRnZ2dnFgFmZAIED2QWCAIBDxYCHwNnFgoCAQ8PFgIfBwUcU2VhcmNoIGZvciBhIEJ1c2luZXNzIEVudGl0eWRkAgMPDxYEHg9WYWxpZGF0aW9uR3JvdXAFCnZnQkVTZWFyY2geDEVycm9yTWVzc2FnZQUcLSBCdXNpbmVzcyBOYW1lIGlzIHJlcXVpcmVkLmQWAmYPFgIeBXRpdGxlBRlCdXNpbmVzcyBOYW1lIGlzIHJlcXVpcmVkZAIFDw8WAh8HBQ1CdXNpbmVzcyBOYW1lZGQCCw8QZA8WBGYCAQICAgMWBBAFDVN0YXJ0aW5nIFdpdGgFATBnEAUJQWxsIFdvcmRzBQExZxAFCEFueSBXb3JkBQEyZxAFC0V4YWN0IE1hdGNoBQEzZ2RkAg0PEA8WAh8HBRhPbmx5IEFjdGl2ZSBDb3Jwb3JhdGlvbnNkZGRkAgMPZBYEAgMPDxYCHxQFCnZnQkVTZWFyY2hkZAIHDw8WAh8HZWRkAgUPZBYEAgUPDxYCHwdlZGQCBw8PFgIfFAUKdmdCRVNlYXJjaGRkAgcPZBYMAgMPEGRkFgFmZAIFDw8WAh8UBQp2Z0JFU2VhcmNoZGQCCw8PFgIfB2VkZAINDw8WAh8HZWRkAhEPDxYCHwdlZGQCFQ8QZA8WBGYCAQICAgMWBBAFDVN0YXJ0aW5nIFdpdGgFATBnEAUJQWxsIFdvcmRzBQExZxAFCEFueSBXb3JkBQEyZxAFC0V4YWN0IE1hdGNoBQEzZxYBZmQCBg8PFgIfA2hkFgJmD2QWAmYPZBYEAgMPFgQfDQUBLR8LBR5zd1RlbXBsYXRlQnV0dG9uRGl2VGV4dFRvcExlZnRkAgUPFgQfDQUBLR8LBSFzd1RlbXBsYXRlQnV0dG9uRGl2VGV4dEJvdHRvbUxlZnRkAgoPZBYCZg8PFg4fCQUGU2VhcmNoHhBDYXVzZXNWYWxpZGF0aW9uZx4PQ29tbWFuZEFyZ3VtZW50ZB4LQ29tbWFuZE5hbWVkHgtQb3N0QmFja1VybGQfFAUKdmdCRVNlYXJjaB4IVGFiSW5kZXgBAABkFgJmD2QWBAIDDxYEHw0FBlNFQVJDSB8LBSFzd1RlbXBsYXRlQnV0dG9uSWNvbkRpdlRleHRDZW50ZXJkAgUPFgIfDWVkAgwPZBYEAgMPPCsADgIAFCsAAmQXAQUIUGFnZVNpemUCFAEWAhYLDwIMFCsADDwrAAUBBAUMU2VsZWN0Q29sdW1uPCsABQEEBRRHcmlkQnVzaW5lc3NFbnRpdHlJRDwrAAUBBAUKU1dFbnRpdHlJRDwrAAUBBAUPQkVOYW1lRGF0YUJvdW5kFCsABRYCHgpIZWFkZXJUZXh0BQ1CdXNpbmVzcyBOYW1lZGRkBQpHcmlkQkVOYW1lPCsABQEEBQlCRUFkZHJlc3MUKwAFFgIfHAULQ2hhcnRlciBOby5kZGQFGkdyaWRCdXNpbmVzc0VudGl0eUlETnVtYmVyFCsABRYCHxwFBFR5cGVkZGQFCkdyaWRCRVR5cGUUKwAFFgIfHAUGU3RhdHVzZGRkBQxHcmlkQkVTdGF0dXM8KwAFAQQFDUdyaWRJc1ByaW1hcnkUKwAFFgIfHAUHQ3JlYXRlZGRkZAUOR3JpZERhdGVGb3JtZWQUKwAFFgIfHAUVUmVnaXN0ZXJlZCBBZ2VudCBOYW1lZGRkBQxHcmlkUmVnQWdlbnRkZRQrAAALKXlUZWxlcmlrLldlYi5VSS5HcmlkQ2hpbGRMb2FkTW9kZSwgVGVsZXJpay5XZWIuVUksIFZlcnNpb249MjAyMS4xLjIyNC40NSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0ATwrAAcACyl0VGVsZXJpay5XZWIuVUkuR3JpZEVkaXRNb2RlLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDIxLjEuMjI0LjQ1LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPTEyMWZhZTc4MTY1YmEzZDQBZGRkZGZkAgUPPCsADgIAFCsAAmQXAQUIUGFnZVNpemUCFAEWAhYLDwIHFCsABzwrAAUBBAUOR3JpZFJlZ0FnZW50SUQ8KwAFAQQFGEdyaWRSZWdBZ2VudEVudGl0eVJlY29yZDwrAAUBBAUQR3JpZFJlZ0FnZW50TmFtZTwrAAUBBAUSR3JpZFJlZ0FnZW50T2ZmaWNlPCsABQEEBRZHcmlkUmVnQWdlbnRSZXByZXNlbnRzPCsABQEEBQ5HcmlkQkVJRE51bWJlcjwrAAUBBAUMR3JpZEJFU3RhdHVzZGUUKwAACysFATwrAAcACysGAWRkZGRmZAIFDxYCHwNoZAIVDw8WBB8GZx8EZ2RkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBShjdGwwMCRjdGwwMCRBZGRpdGlvbmFsUXVpY2tMaW5rc0xlZnRNZW51BV9jdGwwMCRjdGwwMCRDb250ZW50UGxhY2VIb2xkZXJNYWluJENvbnRlbnRQbGFjZUhvbGRlck1haW5TaW5nbGUkcHBCRVNlYXJjaCRic1BhbmVsJGNiQWN0aXZlT25seVnRD1IMhjUpcWRwphxUD7lW9QCIIt3/vqTAyH3/AcuB',
    'ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderMainSingle$ppBESearch$bsPanel$tbBusinessName': 'A',
    'ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderMainSingle$ppBESearch$bsPanel$cbActiveOnly': 'on'
}

def main():
    get_business_data(headers_page_one, data_page_one, "page1")

def get_business_data(headers, data, page):
    # Create requests session
    s = requests.Session()

    # Make a POST request to the website
    response = s.post('https://bsd.sos.mo.gov/BusinessEntity/BESearch.aspx', headers=headers, data=data)

    path = "response_" + page + ".html"
    # Write response to an html file
    with open(path, "w") as f:
        f.truncate(0) # Clear old file
        f.write(response.text)

    # Convert website info to CSV
    soup = BeautifulSoup(open(path), 'html.parser')

    # Get header
    header_soup = soup.find_all("table",
                                id="ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBESearch_bsPanel_SearchResultGrid_ctl00")[0].find("thead")

    headers = [th.text.encode("utf-8") for th in header_soup.select("tr th")]
    headers = headers[4:]

    # Remove leading and trailing characters and convert to string
    functions.reformat_list(headers)

    # Get all the information in the body
    body = soup.find("table",
                     id="ctl00_ctl00_ContentPlaceHolderMain_ContentPlaceHolderMainSingle_ppBESearch_bsPanel_SearchResultGrid_ctl00").find_all("tbody")[2]

    parsed_table = functions.parse_body(body)

    # Write data to CSV
    functions.write_table_to_csv(headers, parsed_table, page + ".csv")

main()